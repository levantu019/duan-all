import OlStyleDefs from "@/style/OlStyleDefs";
import Feature from "ol/Feature";
import Point from "ol/geom/Point";
import { transform } from "ol/proj.js";

const editLayerHelper = {
  selectedLayer: null,
  deletedFeatured: [],

  addFeaturesToSource: (layer, list) => {
    const style = OlStyleDefs.getPointDiemDieuHanhStyle();
    const source = layer.getSource();

    source.clear();

    layer.setStyle(style);

    if (list.length > 0) {
      source.clear();
      // tao feature to layer

      list.forEach((item) => {
        let feature = new Feature({
          geometry: new Point(item.geometry.coordinates),
        });

        feature.setProperties(item.properties);
        feature.setId(item.id);

        feature.getGeometry().transform("EPSG:4326", "EPSG:3857");

        source.addFeature(feature);
      });
    }
  },

  addFeatureToSource: (layer, item) => {
    const newFeature = new Feature({
      geometry: new Point(item.geometry.coordinates),
    });

    newFeature.setId(item.id);
    newFeature.setProperties(item.properties);

    newFeature.getGeometry().transform("EPSG:4326", "EPSG:3857");

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
