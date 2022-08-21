import { Overlay } from "ol";
import { unByKey } from "ol/Observable";
import { Modify, Draw, Snap } from "ol/interaction";
import OlBaseController from "./OlBaseController";
import editLayerHelper from "./OlEditLayerHelper";
import OlStyleDefs from "@/style/OlStyleDefs";

// import VectorSource from "ol/source/Vector";
// import VectorLayer from "ol/layer/Vector";

export default class OlEditController extends OlBaseController {
  featuresToCommit = [];

  constructor(map) {
    super(map);
  }

  /**
   * Creates the edit vector layer and add it to the
   * map.
   */
  createEditLayer(onFeatureChangeCb, onSourceChangeCb) {
    const me = this;
    const style = OlStyleDefs.defaultStyle();
    super.createLayer("Edit Layer", style, {
      queryable: true,
    });
    me.source.on("changefeature", onFeatureChangeCb);
    me.source.on("change", onSourceChangeCb);

    //Create highlight layer
    //    const highlightSource = new VectorSource({ wrapX: false });
    //  const highlightLayer = new VectorLayer({
    //displayInLayerList: false,
    //  source: highlightSource,
    // zIndex: 10,
    //style: OlStyleDefs.getFeatureHighlightStyle(),
    //});
    //me.map.addLayer(highlightLayer);
    //me.highlightSource = highlightSource;
  }

  createModifyLayer(item) {
    const me = this;
    const style = OlStyleDefs.defaultStyle();
    super.createLayer("Modify Layer", style, {
      queryable: true,
    });

    const modifyFeature = editLayerHelper.createFeature(item);

    me.source.addFeature(modifyFeature);
  }

  /**
   * Creates the edit interaction and adds it to the map.
   */
  addInteraction(editType, startCb, endCb, item = null) {
    const me = this;

    me.removeInteraction();
    // me.createHelpTooltip();

    // me.pointerMoveKey = me.map.on("pointermove", me.onPointerMove.bind(me));

    //me.createPopupOverlay();

    switch (editType) {
      case "add": {
        let geometryType = editLayerHelper.selectedLayer.get("editGeometry");

        me.edit = new Draw({
          source: me.source,
          type: geometryType,
        });

        me.edit.on("drawstart", startCb);
        me.edit.on("drawend", endCb);

        me.snap = new Snap({ source: me.source });
        me.currentInteraction = "draw";

        //i18n.t

        break;
      }
      case "modify": {
        const featureModify = editLayerHelper.createFeature(item);

        me.source.addFeature(featureModify);

        me.edit = new Modify({ source: me.source });
        me.edit.on("modifystart", startCb);
        me.edit.on("modifyend", endCb);
        me.snap = new Snap({ source: me.source });
        me.currentInteraction = "modify";
        break;
      }
      default:
        break;
    }

    if (me.edit) {
      me.map.addInteraction(me.edit);
    }

    if (me.snap) {
      me.map.addInteraction(me.snap);
    }
  }

  /**
   * Removes the current edit interaction.
   */

  removeInteraction() {
    const me = this;
    me.featuresToCommit = [];
    me.currentInteraction = "";
    // me.closePopup();

    if (me.edit) {
      me.map.removeInteraction(me.edit);
      me.edit = null;
    }

    if (me.snap) {
      me.map.removeInteraction(me.snap);
    }

    // if (me.deleteFeatureListener) {
    //   unByKey(me.deleteFeatureListener);
    // }
    // if (me.selectedFeature) {
    // me.selectedFeature = null;
    // }
    // if (me.pointerMoveKey) {
    //   unByKey(me.pointerMoveKey);
    // }
    // if (me.clearOverlays) {
    //   me.clearOverlays();
    // }
  }

  /**
   * Closes the popup if user choose cancel.
   */
  // closePopup() {
  //   const me = this;
  //   if (me.popupOverlay) {
  //     me.popupOverlay.setPosition(undefined);
  //     me.popup.isVisible = false;
  //   }
  //   if (me.edit) {
  //     me.edit.setActive(true);
  //   }

  //   me.highlightSource.clear();
  // }

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

  /**
   * Show popup when user deletes or draws a feature.
   */
  createPopupOverlay() {
    const me = this;
    me.popupOverlay = new Overlay({
      element: me.popup.el.$el,
      autoPan: true,
      autoPanMargin: 40,
      autoPanAnimation: {
        duration: 250,
      },
    });
    me.map.addOverlay(me.popupOverlay);
    me.overlayersGarbageCollector.push(me.popupOverlay);
  }

  clear() {
    // if (this.highlightSource) {
    //   this.highlightSource.clear();
    // }

    const me = this;

    if (this.removeInteraction) {
      this.removeInteraction();
    }

    //clear Overlay

    //super.clearOverlays();

    me.source.getFeatures().forEach((f) => {
      // const props = f.getProperties();

      //check condition

      this.source.removeFeature(f);
    });
  }

  removeLayerEdit() {
    this.map.removeLayer(this.layer);
  }
}
