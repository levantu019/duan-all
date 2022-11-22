import { Group as LayerGroup } from "ol/layer";
import olLayerImage from "ol/layer/Image.js";
import olLayerTile from "ol/layer/Tile";
import olLayerVector from "ol/layer/Vector.js";

/**
 * Returns all map layers excluding from group layer
 *
 * @param  {ol.Map} olMap  The OL map to search in
 * @return {ol.layer.Base[]} Array of all map layers
 */
export function getAllChildLayers(olMap) {
  const allLayers = [];
  olMap
    .getLayers()
    .getArray()
    .forEach((layer) => {
      if (layer instanceof LayerGroup) {
        const layers = layer.getLayers().getArray();
        allLayers.push(...layers);
      } else {
        allLayers.push(layer);
      }
    });
  return allLayers;
}

/**
 * Returns OL Layer type.
 *
 * @param  {ol.layer.Base} Object OL layer
 */
export function getLayerType(layer) {
  let layerType;
  if (layer instanceof olLayerImage || layer instanceof olLayerTile) {
    layerType = "WMS";
  } else if (layer instanceof olLayerVector) {
    layerType = "WFS";
  }
  return layerType;
}
