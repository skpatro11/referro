import { createStore } from 'vuex';
import axios from 'axios';

export default createStore({
  state: {
    user: null,
    token: null,
  },
  mutations: {
    SET_USER_DATA(state, userData) {
      // localStorage.setItem('user', JSON.stringify(userData));
      state.user = userData;
    },
    SET_AUTH_TOKEN(state, token) {
      localStorage.setItem('token', token);
      axios.defaults.headers.common['Authorization'] = `Bearer ${token}`;
      state.token = token;
    },
    CLEAR_DATA(state) {
      state.data = null;
      state.token = null;
      localStorage.removeItem('user');
      localStorage.removeItem('token');
      location.reload();
    },
  },
  actions: {
    login({ commit }, credentials) {
      return axios
        .post(
          'https://referro.herokuapp.com/authentication/token/',
          credentials
        )
        .then(({ data }) => {
          commit('SET_AUTH_TOKEN', data.access);
        });
    },
    logout({ commit }) {
      commit('CLEAR_DATA');
    },
    setUser({ commit }) {
      axios
        .get('https://referro.herokuapp.com/authentication/profile/')
        .then(({ data }) => commit('SET_USER_DATA', data))
        .catch((err) => console.log('Unable to set user data'));
    },
  },
  modules: {},
  getters: {
    loggedIn(state) {
      return !!state.token;
    },
    user(state) {
      return state.user;
    },
  },
});
