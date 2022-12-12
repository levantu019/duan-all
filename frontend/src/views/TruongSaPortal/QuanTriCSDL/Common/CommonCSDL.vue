<template>
  <div class="pa-0">
    <v-row class="pa-0">
      <v-col cols="12">
        <v-toolbar
          color="grey lighten-2"
          class="pa-1 d-flex align-center"
          dense
        >
          <div class="d-flex">
            <v-autocomplete
              v-model="search"
              :items="listItems"
              item-text="properties.nguyenNhanThayDoi"
              dense
              outlined
              hide-details
              hide-no-data
              append-icon=""
              clearable
              return-object
              placeholder="Tìm kiếm"
              solo
            />
            <v-btn
              color="white"
              class="ml-3"
              @click="addNewGeometry()"
              :disabled="isAdding"
            >
              <v-icon class="mr-1" color="success">mdi-plus-circle </v-icon>Thêm
              mới
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
              <v-icon class="mr-1" color="warning">mdi-table-large-plus </v-icon
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
      </v-col>
    </v-row>
    <v-row class="mt-0 ma-0">
      <MapComponent />
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
          :items="listItems"
          multi-sort
          class="elevation-1"
          fixed-header
          height="290"
          :search="search"
        >
          <template v-slot:[`item.actions`]="{ item }">
            <v-icon color="yellow" class="mr-2" @click="zoomToPoint(item)">
              mdi-map-marker
            </v-icon>
            <v-icon color="green" class="mr-2" @click="editItem(item)">
              mdi-square-edit-outline
            </v-icon>
            <v-icon color="red" @click="deleteItem(item)"> mdi-delete </v-icon>
          </template>
          <template v-slot:[`body.append`]>
            <span></span>
          </template>
        </v-data-table>
      </v-sheet>
    </v-row>
    <v-dialog v-model="dialog" persistent max-width="600px">
      <v-toolbar dark color="primary">
        <v-toolbar-title>Thông tin đảo</v-toolbar-title>
      </v-toolbar>
      <v-card>
        <v-card-text>
          <v-form ref="form" lazy-validation class="pt-2">
            <template v-for="(item, index) in headers">
              <v-text-field
                :key="index"
                v-if="
                  item.hasOwnProperty('type') &&
                  (item.type.name === 'text' ||
                    item.type.name === 'number' ||
                    item.type.name === 'date')
                "
                v-model="editedItem[item.type.key]"
                outlined
                :placeholder="item.text"
                :label="item.text"
                :rules="item.type.required ? nameRules : []"
                :type="item.type.name"
                :required="item.type.required"
              ></v-text-field>
              <v-textarea
                v-if="
                  item.hasOwnProperty('type') && item.type.name === 'textarea'
                "
                :key="index"
                v-model="editedItem[item.type.key]"
                outlined
                :placeholder="item.text"
                :label="item.text"
                :required="item.type.required"
                :rules="item.type.required ? nameRules : []"
              ></v-textarea>

              <v-combobox
                v-if="
                  item.hasOwnProperty('type') && item.type.name === 'select'
                "
                :key="index"
                v-model="editedItem[item.type.key]"
                :items="item.type.value || []"
                :placeholder="item.text"
                outlined
                :label="item.text"
                :rules="item.type.required ? nameRules : []"
                :required="item.type.required"
              ></v-combobox>
            </template>
          </v-form>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn width="100" depressed color="primary" @click="save">
            Lưu lại
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</template>

<script>
import OlEditController from "@/controllers/OlEdtiController";
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
  props: ["headers", "listItems", "isLoading", "typeGeo"],
  components: {
    MapComponent,
  },
  data() {
    return {
      interactionType: "edit-interaction",

      selectedLayer: null,

      dialog: false,
      show: false,

      search: null,

      // menu1: false,
      // date: new Date(Date.now() - new Date().getTimezoneOffset() * 60000)
      //   .toISOString()
      //   .substr(0, 10),

      isAdding: false,
      isEditing: false,

      //move header to config

      nameRules: [(v) => !!v || "*Bắt buộc"],

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

    async initData() {},

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

    // editItem(item) {
    //   this.isEditing = true;

    //   this.editedIndex = this.listDiemNhiemVu.indexOf(item);

    //   this.editedItem = Object.assign({}, item);

    //   if (!this.isAdding && this.isEditing) {
    //     const editType = "modify";
    //     const startCb = this.onDrawStart;
    //     const endCb = this.onDrawModifyEnd;

    //     this.olEditCtrl.addInteraction(editType, startCb, endCb, item);

    //     EventBus.$emit("ol-interaction-activated", this.interactionType);
    //   }
    // },

    // async deleteItem(item) {
    //   const index = this.listDiemNhiemVu.indexOf(item);
    //   if (confirm("Are you sure you want to delete this item?")) {
    //     await diemNhiemVuDieuHanh.delete(item);
    //     this.listDiemNhiemVu.splice(index, 1);

    //     //remove Feature
    //     editLayerHelper.removeFeatureFromSource(this.selectedLayer, item);
    //   }
    // },

    close(isSaved) {
      // this.editedItem = Object.assign({}, this.defaultItem);
      // this.editedIndex = -1;

      // this.isAdding && !isSaved && this.listDiemNhiemVu.shift();

      this.stop();

      this.isAdding = false;
      this.isEditing = false;
    },
    addNewGeometry() {
      if (this.typeGeo === "") throw new Error("Don't have type Geo");

      this.selectedLayer = this.olEditCtrl.createEditLayer(
        null,
        null,
        this.typeGeo
      );

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

        this.olEditCtrl.addInteraction(editType, startCb, endCb, null);

        EventBus.$emit("ol-interaction-activated", this.interactionType);
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
      this.$emit("showDialog");
    },

    // zoomToPoint(item) {
    //   const view = this.$map.getView();
    //   editLayerHelper.zoomToPoint(view, item, 18);
    // },

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

      // me.stop();

      this.dialog = true;

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

        this.dialog = true;
      }
    },
    stop() {
      this.olEditCtrl.clear();
      EventBus.$emit("ol-interaction-stopped", this.interactionType);
    },

    save() {
      // console.log(this.editedItem);

      // if (this.$refs.form.validate() && !!this.geometry) {
      //   try {
      //     const requestData = {
      //       ...this.editedItem,
      //       ngayPhienBan: new Date(this.editedItem.ngayPhienBan).toISOString(),
      //       id: this.editedItem.id,
      //       geom: `{'type':'Point','coordinates':[${this.geometry.flatCoordinates[0]},${this.geometry.flatCoordinates[1]}]}`,
      //     };
      //     const res = await service.post(
      //       "/nen-dia-ly/dia-hinh/diem-do-cao/",
      //       requestData
      //     );
      //     console.log(res);
      //   } catch (error) {
      //     console.log(error);
      //   }
      // } else {
      // }

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
      // this.close(true);
      this.stop();

      this.dialog = false;

      this.$map.removeLayer(this.selectedLayer);

      // this.onMapBound();

      this.selectedLayer = null;

      // console.log(this.editedItem);

      this.$emit("saveItem", this.editedItem);

      //remove layer edit
      // this.olEditCtrl.removeLayerEdit();
    },
  },
  computed: {
    ...mapGetters("draw", {
      geometry: "geometry",
    }),
  },
};
</script>

<style>
.container {
  height: calc(100vh - 75px);
  width: 100vw;
  padding: 0px;
}
.wrapper-tabs {
  border-bottom: 1px solid #ddd;
}
.nav {
  height: calc(100vh - 64px);
  overflow-y: hidden;
}
#btshowTable {
  z-index: 100;
  position: fixed;
  bottom: 37px;
  right: 35%;
  padding: 5px 19px;
  border-radius: 5px 5px 0 0;
  line-height: 17px;
  box-shadow: 0px 0px 5px 2px #c2c2c2;
  background: white;
}
#btshowTable:hover {
  background: #10a5e0;
  color: white;
  font-weight: bold;
}
.view-attribute {
  position: absolute;
  bottom: 0;
  left: 0;
}
.wrapper-map {
  position: relative;
}
.theme--light.v-data-table.v-data-table--fixed-header thead th {
  background: #aedbec !important;
}

.toolbar-top {
  position: absolute;
  left: 0;
  top: 0;
  height: 40px;
  width: 100%;
  z-index: 10;
  background: white;
  box-shadow: 0 1px 3px rgb(0 0 0 / 12%), 0 1px 2px rgb(0 0 0 / 10%);

  display: flex;
}
.toolbar-top-left,
.toolbar-top-right,
.toolbar-right-top {
  list-style: none;
  padding: 0;
  display: flex;
}

.tool {
  border: 1px solid;
  border-color: #cdcdcd #d5d5d5 #d0d0d0;
  height: 40px;
  width: 40px;
  display: flex;
  justify-content: center;
  align-items: center;
  border-left: transparent;
}
.toolbar-top-right > .tool:first-child {
  border-left: 1px solid #cdcdcd;
}
.toolbar-right {
  position: absolute;
  top: 70px;
  right: 8px;

  display: flex;
  flex-direction: column;
}
.toolbar-right > ul {
  padding: 0;
  border-left: 1px solid #cdcdcd;
}

.toolbar-right-bottom {
  margin-top: 10px;
  background-color: white;
}

.toolbar-right-top {
  flex-direction: column;
  background-color: white;
}
</style>
