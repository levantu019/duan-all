const state = {
  listDiemNVDH: Object,
};

const getters = {
  listDiemNVDH: (state) => state.listDiemNVDH,
};

const mutations = {
  SET_LIST_DIEM_NVDH: (state, listDiemNVDH) => {
    state.listDiemNVDH = listDiemNVDH;
  },
};

export default {
  namespaced: true,
  state,
  getters,
  mutations,
};
