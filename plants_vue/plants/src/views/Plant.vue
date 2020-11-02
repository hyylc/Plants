<template>
  <div id="Plant">
      <Header />
      <b-container>
        <div style="height:2000px;background-color:pink">
            //根据plantID获取一个植物的信息
            
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
                                <tr role="row" v-for="item in headData.headers" :key="item.id">
                                <td aria-colindex="1" role="cell" class=""><a :href="'/plant/'+ item.PlantID">{{ item.PlantName }}</a></td>
                                <td aria-colindex="2" role="cell" class="">{{ item.Characters }}</td>
                                <td aria-colindex="3" role="cell" class="">{{ item.Location }}</td></tr>
                                
                            </tbody><!---->
                        </table>    
                </b-col>
        </b-row>

        <ul  class="navbar-nav ml-auto">
                    <li class="form-inline">
                        <div class="form-inline">
                           <button @click="Oncollect"  type="submit" class="btn my-2 my-sm-0 btn-secondary btn-sm">点击收藏</button>
                        </div>
                    </li>
                </ul>
        </div>

      </b-container>
      <Footer />
  </div>
</template>

<script>
import Header from "../components/Header";
import Footer from "../components/Footer";
import { reactive, ref, onMounted} from "@vue/composition-api";//ref定义常量;reactive定义对象
import { Get_one_plant } from "../apis/read"

export default{
    name : "Plant",
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
        Get_one_plant(newestParams).then(resp => {
            console.log("resp = ",resp);
            headData.headers = resp.data.data;
        });

        const Oncollect = ()=>{
            console.log("待完成的代码");

        };

        onMounted(()=>{
            console.log("In Plant context = ", context.root.$route.path)//获取地址
        });

        return {
            headData,
            Oncollect
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