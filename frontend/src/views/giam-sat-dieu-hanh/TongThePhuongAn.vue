<template>
  <v-container>
    <v-row v-show="selectionNVBP === ''">
      <v-col cols="12">
        <v-data-table
          :headers="headers"
          :items="listNVBP"
          :search="search"
          class="elevation-1"
          height="calc(100vh - 260px)"
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
          <template v-slot:[`item.maNVDH`]="{ item }">
            <span>{{ item.maNVDH | convertNVDH(listNVDH) }}</span>
          </template>
          <template v-slot:[`item.maDV`]="{ item }">
            <span>{{ item.maDV | convertDV(listDV) }}</span>
          </template>
          <template v-slot:[`item.view`]="{ item }">
            <v-icon @click="viewPA(item)"> mdi-account-tie-voice </v-icon>
          </template>
          <template v-slot:[`item.trangThaiNVBP`]="{ item }">
            <span>{{ item.trangThaiNVBP | convertStatus(listStatus) }}</span>
          </template>
          <template v-slot:[`body.append`]>
            <span></span>
          </template>
        </v-data-table>
      </v-col>
    </v-row>
    <v-row v-show="selectionNVBP !== ''">
      <v-toolbar dense outlined>
        <v-toolbar-title>Tổng thể phương án</v-toolbar-title>

        <v-spacer></v-spacer>

        <v-btn icon @click="closeMap">
          <v-icon color="red">mdi-close</v-icon>
        </v-btn></v-toolbar
      >
      <MapComponent heightMap="calc(100vh - 190px)" />
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

import OlStyleDefs from "@/style/OlStyleDefs";

import vungNVDH from "@/api/vung-nhiem-vu-dieu-hanh";
import tuyenNVDH from "@/api/tuyen-nhiem-vu-dieu-hanh";
import diemNVDH from "@/api/diem-nhiem-vu-dieu-hanh";
import donVi from "@/api/don-vi";

import nhiemVuDieuHanh from "@/api/nhiem-vu-dieu-hanh";
import nhiemVuBoPhan from "@/api/nhiem-vu-bo-phan";

import phuongAnViTri from "@/api/phuong-an-vi-tri";
import phuongAnTuyen from "@/api/phuong-an-tuyen";
import phuongAnVung from "@/api/phuong-an-vung";

export default {
  mixins: [InteractionsToggle, Mapable, KeyShortcuts],
  components: {
    MapComponent,
  },
  data() {
    return {
      interactionType: "edit-interaction",
      layerName: "geo_TongThePhuongAn",
      selectedLayer: null,

      search: "",
      menu2: false,

      isLoading: false,

      headers: this.$appConfig.tongThePhuongAn.headers,
      nameRules: [(v) => !!v || "Name is required"],

      listStatus: [],
      listNVDH: [],
      listNVBP: [],
      listDV: [],

      listDiemNVDH: [],
      listTuyenNVDH: [],
      listVungNVDH: [],

      listPAViTri: [],
      listPATuyen: [],
      listPAVung: [],

      paVTSelected: null,
      paTuyenSelected: null,
      paVungSelected: null,

      selectionNVBP: "",

      currenItem: null,
    };
  },
  created() {
    this.initData().then(() => {
      this.onMapBound();
    });
  },
  mounted() {},

  sockets: {
    updateMap: function (data) {
      this.initData().then(() => {
        this.onMapBound();
        this.viewPA(this.currenItem);
      });
    },
  },

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
          listPAViTri,
          listPATuyen,
          listPAVung,
        ] = await Promise.all([
          nhiemVuDieuHanh.getAll({}),
          nhiemVuBoPhan.getAll({}),
          nhiemVuBoPhan.getTrangThaiBPNV({}),
          diemNVDH.getAll({}),
          tuyenNVDH.getAll({}),
          vungNVDH.getAll({}),
          donVi.getAll({}),
          phuongAnViTri.getAll({}),
          phuongAnTuyen.getAll({}),
          phuongAnVung.getAll({}),
        ]);

        this.listDV = listDonVi;

        this.listNVDH = resultNVDH;
        this.listNVBP = resultNVBP;
        this.listStatus = resultStatus;

        this.listDiemNVDH = listDiemNVDH.features;
        this.listTuyenNVDH = listTuyenNVDH.features;
        this.listVungNVDH = listVungNVDH.features;

        this.listPAViTri = listPAViTri.features;
        this.listPATuyen = listPATuyen.features;
        this.listPAVung = listPAVung.features;

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
    viewPA(item) {
      this.selectionNVBP = item.maNhanDang;
      this.currenItem = item;

      //get MaNVDH  =
      const maNVDH = item.maNVDH;
      //get maNVBP
      const maNVBP = item.maNhanDang;

      //get list DiemNVDH = maNVDH
      const listDiemNVDHSelected = this.listDiemNVDH.filter(
        (item) => item.properties.nvdh === maNVDH
      );
      //get list TuyenNVDH = maNVDH
      const listTuyenNVDHSelected = this.listTuyenNVDH.filter(
        (item) => item.properties.nvdh === maNVDH
      );
      //get list Vung NVDH = maNVDH
      const listVungNVDH = this.listVungNVDH.filter(
        (item) => item.properties.nvdh === maNVDH
      );

      const listPAViTriSelected = this.listPAViTri.filter(
        (item) => item.properties.nvbp === maNVBP
      );

      const listPATuyenSelected = this.listPATuyen.filter(
        (item) => item.properties.nvbp === maNVBP
      );

      const listPAVungSelected = this.listPAVung.filter(
        (item) => item.properties.nvbp === maNVBP
      );

      editLayerHelper.addFeaturesToSource2(this.selectedLayer, [
        { features: listDiemNVDHSelected, style: "nvdh" },
        { features: listTuyenNVDHSelected, style: "nvdh" },
        { features: listVungNVDH, style: "nvdh" },
        { features: listPAViTriSelected, style: "pa" },
        { features: listPATuyenSelected, style: "pa" },
        { features: listPAVungSelected, style: "pa" },
      ]);

      setTimeout(() => {
        this.$map.updateSize();
      }, 100);
    },
    closeMap() {
      this.selectionNVBP = "";
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
