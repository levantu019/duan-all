<template>
  <v-container id="ol-map-container">
    <!-- <overlay-popup :title="popup.title" v-show="popup.isVisible" ref="popup">
      <v-btn icon>
        <v-icon small>fas fa-times</v-icon>
      </v-btn>
      <template v-slot:close>
        <template v-if="getInfoResult.length > 1">
          <span
            >({{ popup.currentLayerIndex + 1 }} of
            {{ getInfoResult.length }})</span
          >
          <v-icon
            :disabled="popup.currentLayerIndex === 0"
            style="cursor: pointer"
            @click="popup.currentLayerIndex -= 1"
            >chevron_left</v-icon
          >
          <v-icon
            :disabled="popup.currentLayerIndex === getInfoResult.length - 1"
            style="cursor: pointer"
            @click="popup.currentLayerIndex += 1"
            >chevron_right</v-icon
          >
        </template>
        <v-btn @click="closePopup()" icon>
          <v-icon small>fas fa-times</v-icon>
        </v-btn>
      </template>
      <template v-slot:body>
        <div class="subtitle-2 mb-4 font-weight-bold">
          {{
            getInfoResult[popup.currentLayerIndex]
              ? getInfoResult[popup.currentLayerIndex].get("layerName")
              : ""
          }}
        </div>

        <v-divider></v-divider>
        <span v-html="popup.rawHtml"></span>
        <div style="height: 190px">
          <vue-scroll>
            <v-simple-table dense class="pr-2">
              <template v-slot:default>
                <tbody>
                  <tr v-for="item in currentInfo" :key="item.property">
                    <td>{{ item.property }}</td>
                    <td>{{ item.value }}</td>
                  </tr>
                </tbody>
              </template>
            </v-simple-table>
          </vue-scroll>
        </div>

        <v-divider></v-divider>
      </template>
    </overlay-popup> -->
  </v-container>
</template>

<script>
import Vue from "vue";
import View from "ol/View";
import Map from "ol/Map";

//store imports
import { mapGetters, mapMutations } from "vuex";

//utils import
import { groupBy } from "@/utils/Helpers";
import { LayerFactory } from "@/factory/layer";

//ol import
import Mask from "ol-ext/filter/Mask";
import OlFill from "ol/style/Fill";
import { Group as LayerGroup } from "ol/layer";
import VectorSource from "ol/source/Vector";
import VectorLayer from "ol/source/Vector";
import Overlay from "ol/Overlay";
//import { Tile as TileLayer } from "ol/layer";
//import OSM from "ol/source/OSM";

//style imports
import OlStylesDefs from "@/style/OlStyleDefs";

// import the app-wide EventBus
import { EventBus } from "@/EventBus";

//map Control
import DoubleClickZoom from "ol/interaction/DoubleClickZoom";
// import OverlayPopup from "./controls/Overlay";

import { defaults as defaultControls, Attribution } from "ol/control";
import { defaults as defaultInteractions } from "ol/interaction";

export default {
  name: "app-ol-app",

  // components: {
  //   "overlay-popup": OverlayPopup,
  // },
  data() {
    return {
      zoom: this.$appConfig.map.zoom,
      center: this.$appConfig.map.center,
      maxZoom: this.$appConfig.maxZoom,
      minZoom: this.$appConfig.minZoom,
      extent: this.$appConfig.extent,
      allLayers: [],
      activeInteractions: [],
      popup: {
        rawHtml: null,
        title: "info",
        isVisible: false,
        currentLayerIndex: 0,
      },
      getInfoResult: [],
    };
  },
  mounted() {
    var me = this;
    Vue.prototype.$map = me.map;

    //Send the  event 'ol-map-mounted' ...

    EventBus.$emit("ol-map-mounted", me.map);

    //Add Map to the VueX store
    me.setMap(me.map);
    me.map.setTarget(document.getElementById("ol-map-container"));
    me.map.updateSize();

    //set up Map Hover;

    //setup map click

    //set up map pointer move

    //create popup Overlay
    //me.createPopupOverlay();
  },
  created() {
    console.log("created Map");
    var me = this;
    // make map rotateable according to property
    const attribution = new Attribution({
      collapsible: true,
    });

    //Need to reference as we should deactive double click zoom when there
    //are active interaction like draw/modify

    this.dblClickZoomInteraction = new DoubleClickZoom();

    me.map = new Map({
      layers: [],
      interactions: defaultInteractions({
        altShiftDragRotate: me.rotateableMap,
        doubleClickZoom: false,
      }).extend([this.dblClickZoomInteraction]),
      controls: defaultControls({
        attribution: false,
        zoom: false,
      }).extend([attribution]),
      view: new View({
        center: me.center || [0, 0],
        zoom: me.zoom,
        extent: me.extent,
        minZoom: me.minZoom,
        maxZoom: me.maxZoom,
      }),
    });

    //create Layers from config and add them to map

    const layers = me.createLayers();

    me.map.getLayers().extend(layers);
    //this.createMaskFilter(layers);
    // me.createGetInfoLayer();

    //
    EventBus.$on("ol-interaction-activated", (startedInteraction) => {
      me.activeInteractions.push(startedInteraction);
    });
    EventBus.$on("ol-interaction-stopped", (stoppedInteraction) => {
      me.activeInteractions = Array.from(new Set(me.activeInteractions));
      me.activeInteractions = me.activeInteractions.filter((interaction) => {
        return interaction !== stoppedInteraction;
      });
    });
  },
  methods: {
    ...mapMutations("map", {
      setMap: "SET_MAP",
    }),

    /**
     * Creates the OL layers due to the map "layers" array in app config.
     * @return {ol.layer.Base[]} Array of OL layer instances
     */
    createLayers() {
      let layers = [];
      const layersConfigGrouped = groupBy(this.$appConfig.map.layers, "group");
      for (var group in layersConfigGrouped) {
        if (!(group in layersConfigGrouped)) {
          continue;
        }

        const mapLayers = [];
        layersConfigGrouped[group].reverse().forEach((lConf) => {
          const layer = LayerFactory.getInstance(lConf);
          mapLayers.push(layer);
        });

        let layerGroup = new LayerGroup({
          name: group !== undefined ? group.toString() : "Other Layers",
          layers: mapLayers,
        });
        layers.push(layerGroup);
      }

      return layers;
    },
    createMaskFilter(mapLayers) {
      //filter background layers
      const backgroundLayers = [];
      mapLayers.forEach((layer) => {
        if (layer.get("name") === "backgroundLayers") {
          backgroundLayers.push(...layer.getLayers().getArray());
        }
      });

      //create masks

      const feature = this.$appConfig.map.studyAreaFeature;
      if (!feature[0]) return;

      const mask = new Mask({
        feature: feature[0],
        inner: false,
        fill: new OlFill({ color: [169, 169, 169, 0.8] }),
      });

      for (const i of backgroundLayers) {
        i.addFilter(mask);
      }
    },
    createGetInfoLayer() {
      const source = new VectorSource({
        wrapX: false,
      });

      const vector = new VectorLayer({
        name: "Get Info Layer",
        displayInLayerList: false,
        zIndex: 10,
        source: source,
        style: OlStylesDefs.getInfoStyle(),
      });
      this.getInfoLayer = source;
      this.map.addLayer(vector);
    },

    createPopupOverlay() {
      const me = this;
      me.popupOverlay = new Overlay({
        element: me.$refs.popup,
        autoPan: false,
        autoPanMargin: 40,
        autoPanAnimation: {
          duration: 250,
        },
      });
    },
    closePopup() {
      if (this.popupOverlay) {
        this.popupOverlay.setPosition(undefined);
        this.popup.isVisible = false;
      }
      this.getInfoResult = [];
      this.popup.currentLayerIndex = 0;
      if (this.getInfoLayerSource) {
        this.getInfoLayerSource.clear();
      }
    },

    /**
     * Show getInfo popup.
     */
    showPopup(coordinate) {
      this.map.getView().animate({
        center: coordinate,
        duration: 400,
      });
      this.popupOverlay.setPosition(coordinate);
      this.popup.isVisible = true;
      this.popup.title = `info`;
    },
  },
  computed: {
    // ...mapGetters("map", {
    //   helpTooltip: "helpTooltip",
    //   currentMessage: "currentMessage",
    // }),
  },
  watch: {
    activeInteractions() {
      if (!this.dblClickZoomInteraction) return;
      if (this.activeInteractions.length > 0) {
        this.dblClickZoomInteraction.setActive(true);
      } else {
        this.dblClickZoomInteraction.setActive(true);
      }
    },
  },
};
</script>

<style scoped>
#ol-map-container {
  height: calc(50vh - 25px);
}
</style>
