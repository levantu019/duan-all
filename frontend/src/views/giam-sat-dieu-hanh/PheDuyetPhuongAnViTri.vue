<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-data-table
          :headers="headers"
          :items="listPheDuyetPAViTri"
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

          <template v-slot:[`item.nguoiCMPAVT`]="{ item }">
            <v-text-field
              v-model="editedItem.nguoiCMPAVT"
              :hide-details="true"
              dense
              label="Người phê duyệt"
              v-if="item.id === editedItem.id"
            ></v-text-field>
            <span v-else>{{ item.nguoiCMPAVT }}</span>
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
          <template v-slot:[`item.maNVDH`]="{ item }">
            <v-select
              :items="listNVDH"
              v-model="editedItem.maNVDH"
              label="Nhiệm vụ"
              v-if="item.id === editedItem.id"
              dense
              :hide-details="true"
              required
              :rules="nameRules"
              item-text="tenNVDH"
              item-value="maNVDH"
              @change="listNVDHChange"
            ></v-select>
            <span v-else>{{ item.maNVDH | convertNVDH(listNVDH) }}</span>
          </template>
          <template v-slot:[`item.paVitri`]="{ item }">
            <v-select
              :items="listPAViTriForSelect"
              v-model="editedItem.paViTri"
              label="Nhiệm vụ"
              v-if="item.id === editedItem.id"
              dense
              :hide-details="true"
              required
              :rules="nameRules"
              item-text="properties.tenPAVT"
              item-value="id"
              @change="paViTriChange"
            ></v-select>
            <span v-else>{{ item.paVitri | convertPAVT(listPAViTri) }}</span>
          </template>

          <template v-slot:[`item.maDV`]="{ item }">
            <span label="Nhiệm vụ" v-if="item.id === editedItem.id">{{
              editedItem.maDV | convertDV(listDV)
            }}</span>
            <span v-else>{{ item.maDV | convertDV(listDV) }}</span>
          </template>

          <template v-slot:[`item.trangThaiCMPAVT`]="{ item }">
            <v-select
              :items="listStatus"
              v-model="editedItem.trangThaiCMPAVT"
              label="Trạng thái nhiệm vụ"
              v-if="item.id === editedItem.id"
              dense
              :hide-details="true"
              required
              :rules="nameRules"
            ></v-select>
            <span v-else>{{
              item.trangThaiCMPAVT | convertStatus(listStatus)
            }}</span>
          </template>

          <template v-slot:[`item.moTaCMPAVT`]="{ item }">
            <v-text-field
              v-model="editedItem.moTaCMPAVT"
              :hide-details="true"
              dense
              single-line
              v-if="item.id === editedItem.id"
              required
              :rules="nameRules"
            ></v-text-field>
            <span v-else>{{ item.moTaCMPAVT }}</span>
          </template>
          <template v-slot:[`item.ngayCMPAVT`]="{ item }">
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
                  v-model="editedItem.ngayCMPAVT"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                v-model="editedItem.ngayCMPAVT"
                @input="menu2 = false"
                no-title
              ></v-date-picker>
            </v-menu>

            <span v-else>{{ item.ngayCMPAVT }}</span>
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
import OlEditController from "@/controllers/OlEdtiController";
import pheDuyetPhuongAnViTri from "@/api/phe-duyet-phuong-an-vi-tri";
import phuongAnViTri from "@/api/phuong-an-vi-tri";
import MapComponent from "@/components/ol/MapComponent.vue";
import { EventBus } from "@/EventBus";
import { getAllChildLayers } from "@/utils/Layer";
import { mapGetters, mapMutations } from "vuex";
import editLayerHelper from "@/controllers/OlEditLayerHelper";
import { InteractionsToggle } from "@/mixins/InteractionsToggle";
import { Mapable } from "@/mixins/Mapable";
import { KeyShortcuts } from "@/mixins/KeyShortcuts";
import nhiemVuDieuHanh from "@/api/nhiem-vu-dieu-hanh";
import nhiemVuBoPhan from "@/api/nhiem-vu-bo-phan";
import donViApi from "@/api/don-vi";
import diemNhiemVuDieuHanh from "@/api/diem-nhiem-vu-dieu-hanh";
import OlStyleDefs from "@/style/OlStyleDefs";

export default {
  mixins: [InteractionsToggle, Mapable, KeyShortcuts],
  components: {
    MapComponent,
  },
  data() {
    return {
      interactionType: "edit-interaction",
      layerName: "geo_pheDuyetPhuongAn",
      selectedLayer: null,

      dataObject: {},
      search: "",
      geotype: "",
      menu2: false,

      isLoading: false,
      isAdding: false,
      isEditing: false,
      hasFeedback: false,

      headers: this.$appConfig.pheDuyetPhuongAnViTri.headers,
      nameRules: [(v) => !!v || "Name is required"],

      listPheDuyetPAViTri: [],
      listPAViTri: [],
      listStatus: [],
      listNVDH: [],
      listNVBP: [],
      listDV: [],
      listDiemNVDH: [],

      listPAViTriForSelect: [],

      editedIndex: -1,
      editedItem: this.$appConfig.pheDuyetPhuongAnViTri.defaultItem,
      defaultItem: this.$appConfig.pheDuyetPhuongAnViTri.defaultItem,
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

        const resultPAViTri = await phuongAnViTri.getAll({});
        const resultDV = await donViApi.getAll({});
        const resultNVDH = await nhiemVuDieuHanh.getAll({});
        const resultStatus = await pheDuyetPhuongAnViTri.getStatus({});
        const resultNVBP = await nhiemVuBoPhan.getAll({});
        const resultDiemNVDH = await diemNhiemVuDieuHanh.getAll({});

        this.listStatus = resultStatus;
        this.listPAViTri = resultPAViTri.results.features;
        this.listNVDH = resultNVDH.results;
        this.listDV = resultDV.results.features;
        this.listNVBP = resultNVBP.results;
        this.listDiemNVDH = resultDiemNVDH.results.features;

        let resultPheDuyetPAVitri;
        await pheDuyetPhuongAnViTri.getAll({}).then((response) => {
          resultPheDuyetPAVitri = response.results.features.map((item) => {
            return {
              ...item.properties,
              ...this.getInfo(this.listPAViTri, this.listNVBP, item),
              id: item.id,
              geometry: item.geometry,
            };
          });
        });

        this.listPheDuyetPAViTri = resultPheDuyetPAVitri;

        this.isLoading = false;
      } catch (error) {
        console.log(error);
      }
    },

    getInfo(PAVT, NVBP, item) {
      let PAItem = PAVT.filter((pa) => pa.id === item.properties.paViTri)[0];

      let NVBPItem = NVBP.filter((nv) => {
        return nv.maNVBP === PAItem.properties.nvbp;
      })[0];

      return {
        paVitri: PAItem.id,
        maNVDH: NVBPItem.maNVDH,
        maDV: NVBPItem.maDV,
      };
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

      //load Điểm nhiệm vụ điều hành
      const styleDiemNVDH = OlStyleDefs.getDieuHanhStyle();
      const stylePAViTri = OlStyleDefs.getPAViTriStyle();
      const stylePDPAViTri = OlStyleDefs.getPDPAViTriStyle();

      editLayerHelper.addFeaturesToSource2(this.selectedLayer, [
        { features: this.listDiemNVDH, style: styleDiemNVDH },
        { features: this.listPAViTri, style: stylePAViTri },
        { features: this.listPheDuyetPAViTri, style: stylePDPAViTri },
      ]);

      // //load PA Vi tri
      // editLayerHelper.addFeaturesToSource(
      //   this.selectedLayer,
      //   this.listPAViTri,
      //   styleDiemNVDH
      // );
    },

    editItem(item) {
      this.isEditing = true;

      this.editedIndex = this.listPheDuyetPAViTri.indexOf(item);

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
      const index = this.listPheDuyetPAViTri.indexOf(item);
      if (confirm("Are you sure you want to delete this item?")) {
        await pheDuyetPhuongAnViTri.delete(item);
        this.listPheDuyetPAViTri.splice(index, 1);
      }

      //   //remove Feature
      //   editLayerHelper.removeFeatureFromSource(this.selectedLayer, item);
      // }
    },

    close(isSaved) {
      this.editedItem = Object.assign({}, this.defaultItem);
      this.editedIndex = -1;

      this.isAdding && !isSaved && this.listPheDuyetPAViTri.shift();

      this.stop();

      this.isAdding = false;
      this.isEditing = false;
    },
    addNewPosition() {
      const me = this;
      this.isAdding = true;

      this.hasFeedback = confirm("Bạn có muốn thêm điểm không?");

      if (!this.hasFeedback) {
        this.addNewMission();
        return;
      }

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

      this.listPheDuyetPAViTri.unshift(addObj);

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
        ...this.editedItem,
        id: this.editedItem.id,
        geoCMPAVT: !!this.geometry
          ? `SRID=4326;POINT(${this.geometry.flatCoordinates[0]} ${this.geometry.flatCoordinates[1]})`
          : null,
      };

      const { moTaCMPAVT, trangThaiCMPAVT, paViTri } = requestData;

      if (
        moTaCMPAVT.length === 0 ||
        trangThaiCMPAVT === null ||
        paViTri === null
      ) {
        //Thong Bao
        return;
      }

      try {
        let result;
        if (this.isAdding) {
          result = await pheDuyetPhuongAnViTri.create(requestData);
        } else if (this.isEditing) {
          result = await pheDuyetPhuongAnViTri.edit(requestData);
        }

        if (!!result && this.editedIndex > -1) {
          const convertData = this.getInfo(
            this.listPAViTri,
            this.listNVBP,
            result
          );

          console.log(result, convertData);

          result = {
            id: result.id,
            ...result.properties,
            ...convertData,
            geometry: result.geometry,
          };

          Object.assign(this.listPheDuyetPAViTri[this.editedIndex], result);
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
    listNVDHChange(item) {
      this.listPAViTriForSelect = [];
      const filterNVBP = this.listNVBP.filter((nvbp) => {
        return nvbp.maNVDH === item;
      });

      filterNVBP.forEach((nvbp) => {
        this.listPAViTri.forEach((pavt) => {
          if (pavt.properties.nvbp === nvbp.maNVBP) {
            this.listPAViTriForSelect.push(pavt);
          }
        });
      });
    },
    paViTriChange(idPAVT) {
      const PAVT = this.listPAViTri.filter((item) => item.id === idPAVT)[0];
      const filterNVBP = this.listNVBP.filter((nvbp) => {
        return nvbp.maNVBP === PAVT.properties.nvbp;
      })[0];

      this.editedItem.maDV = filterNVBP.maDV;
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
      return listNV.filter((nv) => nv.maNVDH === nvdh)[0].tenNVDH;
    },
    convertPAVT: (pavt, listPAVT) => {
      if (!pavt) return "";
      return listPAVT.filter((vt) => vt.id === pavt)[0].properties.tenPAVT;
    },

    convertDV: (maDV, listDV) => {
      if (!maDV) return "";
      return listDV.filter((dv) => dv.id === maDV)[0].properties.tenDV;
    },
    convertStatus: (maStatus, listStatus) => {
      if (!maStatus) return "";

      return listStatus.filter((stt) => stt.value === maStatus)[0].text;
    },
  },
};
</script>

<style>
.theme--light.v-data-table.v-data-table--fixed-header thead th {
  background: rgb(160, 159, 159) !important;
}
</style>
