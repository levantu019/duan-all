<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-data-table
          :headers="headers"
          :items="listDiemNhiemVu"
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
          item-key="name"
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
                  :disabled="isAdding"
                >
                  <v-icon dark>mdi-plus</v-icon>Thêm mới
                </v-btn>
              </div>
            </v-toolbar>
          </template>
          <template v-slot:[`item.tenDiem`]="{ item }">
            <v-text-field
              v-model="editedItem.properties.tenDiem"
              :hide-details="true"
              dense
              label="Tên điểm"
              required
              :rules="nameRules"
              v-if="item.id === editedItem.id"
            ></v-text-field>
            <span v-else>{{ item.properties.tenDiem }}</span>
          </template>
          <template v-slot:[`item.actions`]="{ item }">
            <div v-if="item.id === editedItem.id">
              <v-icon color="red" class="mr-2" @click="close(false)">
                mdi-window-close
              </v-icon>
              <v-icon color="green" @click="save"> mdi-content-save </v-icon>
            </div>
            <div v-else>
              <v-icon color="yellow" class="mr-2" @click="zoomToPoint(item)">
                mdi-map-marker
              </v-icon>
              <v-icon color="green" class="mr-2" @click="editItem(item)">
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
              :rules="nameRules"
            ></v-select>
            <span v-else>{{
              item.properties.nvdh | convertNVDH(listNhiemVu)
            }}</span>
          </template>
          <template v-slot:[`item.moTaDiem`]="{ item }">
            <v-text-field
              v-model="editedItem.properties.moTaDiem"
              :hide-details="true"
              dense
              single-line
              v-if="item.id === editedItem.id"
            ></v-text-field>
            <span v-else>{{ item.properties.moTaDiem }}</span>
          </template>
          <template v-slot:[`item.ngayDiem`]="{ item }">
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
                  v-model="editedItem.properties.ngayDiem"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                v-model="editedItem.properties.ngayDiem"
                @input="menu2 = false"
                no-title
              ></v-date-picker>
            </v-menu>

            <span v-else>{{ item.properties.ngayDiem }}</span>
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
import OlEditController from "@/ controllers/OlEdtiController";
import diemNhiemVuDieuHanh from "@/api/diem-nhiem-vu-dieu-hanh";
import MapComponent from "@/components/ol/MapComponent.vue";
import { EventBus } from "@/EventBus";
import { getAllChildLayers } from "@/utils/Layer";
import { mapGetters, mapMutations } from "vuex";
import editLayerHelper from "@/ controllers/OlEditLayerHelper";
import { InteractionsToggle } from "@/mixins/InteractionsToggle";
import { Mapable } from "@/mixins/Mapable";
import { KeyShortcuts } from "@/mixins/KeyShortcuts";
import nhiemVuDieuHanh from "@/api/nhiem-vu-dieu-hanh";

export default {
  mixins: [InteractionsToggle, Mapable, KeyShortcuts],
  components: {
    MapComponent,
  },
  data() {
    return {
      interactionType: "edit-interaction",
      layerName: "geo_diemNVDH",
      selectedLayer: null,

      dataObject: {},
      search: "",
      geotype: "",
      menu2: false,

      isLoading: false,
      isAdding: false,
      isEditing: false,

      headers: this.$appConfig.diemNhiemVuDieuHanh.headers,
      nameRules: [(v) => !!v || "Name is required"],

      listDiemNhiemVu: [],
      listNhiemVu: [],
      test: null,

      editedIndex: -1,
      editedItem: {
        geometry: {},
        id: "",
        properties: {
          tenDiem: "",
          moTaDiem: "",
          ngayDiem: "",
          nvdh: 0,
        },
      },
      defaultItem: {
        geometry: {},
        id: "",
        properties: {
          tenDiem: "",
          moTaDiem: "",
          ngayDiem: "",
          nvdh: 0,
        },
      },
    };
  },
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

        const listFeatures = await diemNhiemVuDieuHanh.getAll({});
        const listNhiemVu = await nhiemVuDieuHanh.getAll({});

        this.listDiemNhiemVu = [...listFeatures.results.features];
        this.test = listFeatures.results;

        this.listNhiemVu = listNhiemVu.results.map(({ maNVDH, tenNVDH }) => ({
          value: maNVDH,
          text: tenNVDH,
        }));

        this.isLoading = false;
      } catch (error) {
        console.log(error);
      }
    },

    onMapBound() {
      this.olEditCtrl = new OlEditController(this.$map);
      this.olEditCtrl.createEditLayer();

      const editableLayers = getAllChildLayers(this.$map).filter(
        (layer) => layer.get("name") === this.layerName
      );

      //add Feature to Layer
      this.selectedLayer = editableLayers[0];
      editLayerHelper.selectedLayer = this.selectedLayer;

      editLayerHelper.addFeaturesToSource(
        this.selectedLayer,
        this.listDiemNhiemVu
      );
    },

    editItem(item) {
      this.isEditing = true;

      this.editedIndex = this.listDiemNhiemVu.indexOf(item);

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
      const index = this.listDiemNhiemVu.indexOf(item);
      if (confirm("Are you sure you want to delete this item?")) {
        await diemNhiemVuDieuHanh.delete(item);
        this.listDiemNhiemVu.splice(index, 1);

        //remove Feature
        editLayerHelper.removeFeatureFromSource(this.selectedLayer, item);
      }
    },

    close(isSaved) {
      this.editedItem = Object.assign({}, this.defaultItem);
      this.editedIndex = -1;

      this.isAdding && !isSaved && this.listDiemNhiemVu.shift();

      this.stop();

      this.isAdding = false;
      this.isEditing = false;
    },
    addNewPosition() {
      const me = this;
      // me.createLayerToDraw();
      this.isAdding = true;

      this.toggleSnackbar({
        type: "error",
        message: "Chọn điểm nhiệm vụ điều hành",
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
        type: "error",
        message: "Nhập thông tin điểm nhiệm vụ điều hành",
        state: true,
        timeout: 2000,
      });

      const addObj = Object.assign({}, this.defaultItem);

      this.listDiemNhiemVu.unshift(addObj);

      this.editItem(addObj);
    },

    zoomToPoint(item) {
      const view = this.$map.getView();
      editLayerHelper.zoomToPoint(view, item, 18);
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
        .transform("EPSG:3857", "EPSG:4326");

      this.setGeometry(featureGeometry);

      me.stop();

      me.addNewMission();
    },
    onDrawModifyEnd(evt) {
      if (evt.features.getArray().length > 0) {
        const feature = evt.features.getArray()[0];

        const featureGeometry = feature
          .getGeometry()
          .clone()
          .transform("EPSG:3857", "EPSG:4326");

        this.setGeometry(featureGeometry);
      }
    },
    stop() {
      this.olEditCtrl.clear();
      EventBus.$emit("ol-interaction-stopped", this.interactionType);
    },

    async save() {
      const requestData = {
        ...this.editedItem.properties,
        id: this.editedItem.id,
        geoDiem: `SRID=4326;POINT(${this.geometry.flatCoordinates[0]} ${this.geometry.flatCoordinates[1]})`,
      };

      const { tenDiem, ngayDiem } = requestData;

      if (tenDiem.length === 0 || ngayDiem.length === 0) {
        //Thong Bao
        return;
      }
      try {
        let result;
        if (this.isAdding) {
          result = await diemNhiemVuDieuHanh.create(requestData);
        } else if (this.isEditing) {
          console.log(requestData);
          result = await diemNhiemVuDieuHanh.edit(requestData);
        }

        if (!!result && this.editedIndex > -1) {
          Object.assign(this.listDiemNhiemVu[this.editedIndex], result);

          //Thong bao
          this.toggleSnackbar({
            type: "success",
            message: "Thêm điểm nhiệm vụ điều hành thành công",
            state: true,
            timeout: 2000,
          });

          //add Feature Source
          // console.log(result);
          // editLayerHelper.addFeatureToSource(this.selectedLayer, result);
        }
      } catch (error) {
        console.log(error);
      }
      this.close(true);
      this.stop();

      this.onMapBound();

      //remove layer edit
      // this.olEditCtrl.removeLayerEdit();
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

      return listNV.filter((nv) => nv.value === nvdh)[0].text;
    },
  },
  watch: {
    listDiemNhiemVu() {},
  },
};
</script>

<style>
.theme--light.v-data-table.v-data-table--fixed-header thead th {
  background: rgb(160, 159, 159) !important;
}
</style>
