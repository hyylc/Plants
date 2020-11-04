import Vue from "vue";
import Router from "vue-router";
import Home from "./views/user_Home.vue";
import login from "./views/login_in.vue";
import Cate from "./views/Cate.vue";
import user from "./views/user.vue";
import Plant from "./views/Plant.vue";
import CreateP from "./views/Create_plant.vue";
import plantsearch from "./views/Search_plant.vue";
import txj_sign from "./views/txj_Signin.vue";
import Resetuinfo from "./views/Resetuserinfo.vue";
import Resetpassword from "./views/Resetpassword.vue";

Vue.use(Router);

//这里写路由
export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    { //登录页面
      path: "/login",
      name: "login_in",
      component: login
    },
    {//修改昵称页面
      path: "/Resetuserinfo",
      name: "Resetuserinfo",
      component: Resetuinfo
    },
    {//修改密码页面
      path: "/Resetpassword",
      name: "Resetpassword",
      component: Resetpassword
    },
    { //网站首页
      path: "/",
      name: "home",
      component: Home
    },
    //用户信息页面
    {
      path: "/userinfo/:user_id",//是vue里面写的path
      name: "userinfo",
      component: user
    },
    //植物搜索展示页面，匹配到之后就不会继续匹配了，所以要放在植物分类页面前面
    {
      path: "/search",
      name: "plantsearch",
      component: plantsearch
    },
    //txj的登录页面
    {
      path: "/txj_signin",
      name: "txj_sign",
      component: txj_sign
    },
    //植物信息展示页面
    {
      path: "/plant/:plant_id",
      name: "Plant",
      component: Plant
    },
    //增加植物页面
    {
      path: "/createplant",
      name: "CreateP",
      component: CreateP
    },
    //植物分类显示页面
    {
      path: "/:cate_id",
      name: "Cate",
      component: Cate
    },
    

    //
    //{
    //  path: "/about",
    //  name: "about",
    //  // route level code-splitting
    //  // this generates a separate chunk (about.[hash].js) for this route
    //  // which is lazy-loaded when the route is visited.
    //  component: () =>
    //    import(/* webpackChunkName: "about" */ "./views/About.vue")
    //}
  ]
});
