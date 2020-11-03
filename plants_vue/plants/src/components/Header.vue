<template>
    <b-container>
        <b-navbar toggleable="lg" type="dark" variant="info">
            <b-navbar-brand href="#">植物信息检索</b-navbar-brand>
            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>
            <b-collapse id="nav-collapse" is-nav>
            <b-navbar-nav v-if="User.UserID !== undefined">
                    这里要修改，获取全局变量，登陆后，将用户的ID作为url的一部分
                    <b-nav-item v-for = "item in headData.headers" :key="item.id" :href="item.url" :class="item.url == now_url ? 'active' : ''">{{item.name}}</b-nav-item>
                    <a>{{User.UserID}}</a>
            </b-navbar-nav>
            <b-navbar-nav v-else>
                注册/登录
            </b-navbar-nav>
            <ul  class="navbar-nav ml-auto">
                <li class="form-inline">
                    <div class="form-inline">
                        <input v-model="search.key" type="text" placeholder="输入植物名称" class="mr-sm-2 from-control-sm">
                        <button @click="Onsearch"  type="submit" class="btn my-2 my-sm-0 btn-secondary btn-sm">开始查询</button>
                    </div>
                </li>
            </ul>
            </b-collapse>
        </b-navbar>
    </b-container>
</template>

<script>
import { Get_header } from "../apis/read.js";//从apis中引入，通过这个请求拿到数据
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

        onMounted(()=>{
            console.log("In Header search.key = ",search.key);
            alert(search.key)
        });
        //数据绑定
        const search = reactive({
            key:''
        });
        
        //获取已登录的用户信息
        User.UserID = window.sessionStorage.UserID
        console.log("userID get from winsow.sessionStorage = ",User.UserID)
      
        headData.headers = [
            {'id':0,'name':'首页','url':'/'},
            {'id':1,'name':'个人中心','url':'/userinfo/'+User.UserID}
        ]
        console.log("headData.headers = ",headData.headers)



        const Onsearch = ()=>{
            console.log("In Header search.key = ",search.key);

            if(stripscript(search.key) == false || search.key == ''){
                alert("输入信息有误，请确认后重新输入。")
            } 
            else{
                context.root.$router.push({
                path:'/search',
                query:{
                    q:search.key
                }
                });
            }

        };
        return {
            headData,
            now_url,
            search,
            Onsearch,
            User
        }
    }
}
</script>

<style lang='scss' scoped>//lang告诉解释其css符合什么编译器的语法；scoped：当前vue文件生效，没有scoped则全局生效

</style>