import OlStyleDefs from "@/style/OlStyleDefs";
import Feature from "ol/Feature";
import { LineString, Polygon } from "ol/geom";
import Point from "ol/geom/Point";
import { transform } from "ol/proj.js";

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
};

export default editLayerHelper;
