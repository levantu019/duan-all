const state = {
  isDraw: false,
  actionkey: "",
  geometry: null,
};

const getters = {
  isDraw: (state) => state.isDraw,
  actionkey: (state) => state.actionkey,
  geometry: (state) => state.geometry,
};

const mutations = {
  TOGGLE_DRAW: (state, isVisible) => {
    state.isDraw = isVisible;
  },
  SET_GEOMETRY: (state, geometry) => {
    state.geometry = geometry;
  },
  SET_ACTION_KEY: (state, actionkey) => {
    state.actionkey = actionkey;
  },
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
};
