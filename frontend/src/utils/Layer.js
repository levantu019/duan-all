import { Group as LayerGroup } from "ol/layer";

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
