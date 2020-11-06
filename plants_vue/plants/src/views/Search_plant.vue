<template>
  <div id="search_plant">
      <Header />
      <b-container class="mt">
        <div style="height:2000px;background-color:white;opacity:0.8">
            <b-row><b-col><h4>查询结果</h4></b-col></b-row>
            <b-row>
                <b-col v-if="headData.headers.length > 0"   cols="12" md="12">    
                    
                    <table role="table" aria-busy="false" aria-colcount="3" class="table b-table table-striped table-hover" ><!----><!---->
                            <thead role="rowgroup" class=""><!---->
                            <tr role="row" class="">
                                <th role="columnheader" scope="col" aria-colindex="1" class=""><div>PlantName</div></th>
                                <th role="columnheader" scope="col" aria-colindex="2" class=""><div>Characters</div></th>
                                <th role="columnheader" scope="col" aria-colindex="3" class=""><div>Location</div></th></tr>
                            </thead>
                            <tbody role="rowgroup"><!---->
                                <tr role="row" v-for="item in headData.headers" :key="item.PlantID">
                                <td aria-colindex="1" role="cell" class=""><a :href="'/plant/'+ item.PlantID">{{ item.PlantName }}</a></td>
                                <td aria-colindex="2" role="cell" class="">{{ item.Characters }}</td>
                                <td aria-colindex="3" role="cell" class="">{{ item.Location }}</td></tr>
                                
                            </tbody><!---->
                        </table>    
                </b-col>
                <b-col v-else> 
                    查询结果不存在，请重新查询。
                </b-col>
        </b-row>
        </div>

      </b-container>
      <!-- <Footer /> -->
  </div>
</template>

<script>
import Header from "../components/Header";
import Footer from "../components/Footer";
import { reactive, ref, onMounted} from "@vue/composition-api";//ref定义常量;reactive定义对象
import { Search_plant } from "../apis/read"

export default{
    name : "search_plant",
    components:{
        Header,
        Footer
    },
    //如何组建提交到flask的参数
    setup(props, context){
        //const now_url = ref(context.root.$route.path)//ref用.value才能获取到url值

        //传递参数，目标链接和查询数据的特点
        const searchParams = reactive({
            url:'/search',//用于传递请求的链接，这里是植物的标签，直接作为参数传递给后端
            key:context.root.$route.query.q//在header.vue里加上了query.q这个变量，因此从这里获取输入的数据，作为参数（添加新的植物，可以参考这样的参数传递）
        });

        const headData = reactive({
            headers:[]
        });

        //发起请求获得结果
        Search_plant(searchParams).then(resp => {
            console.log(resp);//打印
            console.log("In search resp.data.data = ",resp.data.data)
            headData.headers = resp.data.data;
        });


        onMounted(()=>{
            console.log("In search context = ", context.root.$route.path)//打印
        });

        return {
            headData//,
            //fields: ['PlantID','PlantName','Characters','Location']
        }
    }
}
</script>


<style lang='scss' scoped>//lang告诉解释其css符合什么编译器的语法；scoped：当前vue文件生效，没有scoped则全局生效
table
{
    table-layout: fixed;
    width: 100%;
}
td
{
    width:200px;  
     overflow:hidden;  
     white-space:nowrap;  
     text-overflow:ellipsis;  
     -o-text-overflow:ellipsis;  
     -icab-text-overflow: ellipsis;  
     -khtml-text-overflow: ellipsis;  
     -moz-text-overflow: ellipsis;  
     -webkit-text-overflow: ellipsis;  
      }
</style>