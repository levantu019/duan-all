<!-- <template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-data-table
          :headers="headers"
          :items="listPheDuyetPATuyen"
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

          <template v-slot:[`item.nguoiCMPATuyen`]="{ item }">
            <v-text-field
              v-model="editedItem.nguoiCMPATuyen"
              :hide-details="true"
              dense
              label="Người phê duyệt"
              v-if="item.id === editedItem.id"
            ></v-text-field>
            <span v-else>{{ item.nguoiCMPATuyen }}</span>
          </template>
          <template v-slot:[`item.actions`]="{ item }">
            <div v-if="item.id === editedItem.id">
              <v-icon color="red" class="mr-2" @click="close(false)">
                mdi-window-close
              </v-icon>
              <v-icon color="green" @click="save"> mdi-content-save </v-icon>
            </div>
            <div v-else>
              <v-icon color="yellow" class="mr-2" @click="zoomToLine(item)">
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
          <template v-slot:[`item.paTuyen`]="{ item }">
            <v-select
              :items="listPATuyenForSelect"
              v-model="editedItem.paTuyen"
              label="Nhiệm vụ"
              v-if="item.id === editedItem.id"
              dense
              :hide-details="true"
              required
              :rules="nameRules"
              item-text="properties.tenPATuyen"
              item-value="id"
              @change="paTuyenChange"
            ></v-select>
            <span v-else>{{ item.paTuyen | convertPAT(listPATuyen) }}</span>
          </template>

          <template v-slot:[`item.maDV`]="{ item }">
            <span label="Nhiệm vụ" v-if="item.id === editedItem.id">{{
              editedItem.maDV | convertDV(listDV)
            }}</span>
            <span v-else>{{ item.maDV | convertDV(listDV) }}</span>
          </template>

          <template v-slot:[`item.trangThaiCMPATuyen`]="{ item }">
            <v-select
              :items="listStatus"
              v-model="editedItem.trangThaiCMPATuyen"
              label="Trạng thái nhiệm vụ"
              v-if="item.id === editedItem.id"
              dense
              :hide-details="true"
              required
              :rules="nameRules"
            ></v-select>
            <span v-else>{{
              item.trangThaiCMPATuyen | convertStatus(listStatus)
            }}</span>
          </template>

          <template v-slot:[`item.moTaCMPATuyen`]="{ item }">
            <v-text-field
              v-model="editedItem.moTaCMPATuyen"
              :hide-details="true"
              dense
              single-line
              v-if="item.id === editedItem.id"
              required
              :rules="nameRules"
            ></v-text-field>
            <span v-else>{{ item.moTaCMPATuyen }}</span>
          </template>
          <template v-slot:[`item.ngayCMPATuyen`]="{ item }">
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
                  v-model="editedItem.ngayCMPATuyen"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                v-model="editedItem.ngayCMPATuyen"
                @input="menu2 = false"
                no-title
              ></v-date-picker>
            </v-menu>

            <span v-else>{{ item.ngayCMPATuyen }}</span>
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
import pheDuyetPhuongAnTuyen from "@/api/phe-duyet-phuong-an-tuyen";
import phuongAnTuyen from "@/api/phuong-an-tuyen";
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
import tuyenNhiemVuDieuHanh from "@/api/tuyen-nhiem-vu-dieu-hanh";
import OlStyleDefs from "@/style/OlStyleDefs";

export default {
  mixins: [InteractionsToggle, Mapable, KeyShortcuts],
  components: {
    MapComponent,
  },
  data() {
    return {
      interactionType: "edit-interaction",
      layerName: "geo_pheDuyetPhuongAnTuyen",
      selectedLayer: null,

      dataObject: {},
      search: "",
      geotype: "",
      menu2: false,

      isLoading: false,
      isAdding: false,
      isEditing: false,
      hasFeedback: false,

      headers: this.$appConfig.pheDuyetPhuongAnTuyen.headers,
      nameRules: [(v) => !!v || "Name is required"],

      listPheDuyetPATuyen: [],
      listPATuyen: [],
      listStatus: [],
      listNVDH: [],
      listNVBP: [],
      listDV: [],
      listTuyenNVDH: [],

      listPATuyenForSelect: [],

      editedIndex: -1,
      editedItem: this.$appConfig.pheDuyetPhuongAnTuyen.defaultItem,
      defaultItem: this.$appConfig.pheDuyetPhuongAnTuyen.defaultItem,
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

        const resultPATuyen = await phuongAnTuyen.getAll({});
        const resultDV = await donViApi.getAll({});
        const resultNVDH = await nhiemVuDieuHanh.getAll({});
        const resultStatus = await pheDuyetPhuongAnTuyen.getStatus({});
        const resultNVBP = await nhiemVuBoPhan.getAll({});
        const resultTuyenNVDH = await tuyenNhiemVuDieuHanh.getAll({});

        this.listStatus = resultStatus;
        this.listPATuyen = resultPATuyen.features;
        this.listNVDH = resultNVDH;
        this.listDV = resultDV.features;
        this.listNVBP = resultNVBP;
        this.listTuyenNVDH = resultTuyenNVDH.features;

        let resultPheDuyetPATuyen;
        await pheDuyetPhuongAnTuyen.getAll({}).then((response) => {
          resultPheDuyetPATuyen = response.features.map((item) => {
            return {
              ...item.properties,
              ...this.getInfo(this.listPATuyen, this.listNVBP, item),
              id: item.id,
              geometry: item.geometry,
            };
          });
        });

        this.listPheDuyetPATuyen = resultPheDuyetPATuyen;

        this.isLoading = false;
      } catch (error) {
        console.log(error);
      }
    },

    getInfo(PAT, NVBP, item) {
      let PAItem = PAT.filter((pa) => pa.id === item.properties.paTuyen)[0];

      let NVBPItem = NVBP.filter((nv) => {
        return nv.maNVBP === PAItem.properties.nvbp;
      })[0];

      return {
        paTuyen: PAItem.id,
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
      const styleTuyenNVDH = OlStyleDefs.getDieuHanhStyle();
      const stylePATuyen = OlStyleDefs.getPAViTriStyle();
      const stylePDPATuyen = OlStyleDefs.getPDPAViTriStyle();

      editLayerHelper.addFeaturesToSource2(this.selectedLayer, [
        { features: this.listTuyenNVDH, style: styleTuyenNVDH },
        { features: this.listPATuyen, style: stylePATuyen },
        { features: this.listPheDuyetPATuyen, style: stylePDPATuyen },
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

      this.editedIndex = this.listPheDuyetPATuyen.indexOf(item);

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
      const index = this.listPheDuyetPATuyen.indexOf(item);
      if (confirm("Are you sure you want to delete this item?")) {
        await pheDuyetPhuongAnTuyen.delete(item);
        this.listPheDuyetPATuyen.splice(index, 1);
      }

      //   //remove Feature
      //   editLayerHelper.removeFeatureFromSource(this.selectedLayer, item);
      // }
    },

    close(isSaved) {
      this.editedItem = Object.assign({}, this.defaultItem);
      this.editedIndex = -1;

      this.isAdding && !isSaved && this.listPheDuyetPATuyen.shift();

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
        type: "warning",
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
        type: "warning",
        message: "Nhập thông tin điểm nhiệm vụ điều hành",
        state: true,
        timeout: 2000,
      });

      const addObj = Object.assign({}, this.defaultItem);

      this.listPheDuyetPATuyen.unshift(addObj);

      this.editItem(addObj);
    },

    zoomToLine(item) {
      try {
        const feature = editLayerHelper.createFeature(item);
        const fitOptions = { duration: 1000 };
        this.$map.getView().fit(feature.getGeometry(), fitOptions);
      } catch (error) {
        this.toggleSnackbar({
          type: "warning",
          message: "Không có Tuyến góp ý",
          state: true,
          timeout: 2000,
        });
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
      const join = this.geometry.getCoordinates().map((el) => el.join(" "));

      const coordinates = join.join(",");

      const requestData = {
        ...this.editedItem,
        id: this.editedItem.id,
        geoCMPATuyen: !!this.geometry
          ? `SRID=4326;LINESTRING(${coordinates})`
          : null,
      };

      const { moTaCMPATuyen, trangThaiCMPATuyen, paTuyen } = requestData;

      if (
        moTaCMPATuyen.length === 0 ||
        trangThaiCMPATuyen === null ||
        paTuyen === null
      ) {
        //Thong Bao
        return;
      }

      try {
        let result;
        if (this.isAdding) {
          result = await pheDuyetPhuongAnTuyen.create(requestData);
        } else if (this.isEditing) {
          result = await pheDuyetPhuongAnTuyen.edit(requestData);
        }

        if (!!result && this.editedIndex > -1) {
          const convertData = this.getInfo(
            this.listPATuyen,
            this.listNVBP,
            result
          );

          result = {
            id: result.id,
            ...result.properties,
            ...convertData,
            geometry: result.geometry,
          };

          Object.assign(this.listPheDuyetPATuyen[this.editedIndex], result);
          //Thong bao
          this.toggleSnackbar({
            type: "success",
            message: "Thêm điểm nhiệm vụ điều hành thành công",
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

      //remove layer edit
      // this.olEditCtrl.removeLayerEdit();
    },
    listNVDHChange(item) {
      this.listPATuyenForSelect = [];
      const filterNVBP = this.listNVBP.filter((nvbp) => {
        return nvbp.maNVDH === item;
      });

      filterNVBP.forEach((nvbp) => {
        this.listPATuyen.forEach((pat) => {
          if (pat.properties.nvbp === nvbp.maNVBP) {
            this.listPATuyenForSelect.push(pat);
          }
        });
      });
    },
    paTuyenChange(idPAT) {
      const PAT = this.listPATuyen.filter((item) => item.id === idPAT)[0];
      const filterNVBP = this.listNVBP.filter((nvbp) => {
        return nvbp.maNVBP === PAT.properties.nvbp;
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
    convertPAT: (pat, listPAT) => {
      if (!pat) return "";
      return listPAT.filter((vt) => vt.id === pat)[0].properties.tenPATuyen;
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
</style> -->

<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-data-table
          :headers="headers"
          :items="listPATuyen"
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
                <v-btn color="primary" class="ml-2 white--text">
                  <v-icon dark>mdi-plus</v-icon>Thêm mới
                </v-btn>
              </div>
            </v-toolbar>
          </template>
          <template v-slot:[`item.properties.kieuPATuyen`]="{ item }">
            <span>{{
              item.properties.kieuPATuyen | convertKieuPATuyen(listKieuPA)
            }}</span>
          </template>
          <template v-slot:[`item.properties.trangThaiPATuyen`]="{ item }">
            <span>{{
              item.properties.trangThaiPATuyen | convertStatus(listStatus)
            }}</span>
          </template>
          <template v-slot:[`item.pheDuyet`]="{ item }">
            <v-chip
              v-if="item.pheDuyet"
              class="ma-2"
              color="green"
              text-color="white"
            >
              Đã Phê Duyệt
            </v-chip>
            <v-chip v-else class="ma-2" color="red" text-color="white">
              Chưa phê duyệt
            </v-chip>
          </template>
          <template v-slot:[`item.actions`]="{ item }">
            <v-icon color="yellow" class="mr-2" @click="zoomToLine(item)">
              mdi-map-marker
            </v-icon>
            <v-icon color="green" class="mr-2" @click="pheDuyet(item)">
              mdi-checkbox-marked-circle
            </v-icon>
            <v-icon color="red" @click="showThongBao(item)">
              mdi-note-text-outline
            </v-icon>
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

    <v-dialog v-model="dialog" max-width="500">
      <v-card>
        <v-card-title class="text-h5"> Ghi chú phương án </v-card-title>

        <v-card-text>
          <v-textarea
            name="input-7-1"
            label="Ghi chú"
            value=""
            outlined
            hide-details
            v-model="note"
          ></v-textarea>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn color="green darken-1" text @click="dialog = false">
            Hủy
          </v-btn>

          <v-btn color="green darken-1" text @click="saveThongBao()">
            OK
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import OlEditController from "@/controllers/OlEdtiController";

import phuongAnTuyen from "@/api/phuong-an-tuyen";
import nhiemVuDieuHanh from "@/api/nhiem-vu-dieu-hanh";
import nhiemVuBoPhan from "@/api/nhiem-vu-bo-phan";
import donViApi from "@/api/don-vi";
import tuyenNhiemVuDieuHanh from "@/api/tuyen-nhiem-vu-dieu-hanh";

import MapComponent from "@/components/ol/MapComponent.vue";
import { EventBus } from "@/EventBus";
import { getAllChildLayers } from "@/utils/Layer";
import { mapGetters, mapMutations } from "vuex";
import editLayerHelper from "@/controllers/OlEditLayerHelper";
import { InteractionsToggle } from "@/mixins/InteractionsToggle";
import { Mapable } from "@/mixins/Mapable";
import { KeyShortcuts } from "@/mixins/KeyShortcuts";
import OlStyleDefs from "@/style/OlStyleDefs";

export default {
  mixins: [InteractionsToggle, Mapable, KeyShortcuts],
  components: {
    MapComponent,
  },
  data() {
    return {
      interactionType: "edit-interaction",
      layerName: "geo_tuyenPAVT",
      selectedLayer: null,

      dataObject: {},
      search: "",
      geotype: "",
      menu2: false,

      isLoading: false,
      isAdding: false,
      isEditing: false,

      dialog: false,
      note: "",

      headers: this.$appConfig.pheDuyetPhuongAnTuyen.headers,
      nameRules: [(v) => !!v || "Name is required"],

      listPATuyen: [],
      listStatus: [],
      listPATShowOnMap: [],
      listKieuPA: [
        {
          value: 1,
          text: "Tuyến bố trí công trình",
        },
        {
          value: 2,
          text: "Tuyến hành quân",
        },
      ],

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

        const resultDV = await donViApi.getAll({});
        const resultNVDH = await nhiemVuDieuHanh.getAll({});
        const resultNVBP = await nhiemVuBoPhan.getAll({});
        const resultTuyenNVDH = await tuyenNhiemVuDieuHanh.getAll({});
        const listFeaturesPAT = await phuongAnTuyen.getAll({});

        this.listStatus = await phuongAnTuyen.getStatus({});
        this.listNVDH = resultNVDH;
        this.listDV = resultDV.features;
        this.listNVBP = resultNVBP;
        this.listTuyenNVDH = resultTuyenNVDH.features;

        this.listPATShowOnMap = listFeaturesPAT.features;

        this.listPATuyen = listFeaturesPAT.features.filter(
          (item) => !item.properties.pheDuyet
        );

        //mapping Data
        this.listPATuyen = this.listPATuyen.map((item) => {
          //get NVBP;
          const nvbp = this.listNVBP.find(
            (nvbp) => nvbp.maNhanDang === item.properties.nvbp
          );

          //Get DiemNVDH
          const listTuyenNVDH = this.listTuyenNVDH.filter(
            (diemNVDH) => diemNVDH.properties.nvdh === nvbp.maNVDH
          );

          item["listTuyenNVDH"] = listTuyenNVDH;

          return item;
        });

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

      //load Điểm nhiệm vụ điều hành
      editLayerHelper.addFeaturesToSource2(this.selectedLayer, [
        { features: this.listTuyenNVDH, style: "nvdh" },
        { features: this.listPATShowOnMap, style: "pa" },
      ]);
    },

    async pheDuyet(item) {
      try {
        this.editedIndex = this.listPATuyen.indexOf(item);

        this.editedItem = Object.assign({}, item);

        const requestData = {
          pheDuyet: true,
          id: this.editedItem.id,
          trangthaiPATuyen:
            this.editedItem.properties["trangthaiPATuyen"] === 1 ? 2 : 4,
        };

        let result = await phuongAnTuyen.update(requestData);

        if (!!result && this.editedIndex > -1) {
          this.listPATuyen.splice(this.editedIndex, 1);

          //update Data
          this.initData().then(() => {
            this.onMapBound();
          });

          //Thong bao
          this.toggleSnackbar({
            type: "success",
            message: "Phê Duyệt thành công điều hành thành công",
            state: true,
            timeout: 2000,
          });
        }
      } catch (error) {
        console.log(error);
      }
    },
    showThongBao(item) {
      this.editedIndex = this.listPATuyen.indexOf(item);
      this.editedItem = Object.assign({}, item);

      this.note = item.properties.thongBao || "";
      this.dialog = true;
    },

    async saveThongBao() {
      try {
        const requestData = {
          thongBao: this.note,
          id: this.editedItem.id,
        };
        let result = await phuongAnTuyen.update(requestData);

        if (!!result && this.editedIndex > -1) {
          Object.assign(this.listPATuyen[this.editedIndex], result);

          //Thong bao
          this.toggleSnackbar({
            type: "success",
            message: "Thêm điểm nhiệm vụ điều hành thành công",
            state: true,
            timeout: 2000,
          });

          this.dialog = false;
        }
      } catch (error) {
        console.log(error);
      }
    },
    closeThongBao() {
      this.editedItem = Object.assign({}, this.defaultItem);
      this.editedIndex = -1;

      this.dialog = false;
    },

    zoomToLine(item) {
      try {
        const feature = editLayerHelper.createFeature(item);
        const fitOptions = { duration: 1000 };
        this.$map.getView().fit(feature.getGeometry(), fitOptions);
      } catch (error) {
        this.toggleSnackbar({
          type: "warning",
          message: "Không có Tuyến góp ý",
          state: true,
          timeout: 2000,
        });
      }
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
    convertKieuPATuyen: (kieu, listKieuPA) => {
      if (!kieu) return "";

      return listKieuPA.find((nv) => nv.value === kieu).text;
    },
    convertStatus: (maStatus, listStatus) => {
      if (!maStatus) return "";

      return listStatus.find((stt) => stt.value === maStatus).text;
    },
  },
};
</script>

<style>
.theme--light.v-data-table.v-data-table--fixed-header thead th {
  background: rgb(160, 159, 159) !important;
}
</style>
