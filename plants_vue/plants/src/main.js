import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";
import VueCompositionApi from "@vue/composition-api";
import VueResource from "vue-resource";
import { BootstrapVue, BootstrapVueIcons } from "bootstrap-vue";
import 'bootstrap/dist/css/bootstrap.css';
import 'bootstrap-vue/dist/bootstrap-vue.css';
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';


Vue.use(ElementUI);
Vue.use(BootstrapVue);
Vue.use(BootstrapVueIcons);
Vue.use(VueCompositionApi);
Vue.use(VueResource);

Vue.config.productionTip = false;

// router.beforeEach((to,from,next) => {
// 	// 如果即将进入的路由对象是登录页，则进行跳转，否则验证是否携带accessToken,如果有，则进
// 	// 行跳转，没有，则不允许跳转
//     if(to.path === "/txj_signin"){
//         next()
//     }
//     else{
//         if (window.sessionStorage.getItem('UserID')){
//           console.log('window.sessionStorage.UserID = ',window.sessionStorage.UserID)
//           next()
//         } 
//         else{
//             next("/txj_signin")
//         }
//     }
// })


new Vue({
  router,
  store,
  render: h => h(App)
}).$mount("#app");
