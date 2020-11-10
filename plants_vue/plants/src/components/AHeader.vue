<template>
    <b-container>
        <div class="background">
        <img :src="imgsrc" width="100%" height="100%" alt=""/>
         </div>
        <b-navbar toggleable="lg" type="dark" variant="info">
            <b-navbar-brand href="#">植物信息检索</b-navbar-brand>
            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
            <b-collapse id="nav-collapse" is-nav>
            <b-navbar-nav >
                    <b-nav-item v-for = "item in headData.headers" :key="item.id" :href="item.url" :class="item.url == now_url ? 'active' : ''">{{item.name}}</b-nav-item>
            </b-navbar-nav>
            </b-collapse>
        </b-navbar>
    </b-container>
</template>

<script>
import { reactive, ref ,onMounted} from "@vue/composition-api";//ref定义常量;reactive定义对象
import { stripscript } from "../apis/validate.js"

export default {
    name : "Header",
    setup(props, context){ //setup相当于before create;props父组件传入的内容;context当前组件拥有的内容
        const now_url = ref(context.root.$route.path);
        
        const headData = reactive({
            headers:[]
        });

        const User  = reactive({
            UserID:''
        });

        //获取已登录的用户信息
        User.UserID = window.sessionStorage.UserID
        //console.log("userID get from window.sessionStorage = ",User.UserID)
      
        headData.headers = [
            {'id':0,'name':'用户管理','url':'/Aindex'},
            {'id':1,'name':'植物管理','url':'/Aplant'},
            {'id':2,'name':'退出','url':'/Signin'},
        ]
        //console.log("headData.headers = ",headData.headers)


        return {
            headData,
            now_url,
            User,
            imgsrc: require('../assets/backpic.jpg')
        }
    }
}
</script>

<style lang='scss' scoped>//lang告诉解释其css符合什么编译器的语法；scoped：当前vue文件生效，没有scoped则全局生效
.background{
  top: 50;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: -1;
  position: absolute;
}
</style>