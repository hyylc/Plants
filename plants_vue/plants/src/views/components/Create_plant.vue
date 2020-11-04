<template>
  <div id="create_plant">
      <Header />
      <b-container>
        <div style="height:2000px;background-color:pink">
            //添加一个新的植物信息 
        </div>

      </b-container>
      <Footer />
  </div>
</template>

<script>
import Header from "../components/Header";
import Footer from "../components/Footer";
import { reactive, ref, onMounted} from "@vue/composition-api";//ref定义常量;reactive定义对象
import { Add_plant } from "../apis/read"

export default{
    name : "create_plant",
    components:{
        Header,
        Footer
    },
    setup(props, context){
        //const now_url = ref(context.root.$route.path)//ref用.value才能获取到url值

        //传递参数，目标链接和查询数据的特点
        //const newestParams = reactive({
        //    url:now_url.value,//用于传递请求的链接，这里是植物的标签，直接作为参数传递给后端
        //    //key://传递查询的标签
        //});

        const headData = reactive({
            headers:[]
        });

        //发起请求获得结果
        Add_plant().then(resp => {
            console.log(resp);
            headData.headers = resp.data.data;
        });


        onMounted(()=>{
            console.log("In Plant context = ", context.root.$route.path)//获取地址
        });

        return {
            headData//,
            //fields: ['PlantID','PlantName','Characters','Location']
        }
    }
}
</script>


<style lang='scss' scoped>//lang告诉解释其css符合什么编译器的语法；scoped：当前vue文件生效，没有scoped则全局生效

</style>