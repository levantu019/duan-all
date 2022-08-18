<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-data-table
          :headers="headers"
          :items="listTuyenNhiemVu"
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
                  @click="addNewPosition('base')"
                >
                  <v-icon dark>mdi-plus</v-icon>Thêm mới
                </v-btn>
              </div>
            </v-toolbar>
          </template>

          <!-- <template v-slot:[`item.maDiem`]="{ item }">
            <v-text-field
              v-model="editedItem.maDiem"
              :hide-details="true"
              dense
              single-line
              v-if="item.maDiem === editedItem.maDiem"
            ></v-text-field>
            <span v-else>{{ item.maDiem }}</span>
          </template> -->
          <template v-slot:[`item.tenTuyen`]="{ item }">
            <v-text-field
              v-model="editedItem.tenTuyen"
              :hide-details="true"
              dense
              single-line
              v-if="item.maTuyen === editedItem.maTuyen"
            ></v-text-field>
            <span v-else>{{ item.tenTuyen }}</span>
          </template>
          <template v-slot:[`item.actions`]="{ item }">
            <div v-if="item.maTuyen === editedItem.maTuyen">
              <v-icon color="red" class="mr-3" @click="close">
                mdi-window-close
              </v-icon>
              <v-icon color="green" @click="save"> mdi-content-save </v-icon>
            </div>
            <div v-else>
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
              v-model="editedItem.nvdh"
              label="Nhiệm vụ"
              v-if="item.maTuyen === editedItem.maTuyen"
              dense
              :hide-details="true"
              required
            ></v-select>
            <span v-else>{{ item.nvdh | convertNVDH(listNhiemVu) }} </span>
          </template>
          <template v-slot:[`item.moTaTuyen`]="{ item }">
            <v-text-field
              v-model="editedItem.moTaTuyen"
              :hide-details="true"
              dense
              single-line
              v-if="item.maTuyen === editedItem.maTuyen"
            ></v-text-field>
            <span v-else>{{ item.moTaTuyen }}</span>
          </template>
          <template v-slot:[`item.ngayTuyen`]="{ item }">
            <v-menu
              v-model="menu2"
              :close-on-content-click="false"
              transition="scale-transition"
              offset-y
              min-width="auto"
              v-if="item.maTuyen === editedItem.maTuyen"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  prepend-icon="mdi-calendar"
                  v-model="item.ngayTuyen"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                v-model="item.ngayTuyen"
                @input="menu2 = false"
                no-title
              ></v-date-picker>
            </v-menu>
            <span v-else>{{ item.ngayTuyen }}</span>
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
import nhiemVuDieuHanh from "@/api/nhiem-vu-dieu-hanh";
import OlEditController from "@/ controllers/OlEdtiController";
import MapComponent from "@/components/ol/MapComponent.vue";
import { EventBus } from "@/EventBus";
import { getAllChildLayers } from "@/utils/Layer";
import { mapMutations } from "vuex";
import editLayerHelper from "@/ controllers/OlEditLayerHelper";
import { InteractionsToggle } from "@/mixins/InteractionsToggle";
import { Mapable } from "@/mixins/Mapable";
import { KeyShortcuts } from "@/mixins/KeyShortcuts";

import tuyenNhiemVuDieuHanh from "@/api/tuyen-nhiem-vu-dieu-hanh";
export default {
  mixins: [InteractionsToggle, Mapable, KeyShortcuts],
  components: {
    MapComponent,
  },
  data() {
    return {
      interactionType: "edit-interaction",
      dataObject: {},
      search: "",
      geotype: "",
      menu2: false,

      isLoading: false,
      isAdding: false,

      headers: this.$appConfig.tuyenNhiemVuDieuHanh.headers,

      listTuyenNhiemVu: [],
      listNhiemVu: [],

      editedIndex: -1,
      editedItem: {
        maTuyen: 0,
        tenTuyen: "",
        moTaTuyen: "",
        ngayTuyen: "",
        nvdh: 0,
      },
      defaultItem: {
        maTuyen: 0,
        tenTuyen: "",
        moTaTuyen: "",
        ngayTuyen: "",
        nvdh: 0,
      },
    };
  },
  mounted() {
    // const me =this ;
    // me.popup.el = me.$ref.popup
    // me.olEditCtrl.referencePopupElement
  },
  async created() {
    try {
      this.isLoading = true;

      const [listFeatures, listNhiemVu] = await Promise.all([
        tuyenNhiemVuDieuHanh.getAll({}),
        nhiemVuDieuHanh.getAll({}),
      ]);

      this.listTuyenNhiemVu = listFeatures.results.features.map((feature) => ({
        ...feature["properties"],
        maTuyen: feature.id,
      }));

      console.log(this.listTuyenNhiemVu);

      this.listNhiemVu = listNhiemVu.results.map(({ maNVDH, tenNVDH }) => ({
        value: maNVDH,
        text: tenNVDH,
      }));

      this.isLoading = false;
    } catch (error) {
      console.log(error);
    }
  },

  methods: {
    ...mapMutations("draw", {
      setGeometry: "SET_GEOMETRY",
    }),

    onMapBound() {
      const me = this;

      //init ol edit controller
      me.olEditCtrl = new OlEditController(me.map);

      me.olEditCtrl.createEditLayer();
    },

    editItem(item) {
      this.editedIndex = this.listVungNhiemVu.indexOf(item);
      this.editedItem = Object.assign({}, item);

      console.log(this.editedItem);
    },

    deleteItem(item) {
      const index = this.listVungNhiemVu.indexOf(item);
      confirm("Are you sure you want to delete this item?") &&
        this.desserts.splice(index, 1);
    },

    close() {
      this.editedItem = Object.assign({}, this.defaultItem);
      this.editedIndex = -1;

      this.isAdding && this.listVungNhiemVu.shift();

      this.isAdding = false;
    },
    addNewPosition(value) {
      const me = this;

      this.geotype = value;

      value = "geo_" + value;

      const editableLayers = getAllChildLayers(me.map).filter(
        (layer) => layer.get("name") === value
      );

      me.selectedLayer = editableLayers[0];
      me.stop();
      editLayerHelper.selectedLayer = me.selectedLayer;

      //
      me.olEditCtrl.dataObject = me.dataObject;

      const editType = "add";

      if (editType !== undefined) {
        const startCb = this.onDrawStart;
        const endCb = this.onDrawEnd;

        me.olEditCtrl.addInteraction(editType, startCb, endCb);

        EventBus.$emit("ol-interaction-activated", me.interactionType);

        if (this.addKeyupListener) {
          this.addKeyupListener();
        }
      } else {
        me.olEditCtrl.removeInteraction();
        EventBus.$emit("ol-interaction-stopped", me.interactionType);
        me.map.getTarget().style.cursor = "";
      }
    },
    addNewMission() {
      this.isAdding = true;
      const addObj = Object.assign({}, this.defaultItem);
      addObj.maDiem = "0" + (this.listVungNhiemVu.length + 1);
      this.listVungNhiemVu.unshift(addObj);
      this.editItem(addObj);
    },

    stop() {
      const me = this;

      me.olEditCtrl.clear();

      EventBus.$emit("ol-interaction-stopped", me.interactionType);
    },

    onDrawStart() {
      this.olEditCtrl.featuresToCommit = [];
    },
    onDrawEnd(evt) {
      const feature = evt.feature;
      const featureGeometry = feature.getGeometry();
      const result = {
        geometry: featureGeometry,
        //color
        geotype: this.geotype,
      };

      this.setGeometry(result);
      this.stop();

      this.addNewMission();
    },
    save() {
      if (this.editedIndex > -1) {
        Object.assign(this.listVungNhiemVu[this.editedIndex], this.editedItem);
      }
      this.close();
    },
  },
  filters: {
    convertNVDH: (nvdh, listNV) => {
      if (!nvdh) return "";
      return listNV.filter((nv) => nv.value === nvdh)[0].text;
    },
  },
};
</script>

<style>
.theme--light.v-data-table.v-data-table--fixed-header thead th {
  background: rgb(160, 159, 159) !important;
}
</style>
