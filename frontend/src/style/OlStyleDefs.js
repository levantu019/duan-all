import OlStyle from "ol/style/Style";
import OlStroke from "ol/style/Stroke";
import OlFill from "ol/style/Fill";
import Text from "ol/style/Text";
import OlCircle from "ol/style/Circle";
import OlIcon from "ol/style/Icon";
//import store from "../store/modules/isochrones";
import LineString from "ol/geom/LineString";
import Icon from "ol/style/Icon";
import ol_style_FlowLine from "ol-ext/style/FlowLine";

//const colorDiffDefault = [6.1, 13.42, 11.789];
//const color1Default = [255, 255, 224];
// const colorDiffInput = [1.789, 10.578, -9.631];
// const color1Input = [34, 211, 41];

// function setNetworkColor(time, colorDiff, color1) {
//   let color;
//   if (time < 1) {
//     color = color1;
//   } else {
//     let diffTime = time - 1;
//     color = [
//       color1[0] - colorDiff[0] * diffTime,
//       color1[1] - colorDiff[1] * diffTime,
//       color1[2] - colorDiff[2] * diffTime,
//     ];
//   }
//   return color;
// }

const OlStyleDefs = {
  boundaryStyle: () => {
    return new OlStyle({
      fill: new OlFill({
        color: [0, 0, 0, 0],
      }),
      stroke: new OlStroke({
        color: "#707070",
        width: 5.5,
      }),
    });
  },
  getMeasureStyle: (measureConf) => {
    return new OlStyle({
      fill: new OlFill({
        color: measureConf.fillColor || "rgba(255, 255, 255, 0.2)",
      }),
      stroke: new OlStroke({
        color: measureConf.strokeColor || "rgba(0, 0, 0, 0.5)",
        width: 4,
      }),
    });
  },
  getMeasureInteractionStyle: (measureConf) => {
    return new OlStyle({
      fill: new OlFill({
        color: measureConf.sketchFillColor || "rgba(255, 255, 255, 0.2)",
      }),
      stroke: new OlStroke({
        color: measureConf.sketchStrokeColor || "rgba(0, 0, 0, 0.5)",
        lineDash: [10, 10],
        width: 2,
      }),
      image: new OlCircle({
        radius: 5,
        stroke: new OlStroke({
          color: measureConf.sketchVertexStrokeColor || "rgba(0, 0, 0, 0.7)",
        }),
        fill: new OlFill({
          color:
            measureConf.sketchVertexFillColor || "rgba(255, 255, 255, 0.2)",
        }),
      }),
    });
  },
  getSelectStyle: () => {
    return new OlStyle({
      fill: new OlFill({
        color: [0, 0, 0, 0],
      }),
      stroke: new OlStroke({
        color: "#fe4a49",
        width: 5,
        lineDash: [10, 10],
      }),
      image: new OlCircle({
        radius: 7,
        fill: new OlFill({
          color: "#FF0000",
        }),
      }),
    });
  },
  getInfoStyle: () => {
    return new OlStyle({
      fill: new OlFill({
        color: "rgba(255,0,0, 0.2)",
      }),
      stroke: new OlStroke({
        color: "#FF0000",
        width: 2,
      }),
      image: new OlCircle({
        radius: 7,
        fill: new OlFill({
          color: "#FF0000",
        }),
      }),
    });
  },
  getEditStyle: () => {
    //TODO: Add a generic style here for other layers
    return OlStyleDefs.editStyleFn();
  },
  getIsochroneStyle: (styleData, addStyleInCache) => {
    const styleFunction = (feature) => {
      // Style array
      let styles = [];
      // Get the incomeLevel and modus from the feature properties
      let level = feature.get("step");
      let modus = feature.get("modus");
      let isVisible = feature.get("isVisible");
      let geomType = feature.getGeometry().getType();
      const color = feature.get("color");
      const highlightFeature = feature.get("highlightFeature");

      /**
       * Creates styles for isochrone polygon geometry type and isochrone
       * center marker.
       */
      if (
        geomType === "Polygon" ||
        geomType === "MultiPolygon" ||
        geomType === "LineString"
      ) {
        //Check feature isVisible Property
        if (isVisible === false) {
          return;
        }

        //Fallback isochrone style
        if (!modus) {
          if (!styleData.styleCache.default["GenericIsochroneStyle"]) {
            let genericIsochroneStyle = new OlStyle({
              fill: new OlFill({
                color: [0, 0, 0, 0],
              }),
              stroke: new OlStroke({
                color: "#0d0d0d",
                width: 7,
              }),
            });
            let payload = {
              style: genericIsochroneStyle,
              isochroneType: "default",
              styleName: "GenericIsochroneStyle",
            };
            addStyleInCache(payload);
          }
          styles.push(styleData.styleCache.default["GenericIsochroneStyle"]);
        }
        //highlight color
        if (highlightFeature !== false) {
          styles.push(
            new OlStyle({
              stroke: new OlStroke({
                color: "#FFFFFF",
                width: 8,
              }),
            })
          );
        }
        // If the modus is 1 it is a default isochrone
        if (modus === 1 || modus === 3) {
          if (
            !styleData.styleCache.default[level] ||
            styleData.styleCache.default[level].getStroke().getColor() !== color //Updates default cache when user has changed the color
          ) {
            let style = new OlStyle({
              fill: new OlFill({
                color: [0, 0, 0, 0],
              }),
              stroke: new OlStroke({
                color: feature.get("color"),
                width: 5,
              }),
            });
            let payload = {
              style: style,
              isochroneType: "default",
              styleName: level,
            };
            addStyleInCache(payload);
          }
          styles.push(styleData.styleCache.default[level]);
        } else {
          if (
            !styleData.styleCache.input[level] ||
            styleData.styleCache.input[level].getStroke().getColor() !== color //Updates input cache when user has changed the color
          ) {
            let style = new OlStyle({
              fill: new OlFill({
                color: [0, 0, 0, 0],
              }),
              stroke: new OlStroke({
                color: feature.get("color"),
                width: 5,
              }),
            });
            let payload = {
              style: style,
              isochroneType: "input",
              styleName: level,
            };
            addStyleInCache(payload);
          }
          styles.push(styleData.styleCache.input[level]);
        }
      } else {
        let path = `img/markers/marker-${feature.get("calculationNumber")}.png`;
        let markerStyle = new OlStyle({
          image: new OlIcon({
            anchor: [0.5, 0.96],
            src: path,
            scale: 0.5,
          }),
        });
        styles.push(markerStyle);
      }
      return styles;
    };

    return styleFunction;
  },
  // getIsochroneNetworkStyle: () => {
  //   const styleFunction = (feature) => {
  //     const modus = feature.get("modus");
  //     const level = feature.get("cost");
  //     let speed = store.state.options.speed * 16.6666667;
  //     let color;
  //     if (modus == 1 || modus == 3) {
  //       color = setNetworkColor(level / speed, colorDiffDefault, color1Default);
  //     } //If the parent_id is not one it is a input isochrone
  //     else {
  //       color = setNetworkColor(level / speed, colorDiffInput, color1Input);
  //     }

  //     const style = new OlStyle({
  //       stroke: new OlStroke({
  //         color: `rgb(${Math.round(color[0])},${Math.round(
  //           color[1]
  //         )},${Math.round(color[2])})`,
  //         width: 3,
  //       }),
  //     });

  //     return [style];
  //   };
  //   return styleFunction;
  // },

  defaultStyle: () => {
    const style = new OlStyle({
      fill: new OlFill({
        color: [0, 0, 0, 0],
      }),
      stroke: new OlStroke({
        color: "#707070",
        width: 3,
      }),
      image: new OlCircle({
        radius: 7,
        fill: new OlFill({
          color: "#FF0000",
        }),
      }),
    });
    return [style];
  },
  uploadedFeaturesStyle: () => {
    const style = new OlStyle({
      fill: new OlFill({
        color: "#2196F3",
      }),
      stroke: new OlStroke({
        color: "#2196F3",
        width: 3,
      }),
      image: new OlCircle({
        radius: 7,
        fill: new OlFill({
          color: "#2196F3",
        }),
      }),
    });
    return [style];
  },
  waysModifiedStyle: (feature) => {
    const style = new OlStyle({
      fill: new OlFill({
        color: [0, 0, 0, 0],
      }),
      stroke: new OlStroke({
        color: "#FF0000",
        width: 3,
        lineDash: feature.getProperties()["status"] == 1 ? [0, 0] : [10, 10],
      }),
      image: new OlCircle({
        radius: 7,
        fill: new OlFill({
          color: "#FF0000",
        }),
      }),
    });
    return [style];
  },
  waysNewRoadStyle: (feature) => {
    const style = new OlStyle({
      fill: new OlFill({
        color: [0, 0, 0, 0],
      }),
      stroke: new OlStroke({
        color: "#6495ED",
        width: 4,
        lineDash: feature.getProperties()["status"] == 1 ? [0, 0] : [10, 10],
      }),
    });
    return [style];
  },
  waysNewBridgeStyle: (feature) => {
    const style = new OlStyle({
      fill: new OlFill({
        color: [0, 0, 0, 0],
      }),
      stroke: new OlStroke({
        color: "#FFA500",
        width: 4,
        lineDash: feature.getProperties()["status"] == 1 ? [0, 0] : [10, 10],
      }),
    });
    return [style];
  },
  editStyleFn: () => {
    const me = OlStyleDefs;
    const styleFunction = (feature) => {
      const props = feature.getProperties();
      if (feature.get("user_uploaded")) {
        return me.uploadedFeaturesStyle();
      }

      if (
        (props["type"] && props["original_id"] == null) ||
        Object.keys(props).length == 1
      ) {
        //Distinguish Roads from Bridge features
        if (props.type == "bridge") {
          return me.waysNewBridgeStyle(feature);
        } else {
          return me.waysNewRoadStyle(feature);
        }
      } else if (props["type"]) {
        return me.waysModifiedStyle(feature); //Feature are modified
      } else {
        return me.defaultStyle(); //Features are from original table
      }
    };

    return styleFunction;
  },
  getFeatureHighlightStyle: () => {
    return [
      new OlStyle({
        fill: new OlFill({
          color: "#00E8B3",
        }),
        stroke: new OlStroke({
          color: "#FF0000",
          width: 1,
        }),
        image: new OlIcon({
          src: "/img/pointActive.png",
          anchor: [0.5, 1],
        }),
      }),
    ];
  },
  getMissionStyle: () => {
    const styleFunction = (feature) => {
      // Style array
      let styles = [];
      // Get the incomeLevel and modus from the feature properties
      let geometry = feature.getGeometry();
      let type = feature.get("type");
      if (type === "Participation") {
        let path = `img/missions/${feature.get("icon")}.png`;
        let markerStyle = new OlStyle({
          image: new OlIcon({
            anchor: [0.5, 0.5],
            src: path,
            scale: 1,
          }),
        });
        styles.push(markerStyle);
      } else {
        let geomType = feature.get("geotype");
        const color = feature.get("color");
        const style = new OlStyle({
          fill: new OlFill({
            color: color,
          }),
          stroke: new OlStroke({
            color: color,
            width: 3,
          }),
          image: new OlCircle({
            radius: 7,
            fill: new OlFill({
              color: color,
            }),
          }),
        });
        styles.push(style);
        if (geomType === "arrow") {
          geometry.forEachSegment(function (start, end) {
            var dx = end[0] - start[0];
            var dy = end[1] - start[1];
            var rotation = Math.atan2(dy, dx);
            // arrows
            var lineStr1 = new LineString([end, [end[0] - 3, end[1] + 3]]);
            lineStr1.rotate(rotation + 0.5, end);
            var lineStr2 = new LineString([end, [end[0] - 3, end[1] - 3]]);
            lineStr2.rotate(rotation - 0.5, end);

            var stroke = new OlStroke({
              color: color,
              width: 4,
            });

            styles.push(
              new OlStyle({
                geometry: lineStr1,
                stroke: stroke,
              })
            );
            styles.push(
              new OlStyle({
                geometry: lineStr2,
                stroke: stroke,
              })
            );
            /*
    	styles.push(new OlStyle({
      		geometry: new Point(end),
      		image: new OlIcon({
        		src: 'img/missions/arrow.png',
        		anchor: [0.75, 0.5],
        		rotateWithView: true,
        		rotation: -rotation
      		})
    	})); */
          });
        }
      }
      return styles;
    };

    return styleFunction;
  },
  getMissionPlanStyle: () => {
    const styleFunction = (feature) => {
      // Style array
      let styles = [];
      // Get the incomeLevel and modus from the feature properties
      let isVisible = feature.get("isVisible");
      let geometry = feature.getGeometry();
      let type = feature.get("type");
      if (type === "Force") {
        if (isVisible) {
          let dy = feature.get("dy");
          let dx = feature.get("dx");
          let rotation = Math.atan2(dy, dx);
          let path = `img/missions/${feature.get("icon")}.png`;
          let markerStyle = new OlStyle({
            image: new OlIcon({
              anchor: [0.5, 0.5],
              anchorXUnits: "fraction",
              anchorYUnits: "fraction",
              rotation: -rotation,
              src: path,
              scale: 1,
            }),
            text: new Text({
              font: "12px Calibri,sans-serif",
              fill: new OlFill({ color: "#000000" }),
              stroke: new OlStroke({
                color: "#FFFFFF",
                width: 2,
              }),
              offsetY: 20,
              text: feature.get("name"),
            }),
          });
          styles.push(markerStyle);
        }
      } else {
        let geomType = feature.get("geotype");
        const color = feature.get("color");
        const style = new OlStyle({
          fill: new OlFill({
            color: color,
          }),
          stroke: new OlStroke({
            color: color,
            width: 3,
          }),
          image: new OlCircle({
            radius: 7,
            fill: new OlFill({
              color: color,
            }),
          }),
        });
        styles.push(style);
        if (geomType === "arrow") {
          geometry.forEachSegment(function (start, end) {
            var dx = end[0] - start[0];
            var dy = end[1] - start[1];
            var rotation = Math.atan2(dy, dx);
            // arrows
            var lineStr1 = new LineString([end, [end[0] - 3, end[1] + 3]]);
            lineStr1.rotate(rotation + 0.5, end);
            var lineStr2 = new LineString([end, [end[0] - 3, end[1] - 3]]);
            lineStr2.rotate(rotation - 0.5, end);

            var stroke = new OlStroke({
              color: color,
              width: 4,
            });

            styles.push(
              new OlStyle({
                geometry: lineStr1,
                stroke: stroke,
              })
            );
            styles.push(
              new OlStyle({
                geometry: lineStr2,
                stroke: stroke,
              })
            );
            /*
    	styles.push(new OlStyle({
      		geometry: new Point(end),
      		image: new OlIcon({
        		src: 'img/missions/arrow.png',
        		anchor: [0.75, 0.5],
        		rotateWithView: true,
        		rotation: -rotation
      		})
    	})); */
          });
        }
      }
      return styles;
    };
    return styleFunction;
  },
  getDieuHanhStyle() {
    return new OlStyle({
      image: new OlIcon({
        color: "#FFD700",
        src: "/img/city-hall.png",
        anchor: [0.5, 46],
        anchorXUnits: "fraction",
        anchorYUnits: "pixels",
        scale: 0.8,
      }),
      stroke: new OlStroke({
        color: "#00FFFF",
        width: 3,
      }),
      fill: new OlFill({
        color: "rgba(0, 0, 255, 0.1)",
      }),
    });
  },
  getPAViTriStyle(pa) {
    let src = "/img/embassy.svg";
    let color, lineDash;
    if (!!pa) {
      color = !pa["properties"].pheDuyet ? "#FF0000" : "#32CD32";

      //select symbol for type pa
      switch (pa["properties"].kieuPAVT) {
        case 1:
          src = "/img/congtrinh.png";
          break;
        case 2:
          src = "/img/flag.png";
          break;
        case 3:
          src = "/img/flag-end.png";
          break;
      }

      switch (pa["properties"].kieuPATuyen) {
        case 1:
          lineDash = [];
          break;
        case 2:
          lineDash = [5, 5];
          break;
        default:
          lineDash = [];
      }
    }

    return new OlStyle({
      image: new OlIcon({
        color: color,
        src: src,
        anchor: [0.5, 46],
        anchorXUnits: "fraction",
        anchorYUnits: "pixels",
        scale: 0.75,
      }),
      stroke: new OlStroke({
        color: color,
        width: 2,
        lineDash: lineDash,
      }),
      fill: new OlFill({
        color: "rgba(255, 0, 0, 0.1)",
      }),
    });
  },
  getPDPAViTriStyle() {
    return new OlStyle({
      image: new OlCircle({
        radius: 8,
        fill: new OlFill({
          color: "#009dff",
        }),
      }),
      stroke: new OlStroke({
        color: "#009dff",
        width: 2,
      }),
      fill: new OlFill({
        color: "rgba(0, 0, 255, 0.1)",
      }),
    });
  },
  getDrawDefaultStyle() {
    return new OlStyle({
      fill: new OlFill({
        color: "rgba(255, 255, 255, 0.2)",
      }),
      stroke: new OlStroke({
        color: "#ffcc33",
        width: 2,
      }),
      image: new OlCircle({
        radius: 7,
        fill: new OlFill({
          color: "#ffcc33",
        }),
      }),
    });
  },

  getArrowStyle(f) {
    let color1 = "#FFFFFF";
    let color2 = "#FFFF00";

    if (!!f) {
      color2 = !f["properties"].pheDuyet ? "#FF0000" : "#32CD32";
    }

    return new ol_style_FlowLine({
      color: color1,
      color2: color2,
      width: 20,
      width2: 7,
      arrow: 1,
    });
  },
  getArrowDieuHanhStyle() {
    let color1 = "#FFFFFF";
    let color2 = "#00FFFF";

    return new ol_style_FlowLine({
      color: color1,
      color2: color2,
      width: 20,
      width2: 7,
      arrow: 1,
    });
  },

  getDrawArrowStyle(feature, res) {
    /* ol < 7 need a style to make the feature selectable
    return [ defaultStyle, flowStyle ];
    */
    return new ol_style_FlowLine({
      color: "#FF0000",
      color2: "#FFFF00",
      width: 20,
      width2: 7,
      arrow: 1,
    });
  },
};

export default OlStyleDefs;
