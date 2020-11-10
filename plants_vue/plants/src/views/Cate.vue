<template>
  <div id="Cate">
      <Header />
      <b-container>
          <div v-if="headData.headers == 0">
              该分类下暂时没有植物被收录。
          </div>
        <div style="background-color:white;opacity:0.8">
            //这里要获取不同分类并显示，还得附上url
            //可以从现有的url获取植物信息
            
            <b-row>
                <b-col cols="12" md="12">    
                    
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
import { Get_cates } from "../apis/read"

export default{
    name : "Cate",
    components:{
        Header,
        Footer
    },
    setup(props, context){
        const now_url = ref(context.root.$route.path)//ref用.value才能获取到url值

        //传递参数，目标链接和查询数据的特点
        const newestParams = reactive({
            url:now_url.value,//用于传递请求的链接，这里是植物的标签，直接作为参数传递给后端
            //key://传递查询的标签
        });

        const headData = reactive({
            headers:[]
        });

        //发起请求获得结果
        Get_cates(newestParams).then(resp => {
            console.log(resp);
            headData.headers = resp.data.data;
        });


        onMounted(()=>{
            console.log("In Cate context = ", context.root.$route.path)//获取地址
        });

        return {
            headData
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