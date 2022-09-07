import OlStyleDefs from "@/style/OlStyleDefs";
import Feature from "ol/Feature";
import { LineString } from "ol/geom";
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
      }

      let feature = new Feature({
        geometry: geometry,
      });

      feature.setProperties(item.properties);

      feature.getGeometry().transform("EPSG:4326", "EPSG:3857");

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
  addFeaturesToSource2: (layer, list) => {
    const source = layer.getSource();
    let features = [];

    if (list.length > 0) {
      source.clear();
      // tao feature to layer

      list.forEach((item) => {
        item.features.forEach((f) => {
          let feature = editLayerHelper.createFeature(f);
          // if (item.style === undefined)
          //   item.style = OlStyleDefs.getDieuHanhStyle();
          if (!!feature) {
            feature.setStyle(item.style);

            features.push(feature);
          }
        });
        //  let feature = editLayerHelper.createFeature(item);
        //  feature.setStyle(style);
        //  source.addFeature(feature);
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
      if (feature.getId() === item.id) {
        source.removeFeature(feature);
      }
    });
  },

  zoomToPoint: (viewMap, item, zoom) => {
    viewMap.animate({
      zoom: zoom,
      duration: 500,
      center: transform(item.geometry.coordinates, "EPSG:4326", "EPSG:3857"),
    });
  },
};

export default editLayerHelper;
