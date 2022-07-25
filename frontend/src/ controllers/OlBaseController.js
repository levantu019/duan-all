import VectorSource from "ol/source/Vector";
import VectorLayer from "ol/layer/Vector";
import Overlay from "ol/Overlay.js";
import { Circle as CircleStyle, Fill, Stroke, Style } from "ol/style";

export default class OlBaseController {
  /**
   * The tooltip element.
   * @type {Element}
   */
  tooltipElement;

  /**
   * Overlay to show the measurement.
   * @type {module:ol/Overlay}
   */
  tooltip;

  /**
   * The help tooltip element.
   * @type {Element}
   */
  helpTooltipElement;

  /**
   * Overlay to show help tooltip message.
   * @type {module:ol/Overlay}
   */
  helpTooltip;

  /**
   * Overlay objects to be removed on map clear.
   * @type {module:ol/Overlay []}
   */
  overlayersGarbageCollector = [];

  constructor(map) {
    Object.assign(this, { map });
  }

  /**
   * Creates a vector layer and adds it to the
   * map.
   */
  createLayer(name, style, opt = {}) {
    const me = this;
    // create a vector layer
    const source = new VectorSource({
      wrapX: false,
    });
    const options = Object.assign(opt, {
      name: name,
      displayInLayerList: false,
      zIndex: 3,
      source: source,
      style: new Style({
        fill: new Fill({
          color: "rgba(255, 255, 255, 0.2)",
        }),
        stroke: new Stroke({
          color: "#ffcc33",
          width: 2,
        }),
        image: new CircleStyle({
          radius: 7,
          fill: new Fill({
            color: "#ffcc33",
          }),
        }),
      }),
    });

    const vector = new VectorLayer(options);

    me.map.addLayer(vector);

    // make vector source available as member
    me.source = source;
    me.layer = vector;
  }

  /**
   * Get layer source
   */
  getLayerSource() {
    const me = this;
    return me.source;
  }

  getMap() {
    const me = this;
    return me.map;
  }

  /**
   * Creates a value tooltip
   */
  createTooltip() {
    const me = this;
    if (me.tooltipElement) {
      me.tooltipElement.parentNode.removeChild(me.tooltipElement);
    }
    me.tooltipElement = document.createElement("div");
    me.tooltipElement.className = "tooltip tooltip-measure";
    me.tooltip = new Overlay({
      element: me.tooltipElement,
      offset: [0, -22],
      positioning: "bottom-center",
    });
    me.map.addOverlay(me.tooltip);
    me.overlayersGarbageCollector.push(me.tooltip);
  }

  /**
   * Creates a help tooltip
   */

  createHelpTooltip() {
    const me = this;
    if (me.helpTooltipElement) {
      me.helpTooltipElement.parentNode.removeChild(me.helpTooltipElement);
    }
    me.helpTooltipElement = document.createElement("div");
    me.helpTooltipElement.className = "tooltip";
    me.helpTooltip = new Overlay({
      element: me.helpTooltipElement,
      offset: [15, 15],
      positioning: "top-left",
      stopEvent: true,
      insertFirst: false,
    });
    me.map.addOverlay(me.helpTooltip);
    me.overlayersGarbageCollector.push(me.helpTooltip);
  }

  clearOverlays() {
    const me = this;
    if (me.overlayersGarbageCollector) {
      me.overlayersGarbageCollector.forEach((overlay) => {
        me.map.removeOverlay(overlay);
      });
      me.overlayersGarbageCollector = [];
    }
  }

  /**
   * Removes the current interaction and clears the values.
   */
  clear() {
    const me = this;
    if (me.removeInteraction) {
      me.removeInteraction();
    }
    if (me.source) {
      me.source.clear();
    }
    me.clearOverlays();
  }
}
