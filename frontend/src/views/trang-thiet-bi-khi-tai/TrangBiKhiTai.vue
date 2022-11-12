<template>
  <div>
    <header-component title="Trang thiết bị khí tài" />
    <nav-component-khi-tai @selectDV="selectDVHandler" />
    <v-main style="padding-bottom: 0px">
      <v-container fluid>
        <v-row>
          <v-col cols="12">
            <v-data-table
              :headers="headers"
              :items="data.listTB"
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
                <!-- <v-toolbar flat color="white"> -->
                <div class="d-flex">
                  <v-row>
                    <v-col cols="2.4">
                      <v-combobox
                        v-model="select"
                        :items="[]"
                        label="Chọn đơn vị"
                        outlined
                        dense
                      ></v-combobox>
                    </v-col>
                    <v-col cols="2.4">
                      <v-combobox
                        v-model="select"
                        :items="[]"
                        label="Loại trang bị"
                        outlined
                        dense
                      ></v-combobox>
                    </v-col>
                    <v-col cols="2.4">
                      <v-combobox
                        v-model="select"
                        :items="[]"
                        label="Xuất xứ"
                        outlined
                        dense
                      ></v-combobox>
                    </v-col>
                    <v-col cols="2.4">
                      <v-combobox
                        v-model="select"
                        :items="[]"
                        label="Tình trạng"
                        outlined
                        dense
                      ></v-combobox>
                    </v-col>
                    <v-col cols="2.4">
                      <v-text-field
                        label="Tên Trang bị"
                        outlined
                        dense
                      ></v-text-field>
                    </v-col>
                  </v-row>
                </div>
                <!-- </v-toolbar> -->
              </template>
              <template v-slot:[`item.action`]="{ item }">
                <v-btn
                  @click="handlerViewDetails(item)"
                  color="primary"
                  x-small
                  fab
                >
                  <v-icon>mdi-eye-outline </v-icon>
                </v-btn>
              </template>

              <template v-slot:[`body.append`]>
                <span></span>
              </template>
            </v-data-table>
          </v-col>
        </v-row>
        <v-row style="position: relative">
          <div
            style="position: absolute; top: 10px; left: 10px; z-index: 99"
            class="d-flex align-center"
          >
            <v-text-field
              label="Tên đơn vị hoặc khí tài"
              outlined
              dense
              solo
              hide-details=""
            ></v-text-field>
            <v-btn color="primary" class="ml-2" @click="timDonVi"
              >Tìm đơn vị</v-btn
            >
            <v-btn color="primary" class="ml-2" @click="timTrangBi"
              >Tìm trạng bị</v-btn
            >
          </div>
          <div
            style="position: absolute; bottom: 80px; right: 10px; z-index: 99"
            class="d-flex flex-column align-center"
          >
            <v-btn class="my-1" fab small color="warning">
              <v-icon dark>mdi-information-variant </v-icon>
            </v-btn>
            <v-btn
              class="my-1"
              fab
              small
              color="success"
              @click="drawer = !drawer"
            >
              <v-icon dark>mdi-layers-triple-outline </v-icon>
            </v-btn>
            <v-btn class="my-1" fab small color="primary">
              <v-icon dark>mdi-fullscreen </v-icon>
            </v-btn>
          </div>
          <v-navigation-drawer
            v-if="drawer"
            absolute
            permanent
            right
            style="right: 35px"
          >
            <template v-slot:prepend>
              <v-list-item>
                <v-list-item-content>
                  <v-list-item-title>Chọn Lớp chuyên đề</v-list-item-title>
                </v-list-item-content>
              </v-list-item>
            </template>

            <v-divider></v-divider>

            <v-list dense>
              <v-list-item v-for="(layer, index) in layers" :key="index">
                <v-list-item-icon>
                  <v-icon>mdi-layers-triple-outline</v-icon>
                </v-list-item-icon>

                <v-list-item-content>
                  <div
                    style="
                      display: flex;
                      align-items: center;
                      justify-content: space-between;
                    "
                  >
                    <p>{{ layer.title }}</p>
                    <v-checkbox style="margin-top: 0px"></v-checkbox>
                  </div>
                </v-list-item-content>
              </v-list-item>
            </v-list>
          </v-navigation-drawer>
          <div
            style="position: absolute; bottom: 10px; right: 170px; z-index: 99"
            class="d-flex align-center"
            v-if="showBaseMap"
          >
            <v-sheet
              color="white"
              elevation="2"
              height="100"
              rounded
              width="100"
              style="margin-right: 10px"
            >
              <v-img
                src="https://image.thanhnien.vn/w1024/Uploaded/2014/Pictures20135/CongDong/180513/ve-tinh-VNREDSat-1.JPG"
              ></v-img>
              <div class="text-caption">
                <v-icon>mdi-layers-triple-outline</v-icon> Vệ tinh
              </div>
            </v-sheet>
            <v-sheet
              color="white"
              elevation="2"
              height="100"
              rounded
              width="100"
              style="margin-right: 10px"
            >
              <v-img src="/img/DiaHinh.jpg"></v-img>
              <div class="text-caption">
                <v-icon>mdi-layers-triple-outline</v-icon> Địa hình
              </div>
            </v-sheet>
            <v-sheet
              color="white"
              elevation="2"
              height="100"
              rounded
              width="100"
              style="margin-right: 10px"
            >
              <v-img height="70" src="/img/GiaoThong.jfif"></v-img>
              <div class="text-caption">
                <v-icon>mdi-layers-triple-outline</v-icon> Giao thông
              </div>
            </v-sheet>
          </div>
          <div
            style="position: absolute; bottom: 10px; right: 60px; z-index: 99"
            class="d-flex align-center"
            @click="showBaseMap = !showBaseMap"
          >
            <v-sheet
              color="white"
              elevation="2"
              height="100"
              rounded
              width="100"
            >
              <v-img
                src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQOoe-f8mE-pGv5v12vSvAfd6RFniUyGk4U5Q&usqp=CAU"
              ></v-img>
              <div class="text-caption">
                <v-icon>mdi-layers-triple-outline</v-icon> Base map
              </div>
            </v-sheet>
          </div>
          <MapComponent />
        </v-row>
      </v-container>
    </v-main>

    <v-footer app color="#4472c4">
      <h4 class="white--text">Cập nhật dữ liệu gần nhất: 5/2022</h4>
      <v-spacer></v-spacer>
      <h4 class="white--text">Phiên bản: V1.0</h4>
    </v-footer>

    <!-- Modal -->
    <v-dialog v-model="dialog" persistent full-width>
      <template v-slot:activator="{ on }">
        <v-btn color="primary" dark v-on="on">Open Dialog</v-btn>
      </template>
      <v-card>
        <v-card-title class="headline"
          >Thông tin chung về trang bị khí tài
          <v-spacer></v-spacer>
          <v-btn icon color="indigo" @click="dialog = false">
            <v-icon>mdi-close</v-icon>
          </v-btn>
        </v-card-title>
        <v-divider></v-divider>
        <v-card-text>
          <v-container grid-list-md>
            <v-layout wrap>
              <v-flex
                class="d-flex justify-space-between flex-row flex-wrap"
                xs12
                sm12
                md6
              >
                <div
                  v-for="(data, index) in dataDialogs"
                  :key="index"
                  xs6
                  sm6
                  md6
                  style="width: 400px"
                >
                  <p class="text-h6">
                    {{ data.label }}:
                    <span class="text-body-1">{{ data.value }}</span>
                  </p>
                </div>
              </v-flex>

              <v-flex xs12 sm12 md6>
                <v-carousel
                  cycle
                  height="100%"
                  hide-delimiter-background
                  show-arrows-on-hover
                >
                  <v-carousel-item v-for="(slide, i) in slides" :key="i">
                    <v-sheet :color="colors[i]" height="100%">
                      <v-row
                        class="fill-height"
                        align="center"
                        justify="center"
                      >
                        <div class="text-h2">{{ slide }} Slide</div>
                      </v-row>
                    </v-sheet>
                  </v-carousel-item>
                </v-carousel>
              </v-flex>
            </v-layout>
          </v-container>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-title class="headline"
          >Danh sách các trang thiết bị thuộc khí tài
          <v-spacer></v-spacer>
          <v-btn depressed color="primary"> Tìm đơn vị </v-btn>
          <v-btn depressed color="primary" class="ml-2"> Tìm thiết bị </v-btn>
        </v-card-title>
        <v-divider></v-divider>
        <v-card-text>
          <v-container grid-list-md>
            <v-layout wrap>
              <v-flex xs12 sm12>
                <v-data-table
                  :headers="headers"
                  :items="data.listTB"
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

                  <template v-slot:[`item.action`]="{ item }">
                    <v-btn
                      @click="handlerViewDetails(item)"
                      color="primary"
                      x-small
                      fab
                    >
                      <v-icon>mdi-eye-outline </v-icon>
                    </v-btn>
                  </template>
                  <template v-slot:[`body.append`]>
                    <span></span>
                  </template>
                </v-data-table>
              </v-flex>
            </v-layout>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn depressed color="primary"> Xuất báo cáo </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import HeaderComponent from "@/components/layouts/HeaderComponent.vue";
import NavComponentKhiTai from "@/components/layouts/NavComponentKhiTai.vue";
import MapComponent from "@/components/ol/MapComponent.vue";
import editLayerHelper from "@/controllers/OlEditLayerHelper";

import Point from "ol/geom/Point";
import Feature from "ol/Feature";
import VectorLayer from "ol/layer/Vector";
import VectorSource from "ol/source/Vector";

import OlStyle from "ol/style/Style";
import OlIcon from "ol/style/Icon";

import Overlay from "ol/Overlay";

import { transform } from "ol/proj";
import { Polygon } from "ol/geom";
import { Circle as CircleStyle, Fill, Stroke, Style } from "ol/style";

export default {
  components: {
    HeaderComponent,
    NavComponentKhiTai,
    MapComponent,
  },
  mounted() {
    const geo = {
      geometry: {
        type: "Point",
        coordinates: [105.64624125110704, 20.918214338949486],
      },
    };
    const point = new Point(geo.geometry.coordinates);

    let feature = new Feature({
      geometry: point,
    });

    feature.getGeometry().transform("EPSG:4756", "EPSG:3857");

    this.source = new VectorSource({
      features: [feature],
    });

    const me = this;

    const layer = new VectorLayer({
      source: me.source,
      style: new OlStyle({
        image: new OlIcon({
          anchor: [0.5, 46],
          anchorXUnits: "fraction",
          anchorYUnits: "pixels",
          src: "https://openlayers.org/en/latest/examples/data/icon.png",
        }),
        stroke: new Stroke({
          color: "red",
          width: 3,
        }),
      }),
    });

    this.layer = layer;

    this.$map.addLayer(layer);
  },
  data() {
    return {
      drawer: false,
      layers: [
        { title: "Layer 1" },
        { title: "Layer 2" },
        { title: "Layer 3" },
      ],
      select: "",
      source: null,
      layer: null,
      headers: [
        {
          text: "Tên trang bị",
          value: "tenTrangBi",
          sortable: false,
          align: "center",
          divider: true,
        },
        {
          text: "Số lượng",
          value: "soLuong",
          sortable: false,
          align: "center",
          divider: true,
        },
        {
          text: "Số hiệu",
          value: "soHieuTrangBi",
          sortable: false,
          align: "center",
          divider: true,
        },
        {
          text: "Xuất xứ",
          value: "xuatXu",
          sortable: false,
          align: "center",
          divider: true,
        },
        {
          text: "Năm sản xuất",
          value: "namSanXuat",
          sortable: false,
          align: "center",
          divider: true,
        },
        {
          text: "Phân cấp chất lượng",
          value: "phanCapChatLuong",
          sortable: false,
          align: "center",
          divider: true,
        },
        {
          text: "Tình trạng",
          value: "tinhTrangTrangBi",
          sortable: false,
          align: "center",
          divider: true,
        },
        {
          text: "Mô tả chức năng Trang bị",
          value: "chucNangTrangBi",
          sortable: false,
          align: "center",
          divider: true,
        },
        {
          text: "",
          value: "action",
          sortable: false,
          align: "center",
          divider: true,
        },
      ],
      isLoading: false,
      isAdding: false,
      data: {},
      dialog: false,
      dataDialogs: [
        {
          label: "Mã biên chế trang bị",
          value: "BCTB30092201",
        },
        {
          label: "Xuất xứ",
          value: "Đức",
        },
        {
          label: "Đơn vị",
          value: "TC2",
        },
        {
          label: "Năm sản xuất",
          value: "2020",
        },
        {
          label: "Tên trang bị",
          value: "Xe tăng",
        },
        {
          label: "Phân cấp chất lượng",
          value: "Cấp 5",
        },
        {
          label: "Số hiệu trang bị",
          value: "KQH201",
        },
        {
          label: "Đề nghị",
          value: "Không",
        },
        {
          label: "Loại trang bị",
          value: "Xe bộ binh",
        },
        {
          label: "Chức năng trang bị",
          value: "Chiến đấu",
        },
      ],
      colors: [
        "indigo",
        "warning",
        "pink darken-2",
        "red lighten-1",
        "deep-purple accent-4",
      ],
      slides: ["First", "Second", "Third", "Fourth", "Fifth"],
      listTinhTrang: ["Cấp 1", "Cấp 2"],
      showBaseMap: false,
    };
  },
  methods: {
    timDonVi() {
      const listGeo = [
        {
          geometry: {
            type: "Point",
            coordinates: [105.82513481401404, 21.041123763966894],
          },
        },

        {
          geometry: {
            type: "Point",
            coordinates: [105.82895426662378, 21.042886170848767],
          },
        },
        {
          geometry: {
            type: "Point",
            coordinates: [105.82839639368862, 21.04068320604874],
          },
        },
        {
          geometry: {
            type: "Point",
            coordinates: [105.8264223079027, 21.03872052075312],
          },
        },
      ];

      listGeo.forEach((geo) => {
        const point = new Point(geo.geometry.coordinates);

        let feature = new Feature({
          geometry: point,
        });

        feature.getGeometry().transform("EPSG:4756", "EPSG:3857");
        this.source.addFeature(feature);
      });

      const boundary = {
        geometry: {
          type: "Polygon",
          coordinates: [
            [
              [105.82513481401404, 21.041123763966894],
              [105.82895426662378, 21.042886170848767],
              [105.82839639368862, 21.04068320604874],
              [105.8264223079027, 21.03872052075312],
              [105.82513481401404, 21.041123763966894],
            ],
          ],
        },
      };

      let feature1 = editLayerHelper.createFeature(boundary);
      const polygon = new Polygon(boundary.geometry.coordinates);

      let feature = new Feature({
        geometry: polygon,
      });

      feature.getGeometry().transform("EPSG:4756", "EPSG:3857");
      this.source.addFeature(feature);

      const fitOptions = { duration: 1000 };
      this.$map.getView().fit(feature1.getGeometry(), fitOptions);
    },
    timTrangBi() {
      const listGeo = [
        {
          geometry: {
            type: "Point",
            coordinates: [105.82513481401404, 21.041123763966894],
          },
        },

        {
          geometry: {
            type: "Point",
            coordinates: [105.82895426662378, 21.042886170848767],
          },
        },
        {
          geometry: {
            type: "Point",
            coordinates: [105.82839639368862, 21.04068320604874],
          },
        },
        {
          geometry: {
            type: "Point",
            coordinates: [105.8264223079027, 21.03872052075312],
          },
        },
      ];

      listGeo.forEach((geo) => {
        const point = new Point(geo.geometry.coordinates);

        let feature = new Feature({
          geometry: point,
        });

        feature.getGeometry().transform("EPSG:4756", "EPSG:3857");
        this.source.addFeature(feature);
      });

      const boundary = {
        geometry: {
          type: "Polygon",
          coordinates: [
            [
              [105.82513481401404, 21.041123763966894],
              [105.82895426662378, 21.042886170848767],
              [105.82839639368862, 21.04068320604874],
              [105.8264223079027, 21.03872052075312],
              [105.82513481401404, 21.041123763966894],
            ],
          ],
        },
      };

      let feature1 = editLayerHelper.createFeature(boundary);
      const polygon = new Polygon(boundary.geometry.coordinates);

      let feature = new Feature({
        geometry: polygon,
      });

      feature.getGeometry().transform("EPSG:4756", "EPSG:3857");
      this.source.addFeature(feature);

      const fitOptions = { duration: 1000 };
      this.$map.getView().fit(feature1.getGeometry(), fitOptions);
    },
    handlerViewDetails(item) {
      this.dialog = true;
    },
    selectDVHandler(dv) {
      this.data = {
        geometry: {
          type: "Point",
          coordinates: [105.64624125110704, 20.918214338949486],
        },
        listTB: [
          {
            tenTrangBi: "AK-47",
            soLuong: 10,
            soHieuTrangBi: "KQH122",
            xuatXu: "Trung Quốc",
            namSanXuat: "2022",
            phanCapChatLuong: "Cấp 5",
            tinhTrangTrangBi: "Tốt",
            chucNangTrangBi: "Chiến đấu",
          },
          {
            tenTrangBi: "AK-47",
            soLuong: 10,
            soHieuTrangBi: "KQH122",
            xuatXu: "Trung Quốc",
            namSanXuat: "2022",
            phanCapChatLuong: "Cấp 5",
            tinhTrangTrangBi: "Tốt",
            chucNangTrangBi: "Chiến đấu",
          },
          {
            tenTrangBi: "AK-47",
            soLuong: 10,
            soHieuTrangBi: "KQH122",
            xuatXu: "Trung Quốc",
            namSanXuat: "2022",
            phanCapChatLuong: "Cấp 5",
            tinhTrangTrangBi: "Tốt",
            chucNangTrangBi: "Chiến đấu",
          },
        ],
      };
      const view = this.$map.getView();
      editLayerHelper.zoomToPoint(view, this.data, 18);

      const coordinate = transform(
        this.data.geometry.coordinates,
        "EPSG:4756",
        "EPSG:3857"
      );
      // const hdms = toStringHDMS(toLonLat(coordinate));
      // content.innerHTML = "<p>You clicked here:</p><code>" + hdms + "</code>";

      this.$overlay.setPosition(coordinate);
    },
  },
};
</script>

<style>
.theme--light.v-data-table.v-data-table--fixed-header thead th {
  background: rgb(160, 159, 159) !important;
}
</style>
