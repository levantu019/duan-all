<template>
  <v-container>
    <v-row>
      <v-col cols="9" class="pa-0 wrapper-map">
        <!-- dev tool for map -->
        <div class="toolbar-top">
          <ul class="toolbar-top-left">
            <li class="tool">
              <v-icon>mdi-menu-left</v-icon>
            </li>
            <li class="tool" style="width: 260px">
              <v-autocomplete
                :items="[]"
                dense
                hide-details
                hide-no-data
                append-icon=""
                return-object
                label="Tìm địa điểm, địa danh..."
                solo
                flat
              />
              <!-- </div> -->
              <div class="tool">
                <v-icon style="width: 40px">mdi-magnify</v-icon>
              </div>
            </li>
            <li class="tool">
              <v-icon>mdi-call-split </v-icon>
            </li>
          </ul>
          <v-spacer></v-spacer>
          <ul class="toolbar-top-right">
            <li class="tool">
              <v-icon>mdi-delete</v-icon>
            </li>

            <li class="tool">
              <v-icon>mdi-fullscreen </v-icon>
            </li>
          </ul>
        </div>
        <!--  -->
        <map-component heightMap="100%" />
        <button
          id="btshowTable"
          class="btnclick active"
          v-if="!show"
          @click="show = !show"
        >
          <i class="fa fa-angle-up"></i>
        </button>
        <v-sheet
          color="white"
          elevation="5"
          height="400"
          width="100%"
          class="view-attribute"
          v-if="show"
        >
          <v-toolbar dense outlined elevation="0">
            <v-tabs background-color="transparent" color="red">
              <v-tabs-slider color="success"></v-tabs-slider>
              <v-tab> Thông tin </v-tab>
              <v-tab>
                <v-icon left>mdi-chart-line</v-icon>
                Thông kê
              </v-tab>
            </v-tabs>
            <v-spacer></v-spacer>
            <v-icon class="mr-2">mdi-fullscreen</v-icon>
            <v-icon @click="show = !show">mdi-close</v-icon>
          </v-toolbar>
          <v-data-table
            :headers="headers"
            :items="desserts"
            :sort-by="['calories', 'fat']"
            :sort-desc="[false, true]"
            multi-sort
            class="elevation-1"
            fixed-header
            height="290"
          ></v-data-table>
        </v-sheet>
        <!-- <div class="toolbar-right">
              <ul class="toolbar-right-top">
                <li class="tool">
                  <v-icon>mdi-layers-outline </v-icon>
                </li>
              </ul>
              <ul class="toolbar-right-bottom">
                <li class="tool">
                  <v-icon>mdi-circle-outline </v-icon>
                </li>
                <li class="tool">
                  <v-icon>mdi-shape-polygon-plus </v-icon>
                </li>
                <li class="tool">
                  <v-icon>mdi-checkbox-blank-badge-outline </v-icon>
                </li>
                <li class="tool">
                  <v-icon>mdi-vector-polyline </v-icon>
                </li>
              </ul>
            </div> -->
      </v-col>
      <v-col cols="12">
        <v-data-table
          :headers="headers"
          :items="listItems"
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
                  color="white"
                  class="ml-3"
                  @click="addNewPosition()"
                  :disabled="isAdding"
                >
                  <v-icon class="mr-1" color="success">mdi-plus-circle </v-icon
                  >Thêm mới
                </v-btn>
                <v-btn color="white" class="ml-3">
                  <v-icon class="mr-1" color="primary"
                    >mdi-file-document-plus </v-icon
                  >Thêm từ file
                </v-btn>
                <v-btn color="white" class="ml-3">
                  <v-icon class="mr-1" color="red">mdi-delete</v-icon>Xóa
                </v-btn>
                <v-btn color="white" class="ml-3">
                  <v-icon class="mr-1" color="warning"
                    >mdi-table-large-plus </v-icon
                  >Thêm trường
                </v-btn>
                <v-btn color="white" class="ml-3">
                  <v-icon class="mr-1" color="warning"
                    >mdi-table-large-remove </v-icon
                  >Xóa trường
                </v-btn>
                <v-btn color="white" class="ml-3">
                  <v-icon class="mr-1" color="black">mdi-filter </v-icon>Lọc
                </v-btn>
              </div>
            </v-toolbar>
          </template>
        </v-data-table>
      </v-col>
    </v-row>
    <v-row>
      <MapComponent />
    </v-row>
    <v-dialog v-model="dialog" persistent max-width="600px">
      <v-toolbar dark color="primary">
        <v-toolbar-title>Thông tin đảo</v-toolbar-title>
      </v-toolbar>
      <v-card>
        <v-card-text>
          <v-container>
            <v-row>
              <!-- <v-col cols="4">
                <v-subheader class="text-h6">Tên đảo:</v-subheader>
              </v-col> -->
              <v-col>
                <v-text-field
                  outlined
                  placeholder="Nhập tên đảo"
                  hide-details=""
                  label="Tên đảo"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <!-- <v-col cols="4">
                <v-subheader class="text-h6">Loại đảo:</v-subheader>
              </v-col> -->
              <v-col>
                <v-combobox
                  :items="[]"
                  hide-details=""
                  placeholder="Loại đảo"
                  outlined
                  label="Loại đảo"
                ></v-combobox>
              </v-col>
            </v-row>
            <v-row>
              <!-- <v-col cols="4">
                <v-subheader class="text-h6">Mô tả đảo:</v-subheader>
              </v-col> -->
              <v-col>
                <v-textarea
                  outlined
                  hide-details=""
                  placeholder="Mô tả đảo"
                  label="Mô tả đảo"
                ></v-textarea>
              </v-col>
            </v-row>
            <v-row>
              <!-- <v-col cols="4">
                <v-subheader class="text-h6">Diện tích:</v-subheader>
              </v-col> -->
              <v-col>
                <v-text-field
                  outlined
                  placeholder="Diện tích"
                  hide-details=""
                  label="Diện tích"
                ></v-text-field>
              </v-col>
            </v-row>
            <v-row>
              <!-- <v-col cols="4">
                <v-subheader class="text-h6">Ngày Nhập:</v-subheader>
              </v-col> -->
              <v-col>
                <v-menu
                  ref="menu"
                  v-model="menu1"
                  :return-value.sync="date"
                  transition="scale-transition"
                  offset-y
                  min-width="auto"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                      v-model="date"
                      append-icon="mdi-calendar"
                      :close-on-content-click="false"
                      readonly
                      v-bind="attrs"
                      v-on="on"
                      outlined
                      hide-details=""
                      placeholder="Ngày nhập"
                    ></v-text-field>
                  </template>
                  <v-date-picker v-model="date" no-title scrollable>
                  </v-date-picker>
                </v-menu>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn width="100" depressed color="primary" @click="save">
            OK
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import OlEditController from "@/controllers/OlEdtiController";
import diemNhiemVuDieuHanh from "@/api/diem-nhiem-vu-dieu-hanh";
import MapComponent from "@/components/ol/MapComponent.vue";
import { EventBus } from "@/EventBus";
// import { getAllChildLayers } from "@/utils/Layer";
import { mapGetters, mapMutations } from "vuex";
import editLayerHelper from "@/controllers/OlEditLayerHelper";
import { InteractionsToggle } from "@/mixins/InteractionsToggle";
import { Mapable } from "@/mixins/Mapable";
import { KeyShortcuts } from "@/mixins/KeyShortcuts";
import service from "@/utils/request";

export default {
  mixins: [InteractionsToggle, Mapable, KeyShortcuts],
  components: {
    MapComponent,
  },
  data() {
    return {
      interactionType: "edit-interaction",

      selectedLayer: null,

      dialog: false,

      search: "",
      geotype: "",
      menu1: false,
      date: "",

      isLoading: false,
      isAdding: false,
      isEditing: false,

      headers:
        this.$appConfig["quanTriDuLieu"][0]["duLieuDungChung"]["lopDiaDanhDao"]
          .headers,

      nameRules: [(v) => !!v || "Name is required"],

      listItems: [],

      editedIndex: -1,
      editedItem: {},
      defaultItem: {},
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

        // const response = await service.get(
        //   "/nen-dia-ly/bien-gioi-dia-gioi/dia-phan-hanh-chinh-tren-bien/"
        // );

        console.log(response);

        // const response = fetch(
        //   "http://192.168.0.102:8000/nen-dia-ly/bien-gioi-dia-gioi/dia-phan-hanh-chinh-tren-bien/"
        // )
        //   .then((res) => res.json())
        //   .then((data) => console.log(data));

        // const listFeatures = await diemNhiemVuDieuHanh.getAll({});
        // this.listNhiemVu = await nhiemVuDieuHanh.getAll({});

        // this.listDiemNhiemVu = [...listFeatures.features];

        this.isLoading = false;
      } catch (error) {
        console.log(error);
      }
    },

    onMapBound() {
      this.olEditCtrl = new OlEditController(this.$map);

      //add Feature to Layer
      // this.selectedLayer = editableLayers[0];
      // editLayerHelper.selectedLayer = this.selectedLayer;

      // editLayerHelper.addFeaturesToSource(
      //   this.selectedLayer,
      //   this.listDiemNhiemVu
      // );
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

      this.selectedLayer = this.olEditCtrl.createEditLayer(null, null, "Point");

      editLayerHelper.selectedLayer = this.selectedLayer;

      this.isAdding = true;

      this.toggleSnackbar({
        type: "warning",
        message: "Vẽ đối tượng trên bản đồ để thêm dữ liệu không gian",
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
    addNewInfo() {
      this.stop();

      this.toggleSnackbar({
        type: "warning",
        message: "Nhập thông tin đối tượng",
        state: true,
        timeout: 2000,
      });

      //show popup input info
      this.dialog = true;
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
        .transform("EPSG:3857", "EPSG:4756");

      this.setGeometry(featureGeometry);

      me.stop();

      me.addNewInfo();
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
    stop() {
      this.olEditCtrl.clear();
      EventBus.$emit("ol-interaction-stopped", this.interactionType);
    },

    async save() {
      // const requestData = {
      //   ...this.editedItem.properties,
      //   id: this.editedItem.id,
      //   geoDiem: `SRID=4756;POINT(${this.geometry.flatCoordinates[0]} ${this.geometry.flatCoordinates[1]})`,
      // };

      // const { tenDiem, ngayDiem } = requestData;

      // if (tenDiem.length === 0 || ngayDiem.length === 0) {
      //   //Thong Bao
      //   return;
      // }
      // try {
      //   let result;
      //   if (this.isAdding) {
      //     result = await diemNhiemVuDieuHanh.create(requestData);
      //   } else if (this.isEditing) {
      //     result = await diemNhiemVuDieuHanh.edit(requestData);
      //   }

      //   if (!!result && this.editedIndex > -1) {
      //     Object.assign(this.listDiemNhiemVu[this.editedIndex], result);

      //     //Thong bao
      //     this.toggleSnackbar({
      //       type: "success",
      //       message: "Thêm điểm nhiệm vụ điều hành thành công",
      //       state: true,
      //       timeout: 2000,
      //     });

      //     //remove Layer Draw
      //     this.$map.removeLayer(this.selectedLayer);
      //   }
      // } catch (error) {
      //   console.log(error);
      // }
      this.close(true);
      this.stop();

      this.dialog = false;

      this.$map.removeLayer(this.selectedLayer);

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
