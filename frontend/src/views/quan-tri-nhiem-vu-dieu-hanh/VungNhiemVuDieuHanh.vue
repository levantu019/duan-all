<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-data-table
          :headers="headers"
          :items="listVungNhiemVu"
          :search="search"
          class="elevation-1"
          height="calc(50vh - 235px)"
          :footer-props="{
            'items-per-page-text': 'Hiển thị 1 trang',
            'items-per-page-options': [10, 15, 20],
          }"
          fixed-header
          :loading="isLoading"
          loading-text="Loading...Please wait"
        >
          <v-divider></v-divider>
          <template v-slot:top>
            <v-toolbar flat color="white">
              <div class="d-flex">
                <v-text-field
                  v-model="search"
                  append-icon="mdi-magnify"
                  label="Tìm kiếm"
                  dense
                  outlined
                  single-line
                  hide-details
                ></v-text-field>
                <v-btn
                  color="primary"
                  class="ml-2 white--text"
                  @click="addNewPosition()"
                >
                  <v-icon dark>mdi-plus</v-icon>Thêm mới
                </v-btn>
              </div>
            </v-toolbar>
          </template>
          <template v-slot:[`item.tenVung`]="{ item }">
            <v-text-field
              v-model="editedItem.properties.tenVung"
              :hide-details="true"
              dense
              single-line
              v-if="item.id === editedItem.id"
            ></v-text-field>
            <span v-else>{{ item.properties.tenVung }}</span>
          </template>
          <template v-slot:[`item.actions`]="{ item }">
            <div v-if="item.id === editedItem.id">
              <v-icon color="red" class="mr-3" @click="close">
                mdi-window-close
              </v-icon>
              <v-icon color="green" @click="save"> mdi-content-save </v-icon>
            </div>
            <div v-else>
              <v-icon color="yellow" class="mr-2" @click="zoomToPolygon(item)">
                mdi-map-marker
              </v-icon>
              <v-icon color="green" class="mr-3" @click="editItem(item)">
                mdi-square-edit-outline
              </v-icon>
              <v-icon color="red" @click="deleteItem(item)">
                mdi-delete
              </v-icon>
            </div>
          </template>
          <template v-slot:[`item.nvdh`]="{ item }">
            <v-select
              :items="listNhiemVu"
              v-model="editedItem.properties.nvdh"
              label="Nhiệm vụ"
              v-if="item.id === editedItem.id"
              dense
              :hide-details="true"
              required
              item-text="tenNVDH"
              item-value="maNhanDang"
            ></v-select>
            <span v-else
              >{{ item.properties.nvdh | convertNVDH(listNhiemVu) }}
            </span>
          </template>
          <template v-slot:[`item.moTaVung`]="{ item }">
            <v-text-field
              v-model="editedItem.properties.moTaVung"
              :hide-details="true"
              dense
              single-line
              v-if="item.id === editedItem.id"
            ></v-text-field>
            <span v-else>{{ item.properties.moTaVung }}</span>
          </template>
          <template v-slot:[`item.ngayVung`]="{ item }">
            <v-menu
              v-model="menu2"
              :close-on-content-click="false"
              transition="scale-transition"
              offset-y
              min-width="auto"
              v-if="item.id === editedItem.id"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  prepend-icon="mdi-calendar"
                  v-model="item.properties.ngayVung"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                v-model="item.properties.ngayVung"
                @input="menu2 = false"
                no-title
              ></v-date-picker>
            </v-menu>

            <span v-else>{{ item.properties.ngayVung }}</span>
          </template>
          <template v-slot:[`body.append`]>
            <span></span>
          </template>
        </v-data-table>
      </v-col>
    </v-row>
    <v-row>
      <MapComponent />
    </v-row>
  </v-container>
</template>

<script>
// api
import vungNhiemVuDieuHanh from "@/api/vung-nhiem-vu-dieu-hanh";
import nhiemVuDieuHanh from "@/api/nhiem-vu-dieu-hanh";

import OlEditController from "@/controllers/OlEdtiController";
import MapComponent from "@/components/ol/MapComponent.vue";
import { EventBus } from "@/EventBus";
import { getAllChildLayers } from "@/utils/Layer";
import { mapMutations, mapGetters } from "vuex";
import editLayerHelper from "@/controllers/OlEditLayerHelper";
import { InteractionsToggle } from "@/mixins/InteractionsToggle";
import { Mapable } from "@/mixins/Mapable";
import { KeyShortcuts } from "@/mixins/KeyShortcuts";
// import OlStyleDefs from "@/style/OlStyleDefs";

export default {
  mixins: [InteractionsToggle, Mapable, KeyShortcuts],
  components: {
    MapComponent,
  },
  data() {
    return {
      interactionType: "edit-interaction",
      layerName: "geo_vungNVDH",
      dataObject: {},
      search: "",
      geotype: "",
      menu2: false,

      isLoading: false,
      isAdding: false,

      headers: this.$appConfig.vungNhiemVuDieuHanh.headers,

      listVungNhiemVu: [],
      listNhiemVu: [],

      editedIndex: -1,
      editedItem: {
        geometry: {},
        id: "",
        properties: {
          maVung: "",
          moTaVung: "",
          ngayVung: "",
          nvdh: 0,
        },
      },
      defaultItem: {
        geometry: {},
        id: "",
        properties: {
          maVung: "",
          moTaVung: "",
          ngayVung: "",
          nvdh: 0,
        },
      },
    };
  },
  mounted() {},
  created() {
    this.initData().then(() => {
      this.onMapBound();
    });
  },

  methods: {
    ...mapMutations("draw", {
      setGeometry: "SET_GEOMETRY",
    }),
    ...mapMutations("map", {
      toggleSnackbar: "TOGGLE_SNACKBAR",
    }),

    async initData() {
      try {
        this.isLoading = true;

        const [listFeatures, listNhiemVu] = await Promise.all([
          vungNhiemVuDieuHanh.getAll({}),
          nhiemVuDieuHanh.getAll({}),
        ]);

        console.log(listFeatures, listNhiemVu);

        this.listVungNhiemVu = [...listFeatures.features];
        this.listNhiemVu = listNhiemVu;

        this.isLoading = false;
      } catch (error) {
        console.log(error);
      }
    },

    onMapBound() {
      const me = this;

      //init ol edit controller
      me.olEditCtrl = new OlEditController(this.$map);

      me.olEditCtrl.createEditLayer();

      const editableLayers = getAllChildLayers(this.$map).filter(
        (layer) => layer.get("name") === this.layerName
      );

      //add Feature to Layer
      this.selectedLayer = editableLayers[0];
      editLayerHelper.selectedLayer = this.selectedLayer;

      editLayerHelper.addFeaturesToSource(
        this.selectedLayer,
        this.listVungNhiemVu
      );
    },

    editItem(item) {
      this.isEditing = true;

      this.editedIndex = this.listVungNhiemVu.indexOf(item);

      this.editedItem = Object.assign({}, item);

      if (!this.isAdding && this.isEditing) {
        const editType = "modify";
        const startCb = this.onDrawStart;
        const endCb = this.onDrawModifyEnd;

        this.olEditCtrl.addInteraction(editType, startCb, endCb, item);

        EventBus.$emit("ol-interaction-activated", this.interactionType);
      }
    },

    async deleteItem(item) {
      const index = this.listVungNhiemVu.indexOf(item);
      if (confirm("Are you sure you want to delete this item?")) {
        // await vungNhiemVuDieuHanh.delete(item);
        this.listVungNhiemVu.splice(index, 1);

        //remove Feature
        editLayerHelper.removeFeatureFromSource(this.selectedLayer, item);
      }
    },

    close(isSaved) {
      this.editedItem = Object.assign({}, this.defaultItem);
      this.editedIndex = -1;

      this.isAdding && !isSaved && this.listTuyenNhiemVu.shift();

      this.stop();

      this.isAdding = false;
      this.isEditing = false;
    },
    addNewPosition() {
      const me = this;
      // me.createLayerToDraw();
      this.isAdding = true;

      this.toggleSnackbar({
        type: "warning",
        message: "Chọn Vùng nhiệm vụ điều hành",
        state: true,
        timeout: 2000,
      });

      const editType = "add";

      if (editType !== undefined) {
        const startCb = this.onDrawStart;
        const endCb = this.onDrawEnd;

        me.olEditCtrl.addInteraction(editType, startCb, endCb, null);

        EventBus.$emit("ol-interaction-activated", me.interactionType);
      }
    },
    addNewMission() {
      this.stop();
      this.toggleSnackbar({
        type: "warning",
        message: "Nhập thông tin Tuyến nhiệm vụ điều hành",
        state: true,
        timeout: 2000,
      });

      const addObj = Object.assign({}, this.defaultItem);

      this.listVungNhiemVu.unshift(addObj);

      this.editItem(addObj);
    },

    stop() {
      const me = this;

      me.olEditCtrl.clear();

      EventBus.$emit("ol-interaction-stopped", me.interactionType);
    },
    onDrawModifyEnd(evt) {
      if (evt.features.getArray().length > 0) {
        const feature = evt.features.getArray()[0];

        const featureGeometry = feature
          .getGeometry()
          .clone()
          .transform("EPSG:3857", "EPSG:4756");

        this.setGeometry(featureGeometry);
      }
    },
    onDrawStart() {
      this.olEditCtrl.featuresToCommit = [];
    },
    onDrawEnd(evt) {
      const me = this;
      const feature = evt.feature;

      const featureGeometry = feature
        .getGeometry()
        .clone()
        .transform("EPSG:3857", "EPSG:4756");

      this.setGeometry(featureGeometry);

      me.stop();

      me.addNewMission();
    },

    async save() {
      const join = this.geometry.getCoordinates()[0].map((el) => el.join(" "));

      const coordinates = join.join(",");

      const requestData = {
        ...this.editedItem.properties,
        id: this.editedItem.id,
        geoVung: `SRID=4756;POLYGON((${coordinates}))`,
      };

      const { tenVung, ngayVung } = requestData;
      if (tenVung.length === 0 || ngayVung.length === 0) {
        //Thong Bao
        return;
      }

      try {
        let result;
        if (this.isAdding) {
          result = await vungNhiemVuDieuHanh.create(requestData);
        } else if (this.isEditing) {
          result = await vungNhiemVuDieuHanh.edit(requestData);
        }
        if (!!result && this.editedIndex > -1) {
          Object.assign(this.listVungNhiemVu[this.editedIndex], result);
          //Thong bao
          this.toggleSnackbar({
            type: "success",
            message: "Thêm nhiệm vụ điều hành thành công",
            state: true,
            timeout: 2000,
          });
        }
      } catch (error) {
        console.log(error);
      }
      this.close(true);
      this.stop();
      this.onMapBound();
    },
    zoomToPolygon(item) {
      const feature = editLayerHelper.createFeature(item);
      const fitOptions = { duration: 1000 };
      this.$map.getView().fit(feature.getGeometry(), fitOptions);
    },
  },
  computed: {
    ...mapGetters("draw", {
      geometry: "geometry",
    }),
  },
  filters: {
    convertNVDH: (nvdh, listNV) => {
      if (!nvdh) return "";
      return listNV.filter((nv) => nv.maNhanDang === nvdh)[0].tenNVDH;
    },
  },
};
</script>

<style>
.theme--light.v-data-table.v-data-table--fixed-header thead th {
  background: rgb(160, 159, 159) !important;
}
</style>
