import { getToken } from "@/utils/auth";

const state = {
  token: getToken(),
  name: "",
  avatar: "",
  introduction: "",
  roles: [],
  userId: undefined,
};

const getters = {
  token: (state) => state.token,
  userId: (state) => state.userId,
};

const mutations = {
  SET_TOKEN: (state, token) => {
    state.token = token;
  },
  SET_INTRODUCTION: (state, introduction) => {
    state.introduction = introduction;
  },

  SET_NAME: (state, name) => {
    state.name = name;
  },
  SET_AVATAR: (state, avatar) => {
    state.avatar = avatar;
  },
  SET_ROLES: (state, roles) => {
    state.roles = roles;
  },
  SET_USER_ID: (state, userId) => {
    state.userId = userId;
  },
};

const actions = {
  // login({ commit }, userInfo) {
  //   console.log(commit, userInfo``);
  // },
  // getInfo({ commit, state }) {
  //   console.log(commit, state);
  //set roles
  //set name
  //set avatar
  //set introduction
  // },
  // logout({ commit, state, dispatch }) {
  //   console.log(commit, state, dispatch);
  //   //set token
  //   //set roles
  // },
  // //remove token
  // resetToken({ commit }) {
  //   console.log(commit);
  //   //set token = ''
  //   //set roles = []
  //   //removeToken();
  // },
  //change Roles
};
export default {
  state,
  actions,
  mutations,
  getters,
};
