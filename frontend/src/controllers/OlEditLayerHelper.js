import OlStyleDefs from "@/style/OlStyleDefs";
import Feature from "ol/Feature";
import { LineString, Polygon } from "ol/geom";
import Point from "ol/geom/Point";
import { transform } from "ol/proj.js";
import { Style, Stroke, Icon, Circle as CircleStyle, Fill } from "ol/style";

import FontSymbol from "ol-ext/style/FontSymbol";
import { Vector as VectorSource } from "ol/source";
import { Vector as VectorLayer } from "ol/layer";
import { getVectorContext } from "ol/render";

const editLayerHelper = {
  selectedLayer: null,
  deletedFeatured: [],

  createFeature: (item) => {
    let geometry;
    if (!!item.geometry) {
      switch (item.geometry.type) {
        case "Point":
          geometry = new Point(item.geometry.coordinates);
          break;
        case "LineString":
          geometry = new LineString(item.geometry.coordinates);
          break;
        case "Polygon":
          geometry = new Polygon(item.geometry.coordinates);
          break;
      }

      let feature = new Feature({
        geometry: geometry,
      });

      if (item.properties) {
        feature.setProperties(item.properties);
      }

      feature.getGeometry().transform("EPSG:4756", "EPSG:3857");

      return feature;
    }
    return null;
  },

  addFeaturesToSource: (layer, list, style) => {
    if (style === undefined) style = OlStyleDefs.getDieuHanhStyle();
    const source = layer.getSource();

    // layer.setStyle(style);

    if (list.length > 0) {
      source.clear();
      // tao feature to layer

      list.forEach((item) => {
        let feature = editLayerHelper.createFeature(item);
        feature.setStyle(style);
        source.addFeature(feature);
      });
    }
  },
  addFeaturesToSource2(layer, list) {
    const me = this;
    const source = layer.getSource();
    let features = [];
    let style;

    if (list.length > 0) {
      source.clear();
      // tao feature to layer

      list.forEach((item) => {
        item.features.forEach((f) => {
          if (item.style === "pa") {
            style =
              f.geometry.type === "LineString"
                ? OlStyleDefs.getArrowStyle(f)
                : OlStyleDefs.getPAViTriStyle(f);
          } else if (item.style === "nvdh") {
            style =
              f.geometry.type === "LineString"
                ? OlStyleDefs.getArrowDieuHanhStyle()
                : OlStyleDefs.getDieuHanhStyle(f);
          } else {
            style = OlStyleDefs.getDieuHanhStyle();
          }

          let feature = editLayerHelper.createFeature(f);
          if (!!feature) {
            feature.setStyle(style);

            features.push(feature);
          }
        });
      });

      source.addFeatures(features);
    }
  },

  addFeatureToSource: (layer, item) => {
    const newFeature = editLayerHelper.createFeature(item);

    layer.getSource().addFeature(newFeature);
  },

  removeFeatureFromSource: (layer, item) => {
    const source = layer.getSource();

    source.forEachFeature((feature) => {
      // if (feature.getId() === item.id) {
      //   source.removeFeature(feature);
      // }
    });
  },

  zoomToPoint: (viewMap, item, zoom) => {
    viewMap.animate({
      zoom: zoom,
      duration: 500,
      center: transform(item.geometry.coordinates, "EPSG:4756", "EPSG:3857"),
    });
  },

  startSimulation(map, polyline) {
    var route = new LineString(polyline.geometry.coordinates).transform(
      "EPSG:4756",
      "EPSG:3857"
    );
    console.log(route);
    const routeFeature = new Feature({
      type: "route",
      geometry: route,
    });
    const startMarker = new Feature({
      type: "icon",
      geometry: new Point(route.getFirstCoordinate()),
    });
    const endMarker = new Feature({
      type: "icon",
      geometry: new Point(route.getLastCoordinate()),
    });
    const position = startMarker.getGeometry().clone();
    const geoMarker = new Feature({
      type: "geoMarker",
      geometry: position,
    });
    const styles = {
      route: new Style({
        stroke: new Stroke({
          width: 6,
          color: [255, 0, 0, 0.2],
        }),
      }),
      icon: new Style({
        image: new Icon({
          anchor: [0.5, 1],
          src: "https://openlayers.org/en/latest/examples/data/icon.png",
        }),
      }),
      geoMarker: new Style({
        image: new FontSymbol({
          form: "marker",

          radius: 15,
          offsetY: -15,
          fontSize: 0.7,
          color: "#fff",
          fill: new Fill({
            color: "blue",
          }),
          stroke: new Stroke({
            color: "#fff",
            width: 2,
          }),
        }),
        stroke: new Stroke({
          width: 5,
          color: "#f00",
        }),
        fill: new Fill({
          color: [255, 0, 0, 0.6],
        }),
      }),
    };
    const vectorLayer = new VectorLayer({
      source: new VectorSource({
        features: [routeFeature, geoMarker],
      }),
      style: function (feature) {
        return styles[feature.get("type")];
      },
      zIndex: 99,
    });
    map.addLayer(vectorLayer);

    const speedInput = 20;
    // const startButton = document.getElementById("start-animation");
    // let animating = false;
    let distance = 0;
    let lastTime;

    function moveFeature(event) {
      const speed = Number(speedInput);
      const time = event.frameState.time;
      const elapsedTime = time - lastTime;
      distance = (distance + (speed * elapsedTime) / 1e6) % 2;
      lastTime = time;

      const currentCoordinate = route.getCoordinateAt(
        distance > 1 ? 2 - distance : distance
      );
      position.setCoordinates(currentCoordinate);
      const vectorContext = getVectorContext(event);
      vectorContext.setStyle(styles.geoMarker);
      vectorContext.drawGeometry(position);
      // tell OpenLayers to continue the postrender animation
      map.render();
    }

    function startAnimation() {
      // animating = true;
      lastTime = Date.now();
      // startButton.textContent = "Stop Animation";
      vectorLayer.on("postrender", moveFeature);
      // hide geoMarker and trigger map render through change event
      geoMarker.setGeometry(null);
    }

    startAnimation();
  },
};

export default editLayerHelper;
