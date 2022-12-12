<template>
  <div class="pa-0">
    <CommonCSDL
      :headers="headers"
      :listItems="listItems"
      :isLoading="isLoading"
      :typeGeo="typeGeo"
      @saveItem="saveHandler"
      @showDialog="showDialogHandler"
    >
    </CommonCSDL>
  </div>
</template>

<script>
import { mapGetters, mapMutations } from "vuex";
// import editLayerHelper from "@/controllers/OlEditLayerHelper";
import { InteractionsToggle } from "@/mixins/InteractionsToggle";
import { Mapable } from "@/mixins/Mapable";
import { KeyShortcuts } from "@/mixins/KeyShortcuts";
import service from "@/utils/request";

// import { KEY_ATTRIBUTE } from "@/constants/keyAttributes";
import { DIEM_DO_CAO_CONFIG } from "@/constants";
import CommonCSDL from "@/views/TruongSaPortal/QuanTriCSDL/Common/CommonCSDL.vue";

export default {
  mixins: [InteractionsToggle, Mapable, KeyShortcuts],
  components: {
    CommonCSDL,
  },
  data() {
    return {
      interactionType: "edit-interaction",

      // selectedLayer: null,

      typeGeo: "Point",

      search: "",

      isLoading: false,
      isAdding: false,
      isEditing: false,

      //move header to config

      headers: [],

      listItems: [],
    };
  },
  created() {
    this.initData();

    // .then(() => {
    //   this.onMapBound();
    // });
  },

  methods: {
    // ...mapMutations("draw", {
    //   setGeometry: "SET_GEOMETRY",
    // }),
    ...mapMutations("map", {
      toggleSnackbar: "TOGGLE_SNACKBAR",
    }),

    async initData() {
      try {
        this.isLoading = true;

        //get Features
        const { features } = await service.get(
          "/nen-dia-ly/dia-hinh/diem-do-cao/"
        );

        //assign features
        this.listItems = features;

        //assign headers
        this.headers = DIEM_DO_CAO_CONFIG.fields;

        this.isLoading = false;
      } catch (error) {
        console.log(error);
      }
    },

    // onMapBound() {
    //   this.olEditCtrl = new OlEditController(this.$map);

    //   //add Feature to Layer
    //   // this.selectedLayer = editableLayers[0];
    //   // editLayerHelper.selectedLayer = this.selectedLayer;

    // },

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

    // close(isSaved) {
    //   this.editedItem = Object.assign({}, this.defaultItem);
    //   this.editedIndex = -1;

    //   this.isAdding && !isSaved && this.listDiemNhiemVu.shift();

    //   this.stop();

    //   this.isAdding = false;
    //   this.isEditing = false;
    // },
    // addNewPosition() {
    //   const me = this;

    //   this.selectedLayer = this.olEditCtrl.createEditLayer(null, null, "Point");

    //   editLayerHelper.selectedLayer = this.selectedLayer;

    //   this.isAdding = true;

    //   this.toggleSnackbar({
    //     type: "warning",
    //     message: "Vẽ đối tượng trên bản đồ để thêm dữ liệu không gian",
    //     state: true,
    //     timeout: 2000,
    //   });

    //   const editType = "add";

    //   if (editType !== undefined) {
    //     const startCb = this.onDrawStart;
    //     const endCb = this.onDrawEnd;

    //     me.olEditCtrl.addInteraction(editType, startCb, endCb, null);

    //     EventBus.$emit("ol-interaction-activated", me.interactionType);
    //   }
    // },
    // addNewInfo() {
    //   this.stop();

    //   this.toggleSnackbar({
    //     type: "warning",
    //     message: "Nhập thông tin đối tượng",
    //     state: true,
    //     timeout: 2000,
    //   });

    //   //show popup input info
    //   this.dialog = true;
    // },

    // onDrawEnd(evt) {
    //   const me = this;
    //   const feature = evt.feature;

    //   const featureGeometry = feature
    //     .getGeometry()
    //     .clone()
    //     .transform("EPSG:3857", "EPSG:4756");

    //   this.setGeometry(featureGeometry);

    //   me.stop();

    //   me.addNewInfo();
    // },

    // onDrawModifyEnd(evt) {
    //   if (evt.features.getArray().length > 0) {
    //     const feature = evt.features.getArray()[0];

    //     const featureGeometry = feature
    //       .getGeometry()
    //       .clone()
    //       .transform("EPSG:3857", "EPSG:4756");

    //     this.setGeometry(featureGeometry);
    //   }
    // },
    // stop() {
    //   this.olEditCtrl.clear();
    //   EventBus.$emit("ol-interaction-stopped", this.interactionType);
    // },

    showDialogHandler() {
      this.dialog = true;
    },

    async saveHandler(editItem) {
      console.log(editItem);

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
      // this.stop();

      // this.dialog = false;

      // this.$map.removeLayer(this.selectedLayer);

      // this.onMapBound();

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
