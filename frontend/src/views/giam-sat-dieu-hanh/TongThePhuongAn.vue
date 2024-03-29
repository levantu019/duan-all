<template>
  <v-container>
    <v-row v-show="selectionNVDH === ''">
      <v-col cols="12">
        <v-data-table
          :headers="headers"
          :items="listNVDH"
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
          <template v-slot:[`item.tenNVDH`]="{ item }">
            <span>{{ item.tenNVDH }}</span>
          </template>
          <template v-slot:[`item.moTaNV`]="{ item }">
            <span>{{ item.moTaNV }}</span>
          </template>
          <template v-slot:[`item.chihuyNVDH`]="{ item }">
            <span>{{ item.chihuyNVDH }}</span>
          </template>
          <template v-slot:[`item.actions`]="{ item }">
            <v-icon @click="viewPA(item)"> mdi-account-tie-voice </v-icon>
          </template>
          <template v-slot:[`item.ngayBDNVDH`]="{ item }">
            <span>{{ item.ngayBDNVDH }}</span>
          </template>
          <template v-slot:[`item.ngayKTNVDH`]="{ item }">
            <span>{{ item.ngayKTNVDH }}</span>
          </template>
          <template v-slot:[`item.vanbanNVDH`]="{ item }">
            <v-btn icon color="red">
              <v-icon>mdi-file-pdf-box</v-icon> {{ item[0] }}
            </v-btn>
          </template>
          <template v-slot:[`item.kieuNVDH`]="{ item }">
            <span>{{ item.kieuNVDH | convertKieuNV(listKieuNhiemVu) }}</span>
          </template>
          <template v-slot:[`item.trang_thai`]="{ item }">
            <v-text-field
              :hide-details="true"
              dense
              single-line
              v-if="item.maNhanDang === editedItem.maNhanDang"
            ></v-text-field>
            <span v-else>{{ item.trang_thai }}</span>
          </template>
          <template v-slot:no-data>
            <v-btn color="primary" @click="initialize">Reset</v-btn>
          </template>
          <template v-slot:[`body.append`]>
            <span></span>
          </template>
        </v-data-table>
      </v-col>
    </v-row>
    <v-row v-show="selectionNVDH !== ''">
      <v-toolbar dense outlined>
        <v-toolbar-title>Tổng thể phương án</v-toolbar-title>

        <v-spacer></v-spacer>
        <v-btn icon @click="moPhong">
          <v-icon color="red">mdi-play</v-icon>
        </v-btn>

        <v-btn icon @click="closeMap">
          <v-icon color="red">mdi-close</v-icon>
        </v-btn>
      </v-toolbar>
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

import vungNVDH from "@/api/vung-nhiem-vu-dieu-hanh";
import tuyenNVDH from "@/api/tuyen-nhiem-vu-dieu-hanh";
import diemNVDH from "@/api/diem-nhiem-vu-dieu-hanh";
import donVi from "@/api/don-vi";

import nhiemVuDieuHanh from "@/api/nhiem-vu-dieu-hanh";
import nhiemVuBoPhan from "@/api/nhiem-vu-bo-phan";

import phuongAnViTri from "@/api/phuong-an-vi-tri";
import phuongAnTuyen from "@/api/phuong-an-tuyen";
import phuongAnVung from "@/api/phuong-an-vung";
import kieuNhiemVu from "@/api/kieu-nhiem-vu";

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

      headers: this.$appConfig.nhiemVuDieuHanh.headers,
      nameRules: [(v) => !!v || "Name is required"],

      listStatus: [],
      listNVDH: [],
      listNVBP: [],
      listDV: [],

      listDiemNVDH: [],
      listTuyenNVDH: [],
      listVungNVDH: [],

      listKieuNhiemVu: [],

      listPAViTri: [],
      listPATuyen: [],
      listPAVung: [],

      paVTSelected: null,
      paTuyenSelected: null,
      paVungSelected: null,

      selectionNVDH: "",

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
          kieuNV,
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
          kieuNhiemVu.getAll({}),
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

        console.log(kieuNV);

        this.listKieuNhiemVu = kieuNV;

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
      // console.log(item, this.listNVBP);

      let listNVBP = [];
      this.listNVBP.forEach((nvbp) => {
        if (item.maNhanDang === nvbp.maNVDH) {
          listNVBP.push(nvbp.maNhanDang);
        }
      });

      this.selectionNVDH = item.maNhanDang;
      this.currenItem = item;

      //get MaNVDH  =
      const maNVDH = item.maNhanDang;
      //get maNVBP
      // const maNVBP = item.maNhanDang;

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

      // let listPAViTriSelected, listPATuyenSelected, listPAVungSelected;

      // listPAViTriSelected = this.listPAViTri.forEach(
      //   (item) => {
      //     console.log(item);
      //   }
      //   // item.properties.nvbp === maNVBP
      // );

      const listPAViTriSelected = this.listPAViTri.filter((item) => {
        return listNVBP.includes(item.properties.nvbp);
      });

      const listPATuyenSelected = this.listPATuyen.filter((item) => {
        return listNVBP.includes(item.properties.nvbp);
      });

      const listPAVungSelected = this.listPAVung.filter((item) => {
        return listNVBP.includes(item.properties.nvbp);
      });

      // const listPAVungSelected = this.listPAVung.filter(
      //   (item) => item.properties.nvbp === maNVBP
      // );

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
    moPhong() {
      for (let i = 0; i < this.listPATuyen.length; i++) {
        editLayerHelper.startSimulation(this.$map, this.listPATuyen[i]);
      }
    },
    closeMap() {
      this.selectionNVDH = "";
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
    convertKieuNV(nv, listKieuNV) {
      if (!nv) return "";
      return listKieuNV.filter((kieuNV) => kieuNV.value === nv)[0].text;
    },
  },
};
</script>

<style>
.theme--light.v-data-table.v-data-table--fixed-header thead th {
  background: rgb(160, 159, 159) !important;
}
</style>
