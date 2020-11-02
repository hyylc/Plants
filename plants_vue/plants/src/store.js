import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    //token:''//初始化token
    //user : window.sessionStorage.getItem('user')
  },
  mutations: {
    // GET_USER :(state,data)=>{
    //   console.log("data = ",data)
    //   state.user = data
    //   window.sessionStorage.setItem('user',data)
    //   console.log("window.sessionStorage.user = ",window.sessionStorage.user)
    // },
    // LOGOUT :(state)=>{
    //   state.user = null
    //   window.sessionStorage.removeItem('user')
    // }
  },
  actions: {}
});
