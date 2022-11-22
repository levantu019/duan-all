<template>
  <div class="dashboard">
    <Header />
    <v-main>
      <v-container class="container" fluid>
        <v-row no-gutters style="height: 100%">
          <v-col cols="3" class="nav">
            <v-navigation-drawer
              v-model="drawer"
              width="100%"
              hide-overlay
              permanent
            >
              <!--  -->
              <v-tabs
                background-color="transparent"
                class="wrapper-tabs"
                color="#555555"
              >
                <v-tabs-slider color="success"></v-tabs-slider>
                <v-tab class="">
                  <v-icon left>mdi-layers-outline</v-icon>
                  Lớp bản đồ
                </v-tab>
              </v-tabs>
              <v-text-field
                label="Tìm lớp bản đồ"
                prepend-inner-icon="mdi-filter-outline"
                v-model="search"
              ></v-text-field>
              <v-treeview
                selectable
                :items="items"
                :search="search"
                v-model="selection"
                return-object
                dense
              >
                <template v-slot:prepend="{ item }">
                  <v-icon color="primary" v-if="item.id.includes('NDL')">
                    mdi-layers-outline
                  </v-icon>
                </template>
                <template v-slot:append="{ item }">
                  <v-icon
                    @click="showAttributes(item)"
                    dense
                    v-if="item.id.includes('LDL')"
                  >
                    mdi-table-large</v-icon
                  >
                </template>
              </v-treeview>
            </v-navigation-drawer>
          </v-col>
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
            <div class="toolbar-right">
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
            </div>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
  </div>
</template>
<script>
import Header from "@/components/layouts/TruongSaPortal/Header.vue";
import MapComponent from "@/components/ol/MapComponent.vue";

import TileLayer from "ol/layer/Tile";
import TileWMS from "ol/source/TileWMS";

import nhomDuLieu from "@/api/nhom-du-lieu";
import lopDuLieu from "@/api/lop-du-lieu";

export default {
  components: {
    Header,
    MapComponent,
  },
  async created() {
    const groupSelect = await this.getGroupLayerSelect();

    await this.getLayerByGroup(groupSelect);

    this.getLayerShow(this.items[0].children, groupSelect[0]);

    this.initMap();
  },
  data() {
    return {
      drawer: true,
      tab: null,
      search: null,
      selection: [],
      oldSelection: [],
      groupLayer: [],
      layers: [],
      items: [{ id: "", children: [{ id: "" }] }],
      sheet: true,
      show: false,
      headers: [
        {
          text: "Dessert (100g serving)",
          align: "start",
          sortable: false,
          value: "name",
        },
        { text: "Calories", value: "calories" },
        { text: "Fat (g)", value: "fat" },
        { text: "Carbs (g)", value: "carbs" },
        { text: "Protein (g)", value: "protein" },
        { text: "Iron (%)", value: "iron" },
      ],
      desserts: [
        {
          name: "Frozen Yogurt",
          calories: 200,
          fat: 6.0,
          carbs: 24,
          protein: 4.0,
          iron: "1%",
        },
        {
          name: "Ice cream sandwich",
          calories: 200,
          fat: 9.0,
          carbs: 37,
          protein: 4.3,
          iron: "1%",
        },
        {
          name: "Eclair",
          calories: 300,
          fat: 16.0,
          carbs: 23,
          protein: 6.0,
          iron: "7%",
        },
        {
          name: "Cupcake",
          calories: 300,
          fat: 3.7,
          carbs: 67,
          protein: 4.3,
          iron: "8%",
        },
        {
          name: "Gingerbread",
          calories: 400,
          fat: 16.0,
          carbs: 49,
          protein: 3.9,
          iron: "16%",
        },
        {
          name: "Jelly bean",
          calories: 400,
          fat: 0.0,
          carbs: 94,
          protein: 0.0,
          iron: "0%",
        },
        {
          name: "Lollipop",
          calories: 400,
          fat: 0.2,
          carbs: 98,
          protein: 0,
          iron: "2%",
        },
        {
          name: "Honeycomb",
          calories: 400,
          fat: 3.2,
          carbs: 87,
          protein: 6.5,
          iron: "45%",
        },
        {
          name: "Donut",
          calories: 500,
          fat: 25.0,
          carbs: 51,
          protein: 4.9,
          iron: "22%",
        },
        {
          name: "KitKat",
          calories: 500,
          fat: 26.0,
          carbs: 65,
          protein: 7,
          iron: "6%",
        },
      ],
    };
  },
  methods: {
    initMap() {
      this.$map.getAllLayers().forEach((layer) => {
        if (layer.className !== "ol-layer") {
          this.$map.removeLayer(layer);
        }
      });

      this.selection.forEach((item) => {
        if (!!item.pathPublic) {
          const layer = new TileLayer({
            source: new TileWMS({
              url: item.pathPublic,
              params: { LAYERS: item.tenLop, tiled: true },
            }),
            serverType: "geoserver",
            crossOrigin: "anonymous",
            zIndex: 1,
            className: item.id,
          });
          this.$map.addLayer(layer);
        }
      });
    },
    getLayerShow(array, groupSelect) {
      for (let i = 0; i < array.length; i++) {
        if (
          array[i].maNhom === groupSelect.maNhanDang &&
          array[i].hienThiLopChuyenDe
        ) {
          this.selection.push(array[i]);
        }
      }
    },

    async getGroupLayerSelect() {
      const res = await nhomDuLieu.getAll({});
      const groupSelect = res.filter(
        (group) => group.maNhanDang === this.$route.params.groupId
      );

      return groupSelect;
    },

    async getLayerByGroup(groupSelect) {
      const resLayers = await lopDuLieu.getAll({});
      this.layers = resLayers.map((layer) => {
        return {
          ...layer,
          name: layer["tenHienThiLop"],
          id: layer["maNhanDang"],
        };
      });

      this.items = groupSelect.map((item) => {
        let children = this.layers.filter(
          (layer) => layer.maNhom === item.maNhanDang
        );
        return {
          ...item,
          id: item["maNhanDang"],
          name: item["tenNhom"],
          children: children,
        };
      });
    },
    showAttributes(item) {
      console.log(item);
    },
  },
  watch: {
    selection(newValue, oldVal) {
      if (newValue.length > oldVal.length) {
        let itemsDiff = newValue.filter((x) => !oldVal.includes(x));
        itemsDiff.forEach((itemDiff) => {
          const layer = new TileLayer({
            source: new TileWMS({
              url: itemDiff.pathPublic,
              params: { LAYERS: itemDiff.tenLop, tiled: true },
            }),
            serverType: "geoserver",
            crossOrigin: "anonymous",
            zIndex: 1,
            className: itemDiff.id,
          });
          this.$map.addLayer(layer);
          // }
        });
      } else {
        let itemsDiff = oldVal.filter((x) => !newValue.includes(x));
        let allLayers = this.$map.getAllLayers();
        itemsDiff.forEach((item) => {
          let layer = allLayers.find((l) => l.className_ === item.id);

          this.$map.removeLayer(layer);
        });
      }
    },
  },
};
</script>

<style scoped>
.container {
  height: calc(100vh - 64px);
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
  bottom: 0;
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
  top: 0;
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

/* .toolbar-right-bottom > li {
  border-top: turquoise;
} */
</style>
