<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-radio-group v-model="selectionNVBP">
          <v-data-table
            :headers="headers"
            :items="listNVBP"
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
                </div>
              </v-toolbar>
            </template>
            <template v-slot:[`item.selection`]="{ item }">
              <v-radio
                @change="handlerSelectionNVBP(item)"
                :value="item.maNhanDang"
              ></v-radio>
            </template>
            <template v-slot:[`item.actions`]="{ item }">
              <div>
                <v-icon @click="zoomToPoint(item)" color="red" class="mr-3">
                  mdi-map-marker-outline
                </v-icon>
                <v-icon color="green" class="mr-3">
                  mdi-vector-polyline
                </v-icon>
                <v-icon color="orange"> mdi-shape-polygon-plus </v-icon>
              </div>
            </template>

            <template v-slot:[`item.trangThaiNVBP`]="{ item }">
              <span>{{ item.trangThaiNVBP | convertStatus(listStatus) }}</span>
            </template>
            <template v-slot:[`item.maDV`]="{ item }">
              <span>{{ item.maDV | convertDV(listDV) }}</span>
            </template>
            <template v-slot:[`item.maNVDH`]="{ item }">
              <span>{{ item.maNVDH | convertNVDH(listNVDH) }}</span>
            </template>

            <template v-slot:[`body.append`]>
              <span></span>
            </template>
          </v-data-table>
        </v-radio-group>
      </v-col>
    </v-row>
    <v-row>
      <MapComponent heightMap="calc(50vh - 65px)" />
    </v-row>
  </v-container>
</template>

<script>
import OlEditController from "@/controllers/OlEdtiController";

import MapComponent from "@/components/ol/MapComponent.vue";
import { EventBus } from "@/EventBus";
import { getAllChildLayers } from "@/utils/Layer";
import { mapGetters, mapMutations } from "vuex";
import editLayerHelper from "@/controllers/OlEditLayerHelper";
import { InteractionsToggle } from "@/mixins/InteractionsToggle";
import { Mapable } from "@/mixins/Mapable";
import { KeyShortcuts } from "@/mixins/KeyShortcuts";

import Vue from "vue";

import vungNVDH from "@/api/vung-nhiem-vu-dieu-hanh";
import tuyenNVDH from "@/api/tuyen-nhiem-vu-dieu-hanh";
import diemNVDH from "@/api/diem-nhiem-vu-dieu-hanh";
import nhiemVuDieuHanh from "@/api/nhiem-vu-dieu-hanh";
import nhiemVuBoPhan from "@/api/nhiem-vu-bo-phan";
import donVi from "@/api/don-vi";

export default {
  mixins: [InteractionsToggle, Mapable, KeyShortcuts],
  components: {
    MapComponent,
  },
  data() {
    return {
      interactionType: "edit-interaction",
      layerName: "geo_nhiemVuBoPhan",
      selectedLayer: null,

      search: "",
      menu2: false,

      isLoading: false,

      headers: this.$appConfig.nhiemVuBoPhan.headers,
      nameRules: [(v) => !!v || "Name is required"],

      listStatus: [],
      listNVDH: [],
      listNVBP: [],

      listDiemNVDH: [],
      listTuyenNVDH: [],
      listVungNVDH: [],

      listDV: [],

      VTDHSelected: null,
      TDHSelected: null,
      VDHSelected: null,

      selectionNVBP: "",
    };
  },
  created() {
    this.initData().then(() => {
      // Vue.prototype.$NVBPSelected = "";
      this.selectionNVBP = this.$NVBPSelected || "";
      this.onMapBound();
    });
  },
  mounted() {},

  methods: {
    ...mapMutations("map", {
      toggleSnackbar: "TOGGLE_SNACKBAR",
    }),

    async initData() {
      try {
        this.isLoading = true;

        const [
          resultNVDH,
          resultNVBP,
          resultStatus,
          listDiemNVDH,
          listTuyenNVDH,
          listVungNVDH,
          listDonVi,
        ] = await Promise.all([
          nhiemVuDieuHanh.getAll({}),
          nhiemVuBoPhan.getAll({}),
          nhiemVuBoPhan.getTrangThaiBPNV({}),
          diemNVDH.getAll({}),
          tuyenNVDH.getAll({}),
          vungNVDH.getAll({}),
          donVi.getAll({}),
        ]);

        this.listNVDH = resultNVDH;
        this.listNVBP = resultNVBP.filter(
          (item) => item.maDV === this.$user.maDV
        );
        this.listStatus = resultStatus;
        this.listDV = listDonVi;

        this.listDiemNVDH = listDiemNVDH.features;
        this.listTuyenNVDH = listTuyenNVDH.features;
        this.listVungNVDH = listVungNVDH.features;

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
    },
    handlerSelectionNVBP(item) {
      this.VTDHSelected = this.listDiemNVDH.filter(
        (diemNVDH) => item.maNVDH === diemNVDH.properties.nvdh
      );

      this.TDHSelected = this.listTuyenNVDH.filter(
        (tuyenNVDH) => item.maNVDH === tuyenNVDH.properties.nvdh
      );

      this.VDHSelected = this.listVungNVDH.filter(
        (vungNVDH) => item.maNVDH === vungNVDH.properties.nvdh
      );

      editLayerHelper.addFeaturesToSource2(this.selectedLayer, [
        { features: this.VTDHSelected, style: "nvdh" },
        { features: this.TDHSelected, style: "nvdh" },
        { features: this.VDHSelected, style: "nvdh" },
      ]);

      let layerExtent = this.selectedLayer.getSource().getExtent();
      const fitOptions = { duration: 1000 };

      this.$map.getView().fit(layerExtent, fitOptions);

      Vue.prototype.$NVBPSelected = item.maNhanDang;
      Vue.prototype.$NVDHSelected = item.maNVDH;
    },

    zoomToPoint(item) {
      if (this.paVTSelected === null) {
        this.toggleSnackbar({
          type: "error",
          message: "Chọn nhiệm vụ bộ phận",
          state: true,
          timeout: 2000,
        });
      } else {
        // const view = this.$map.getView();
        // editLayerHelper.zoomToPoint(view, this.paVTSelected[0], 18);
      }
    },
  },
  computed: {},
  filters: {
    convertNVDH: (nvdh, listNV) => {
      if (!nvdh) return "";
      return listNV.find((nv) => nv.maNhanDang === nvdh).tenNVDH;
    },
    convertStatus: (maStatus, listStatus) => {
      if (!maStatus) return "";

      return listStatus.filter((stt) => stt.value === maStatus)[0].text;
    },
    convertDV: (maDV, listDV) => {
      if (!maDV) return "";
      return listDV.find((dv) => dv.maNhanDang === maDV).tenDonVi;
    },
  },
};
</script>

<style>
.theme--light.v-data-table.v-data-table--fixed-header thead th {
  background: rgb(160, 159, 159) !important;
}
</style>
