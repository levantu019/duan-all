<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-data-table
          :headers="headers"
          :items="listPheDuyetPAVung"
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

          <template v-slot:[`item.nguoiCMPAVung`]="{ item }">
            <v-text-field
              v-model="editedItem.nguoiCMPAVung"
              :hide-details="true"
              dense
              label="Người phê duyệt"
              v-if="item.id === editedItem.id"
            ></v-text-field>
            <span v-else>{{ item.nguoiCMPAVung }}</span>
          </template>
          <template v-slot:[`item.actions`]="{ item }">
            <div v-if="item.id === editedItem.id">
              <v-icon color="red" class="mr-2" @click="close(false)">
                mdi-window-close
              </v-icon>
              <v-icon color="green" @click="save"> mdi-content-save </v-icon>
            </div>
            <div v-else>
              <v-icon color="yellow" class="mr-2" @click="zoomToPolygon(item)">
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
          <template v-slot:[`item.paVung`]="{ item }">
            <v-select
              :items="listPAVungForSelect"
              v-model="editedItem.paVung"
              label="Nhiệm vụ"
              v-if="item.id === editedItem.id"
              dense
              :hide-details="true"
              required
              :rules="nameRules"
              item-text="properties.tenPAVung"
              item-value="id"
              @change="paVungChange"
            ></v-select>
            <span v-else>{{ item.paVung | convertPAVung(listPAVung) }}</span>
          </template>

          <template v-slot:[`item.maDV`]="{ item }">
            <span label="Nhiệm vụ" v-if="item.id === editedItem.id">{{
              editedItem.maDV | convertDV(listDV)
            }}</span>
            <span v-else>{{ item.maDV | convertDV(listDV) }}</span>
          </template>

          <template v-slot:[`item.trangThaiCMPAVung`]="{ item }">
            <v-select
              :items="listStatus"
              v-model="editedItem.trangThaiCMPAVung"
              label="Trạng thái nhiệm vụ"
              v-if="item.id === editedItem.id"
              dense
              :hide-details="true"
              required
              :rules="nameRules"
            ></v-select>
            <span v-else>{{
              item.trangThaiCMPAVung | convertStatus(listStatus)
            }}</span>
          </template>

          <template v-slot:[`item.moTaCMPAVung`]="{ item }">
            <v-text-field
              v-model="editedItem.moTaCMPAVung"
              :hide-details="true"
              dense
              single-line
              v-if="item.id === editedItem.id"
              required
              :rules="nameRules"
            ></v-text-field>
            <span v-else>{{ item.moTaCMPAVung }}</span>
          </template>
          <template v-slot:[`item.ngayCMPAVung`]="{ item }">
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
                  v-model="editedItem.ngayCMPAVung"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                v-model="editedItem.ngayCMPAVung"
                @input="menu2 = false"
                no-title
              ></v-date-picker>
            </v-menu>

            <span v-else>{{ item.ngayCMPAVung }}</span>
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
// call api
import pheDuyetPhuongAnVung from "@/api/phe-duyet-phuong-an-vung";
import phuongAnVung from "@/api/phuong-an-vung";
import nhiemVuDieuHanh from "@/api/nhiem-vu-dieu-hanh";
import nhiemVuBoPhan from "@/api/nhiem-vu-bo-phan";
import vungNhiemVuDieuHanh from "@/api/vung-nhiem-vu-dieu-hanh";

import OlEditController from "@/controllers/OlEdtiController";

import MapComponent from "@/components/ol/MapComponent.vue";
import { EventBus } from "@/EventBus";
import { getAllChildLayers } from "@/utils/Layer";
import { mapGetters, mapMutations } from "vuex";
import editLayerHelper from "@/controllers/OlEditLayerHelper";
import { InteractionsToggle } from "@/mixins/InteractionsToggle";
import { Mapable } from "@/mixins/Mapable";
import { KeyShortcuts } from "@/mixins/KeyShortcuts";

import donViApi from "@/api/don-vi";
import OlStyleDefs from "@/style/OlStyleDefs";

export default {
  mixins: [InteractionsToggle, Mapable, KeyShortcuts],
  components: {
    MapComponent,
  },
  data() {
    return {
      interactionType: "edit-interaction",
      layerName: "geo_pheDuyetPhuongAnVung",
      selectedLayer: null,

      dataObject: {},
      search: "",
      geotype: "",
      menu2: false,

      isLoading: false,
      isAdding: false,
      isEditing: false,
      hasFeedback: false,

      headers: this.$appConfig.pheDuyetPhuongAnVung.headers,
      nameRules: [(v) => !!v || "Name is required"],

      listPheDuyetPAVung: [],
      listPAVung: [],
      listStatus: [],
      listNVDH: [],
      listNVBP: [],
      listDV: [],
      listVungNVDH: [],

      listPAVungForSelect: [],

      editedIndex: -1,
      editedItem: this.$appConfig.pheDuyetPhuongAnVung.defaultItem,
      defaultItem: this.$appConfig.pheDuyetPhuongAnVung.defaultItem,
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

        const resultPAVung = await phuongAnVung.getAll({});
        const resultDV = await donViApi.getAll({});
        const resultNVDH = await nhiemVuDieuHanh.getAll({});
        const resultStatus = await pheDuyetPhuongAnVung.getStatus({});
        const resultNVBP = await nhiemVuBoPhan.getAll({});
        const resultVungNVDH = await vungNhiemVuDieuHanh.getAll({});

        this.listStatus = resultStatus;
        this.listPAVung = resultPAVung.features;
        this.listNVDH = resultNVDH;
        this.listDV = resultDV.features;
        this.listNVBP = resultNVBP;
        this.listVungNVDH = resultVungNVDH.features;

        let resultPheDuyetPAVung;
        await pheDuyetPhuongAnVung.getAll({}).then((response) => {
          resultPheDuyetPAVung = response.features.map((item) => {
            return {
              ...item.properties,
              ...this.getInfo(this.listPAVung, this.listNVBP, item),
              id: item.id,
              geometry: item.geometry,
            };
          });
        });

        this.listPheDuyetPAVung = resultPheDuyetPAVung;

        this.isLoading = false;
      } catch (error) {
        console.log(error);
      }
    },

    getInfo(PAV, NVBP, item) {
      let PAItem = PAV.filter((pa) => pa.id === item.properties.paVung)[0];

      let NVBPItem = NVBP.filter((nv) => {
        return nv.maNVBP === PAItem.properties.nvbp;
      })[0];

      return {
        paVung: PAItem.id,
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
      const styleVungNVDH = OlStyleDefs.getDieuHanhStyle();
      const stylePAVung = OlStyleDefs.getPAViTriStyle();
      const stylePDPAVung = OlStyleDefs.getPDPAViTriStyle();

      editLayerHelper.addFeaturesToSource2(this.selectedLayer, [
        { features: this.listVungNVDH, style: styleVungNVDH },
        { features: this.listPAVung, style: stylePAVung },
        { features: this.listPheDuyetPAVung, style: stylePDPAVung },
      ]);
    },

    editItem(item) {
      this.isEditing = true;

      this.editedIndex = this.listPheDuyetPAVung.indexOf(item);

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
      const index = this.listPheDuyetPAVung.indexOf(item);
      if (confirm("Are you sure you want to delete this item?")) {
        await pheDuyetPhuongAnVung.delete(item);
        this.listPheDuyetPAVung.splice(index, 1);
      }

      //   //remove Feature
      //   editLayerHelper.removeFeatureFromSource(this.selectedLayer, item);
      // }
    },

    close(isSaved) {
      this.editedItem = Object.assign({}, this.defaultItem);
      this.editedIndex = -1;

      this.isAdding && !isSaved && this.listPheDuyetPAVung.shift();

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
        message: "Chọn vùng nhiệm vụ điều hành",
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

      this.listPheDuyetPAVung.unshift(addObj);

      this.editItem(addObj);
    },

    zoomToPolygon(item) {
      try {
        const feature = editLayerHelper.createFeature(item);
        const fitOptions = { duration: 1000 };
        this.$map.getView().fit(feature.getGeometry(), fitOptions);

        //zoom to linestring extend
      } catch (error) {
        this.toggleSnackbar({
          type: "warning",
          message: "Không có Vùng góp ý",
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
      const join = this.geometry.getCoordinates()[0].map((el) => el.join(" "));

      const coordinates = join.join(",");

      const requestData = {
        ...this.editedItem,
        id: this.editedItem.id,
        geoCMPAVung: !!this.geometry
          ? `SRID=4326;POLYGON((${coordinates}))`
          : null,
      };

      const { moTaCMPAVung, trangThaiCMPAVung, paVung } = requestData;

      if (
        moTaCMPAVung.length === 0 ||
        trangThaiCMPAVung === null ||
        paVung === null
      ) {
        //Thong Bao
        return;
      }

      try {
        let result;
        if (this.isAdding) {
          result = await pheDuyetPhuongAnVung.create(requestData);
        } else if (this.isEditing) {
          result = await pheDuyetPhuongAnVung.edit(requestData);
        }

        if (!!result && this.editedIndex > -1) {
          const convertData = this.getInfo(
            this.listPAVung,
            this.listNVBP,
            result
          );

          result = {
            id: result.id,
            ...result.properties,
            ...convertData,
            geometry: result.geometry,
          };

          Object.assign(this.listPheDuyetPAVung[this.editedIndex], result);
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
      this.listPAVungForSelect = [];
      const filterNVBP = this.listNVBP.filter((nvbp) => {
        return nvbp.maNVDH === item;
      });

      filterNVBP.forEach((nvbp) => {
        this.listPAVung.forEach((pav) => {
          if (pav.properties.nvbp === nvbp.maNVBP) {
            this.listPAVungForSelect.push(pav);
          }
        });
      });
    },
    paVungChange(idPAV) {
      const PAV = this.listPAVung.filter((item) => item.id === idPAV)[0];
      const filterNVBP = this.listNVBP.filter((nvbp) => {
        return nvbp.maNVBP === PAV.properties.nvbp;
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
    convertPAVung: (pav, listPAV) => {
      if (!pav) return "";
      return listPAV.filter((v) => v.id === pav)[0].properties.tenPAVung;
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
