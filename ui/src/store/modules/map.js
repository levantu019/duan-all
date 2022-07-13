const state = {
  map: null,
  helpTooltip: {
    isActive: false,
    currentMessage: "",
  },
};

const getters = {
  map: (state) => state.map,
  helpTooltip: (state) => state.helpTooltip,
};

const actions = {};

const mutations = {
  SET_MAP(state, map) {
    state.map = map;
  },
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
