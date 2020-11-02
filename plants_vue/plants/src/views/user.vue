<template>
  <div id="userinfo">
      <Header />
      <b-container>
        <div style="height:1000px;background-color:pink">
            {{user.userinfo.UserID}}
            
            <a v-for="item in user.userinfo" :key="item.UserID" >{{item}}</a>
        </div>
      </b-container>
      <Footer />
  </div>
</template>

<script>
import Header from "../components/Header";
import Footer from "../components/Footer";
import { reactive, ref, onMounted} from "@vue/composition-api";//ref定义常量;reactive定义对象
import { Get_userinfo } from "../apis/read"

export default{
    name : "userinfo",
    components:{
        Header,
        Footer
    },
    setup(props, context){
        const now_url = ref(context.root.$route.path)//ref用.value才能获取到url值
        console.log("now_url = ",now_url.value)//确实在value里面

        const user = reactive({
            userinfo:[]
        });


        const userparam = reactive({
            userID : ''
        });
        
        
    

        //获取已登录的用户信息
        userparam.userID = window.sessionStorage.UserID
        console.log("In user userID get from winsow.sessionStorage = ",userparam.userID)

        //发起请求获得结果
        Get_userinfo(userparam).then(resp => {
            console.log('打印返回结果');
            console.log("resp = ",resp);
            user.userinfo = resp.data.data;
            console.log("user.userinfo = ",user.userinfo);
        });

        onMounted(()=>{
            console.log("In user context = ", context.root.$route.path)//获取地址
        });

        return {
            user
        }
    }
}
</script>


<style lang='scss' scoped>//lang告诉解释其css符合什么编译器的语法；scoped：当前vue文件生效，没有scoped则全局生效

</style>