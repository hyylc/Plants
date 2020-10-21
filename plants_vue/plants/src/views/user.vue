<template>
  <div id="user">
      <Header />
      <b-container>
        <div style="height:1000px;background-color:red">
            <span v-for = "item in headData.headers" :key="item.UserID">{{item}}</span>
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
    name : "user",
    components:{
        Header,
        Footer
    },
    setup(props, context){
        const now_url = ref(context.root.$route.path)//ref用.value才能获取到url值
        console.log("now_url = ",now_url.value)//确实在value里面

        const headData = reactive({
            headers:[]
        });
        //发起请求获得结果
        Get_userinfo().then(resp => {
            console.log(resp);
            headData.headers = resp.data.data;
        });

        onMounted(()=>{
            console.log("In user context = ", context.root.$route.path)//获取地址
        });

        return {
            headData
        }
    }
}
</script>


<style lang='scss' scoped>//lang告诉解释其css符合什么编译器的语法；scoped：当前vue文件生效，没有scoped则全局生效

</style>