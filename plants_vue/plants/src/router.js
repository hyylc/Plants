import Vue from "vue";
import Router from "vue-router";
import Home from "./views/Home.vue";
import Cate from "./views/Cate.vue";
import user from "./views/user.vue";

Vue.use(Router);

//这里写路由
export default new Router({
  mode: "history",
  base: process.env.BASE_URL,
  routes: [
    { //网站首页
      path: "/",
      name: "home",
      component: Home
    },
   
    
    //用户信息页面
    {
      path: "/userinfo",//是vue里面写的path
      name: "userinfo",
      component: user
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
