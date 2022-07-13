import Vue from "vue";
import Vuex from "vuex";
//import createPersistedState from "vuex-persistedstate";
import draw from "./modules/draw";
import user from "./modules/user";
import map from "./modules/map";

Vue.use(Vuex);

export default new Vuex.Store({
  modules: { user, draw, map },
  // plugins: [
  //   createPersistedState({
  //     paths: "",
  //   }),
  // ],
});
