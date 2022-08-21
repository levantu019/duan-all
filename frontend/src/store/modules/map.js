const state = {
  map: null,
  helpTooltip: {
    isActive: false,
    currentMessage: "",
  },
  messages: {
    snackbar: {
      type: "info",
      message: "",
      state: false,
      timeout: 2000,
    },
  },
};

const getters = {
  map: (state) => state.map,
  helpTooltip: (state) => state.helpTooltip,
  messages: (state) => state.messages,
  snackbar: (state) => state.messages.snackbar,
};

const actions = {};

const mutations = {
  SET_MAP(state, map) {
    state.map = map;
  },

  TOGGLE_SNACKBAR(state, payload) {
    state.messages.snackbar = { ...payload };
  },
};

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations,
};
