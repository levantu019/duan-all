import Vue from "vue";
import App from "./App.vue";
import vuetify from "./plugins/vuetify";
import router from "./router";
import VueSplit from "vue-split-panel";
import store from "./store";
import UrlUtil from "./utils/Url";
import axios from "axios";

import VueSocketIO from "vue-socket.io";
import SocketIO from "socket.io-client";

require("../node_modules/ol/ol.css");

Vue.config.productionTip = false;

Vue.use(VueSplit);

const appEl = document.querySelector("#app");
Vue.prototype.$isEmbedded = appEl.hasAttribute("embedded");

/* Establish Connection */
const socketConnection = SocketIO("http://localhost:3004");

Vue.use(
  new VueSocketIO({
    debug: true,
    connection: socketConnection,
  })
);

// Detect an URL parameter for a custom app context
const appCtx = UrlUtil.getQueryParam("appCtx");
let appCtxFile = "";
if (appCtx) {
  // simple approach to avoid path traversal
  appCtxFile = "-" + appCtx.replace(/(\.\.[/])+/g, "");
}

if (Vue.config.productionTip) appCtxFile = ".production";

function getAppConf() {
  return axios.get("/static/app-conf" + appCtxFile + ".json");
}

axios.all([getAppConf()]).then(
  axios.spread(function (config) {
    Vue.prototype.$appConfig = config.data;

    new Vue({
      vuetify,
      router,
      store,
      render: (h) => h(App),
    }).$mount("#app");
  })
);
