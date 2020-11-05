<template>
  <div id="Plant">
      <Header />
<div class="contain">
					<div class="btitle">植物信息</div>
					<div class="bform">
				<ul>
                <li v-for="item in plant.info" :key="item.PlantID">
                    <div class="bform">
						<p><span>植物名称:</span><a>{{item.PlantName}} </a></p>
						<p><span>植物性状:</span><a>{{item.Characters}} </a></p>
						<p><span>门:</span><a>{{item.Phylum}} </a></p>
						<p><span>纲:</span><a>{{item.Class}} </a></p>
						<p><span>目:</span><a>{{item.Order}} </a></p>
						<p><span>科:</span><a>{{item.Family}} </a></p>
						<p><span>属:</span><a>{{item.Genus}} </a></p>
						<p><span>种:</span><a>{{item.Specices}} </a></p>
						<p><span>植物分布:</span><a>{{item.Location}} </a></p>
					</div>
                </li>
               </ul>
              	
			</div>
            <v-if>
               <button @click="add_collect"  class="bbutton">点击收藏</button>
            </v-if>
            <v-else>
                <button @click="del_collect"  class="bbutton">取消收藏</button>
            </v-else>

			
		</div>
		
      <Footer />
  </div>
</template>

<script>
import Header from "../components/Header";
import Footer from "../components/Footer";
import { reactive, ref, onMounted} from "@vue/composition-api";//ref定义常量;reactive定义对象
import { Get_is_collected,Get_one_plant,Add_a_collection,Del_a_collection } from "../apis/read"

export default{
    name : "Plant",
    components:{
        Header,
        Footer
    },
    setup(props, context){
        const now_url = ref(context.root.$route.path)//ref用.value才能获取到url值
        //传递参数：植物ID
        const plantparam = reactive({
            url:now_url.value,//'/plant/:plant_id'
        });
        //传递参数：用户ID和植物ID
        const collectparam = reactive({
            user_id : '',
            plant_id : ''
        });
        //返回植物信息
        const plant = reactive({
            info:[]
        });
        //返回是否已收藏
        const is_col = reactive({
            flag:''
        });
        
        collectparam.user_id = window.sessionStorage.UserID;
        collectparam.plant_id = (now_url.value.match(/\d+/g));
        console.log("user_id = ",collectparam.user_id," plant_id = ",collectparam.plant_id)

        //获得植物信息
        Get_one_plant(plantparam).then(resp => {
            console.log("获得植物信息 = ",resp);
            plant.info = resp.data.data;
        });

        //获得用户是否已收藏该植物
        Get_is_collected(collectparam).then(resp => {
            is_col.flag = resp.data.data;
            console.log("是否收藏：",is_col.flag)
        });

        //添加收藏
        const add_collect = ()=>{
            //console.log("add_collect待完成的代码");
            //调用添加收藏的接口
            Add_a_collection(collectparam).then(resp => {
                console.log("收藏成功 = ",resp.data.data);
                if(resp.data.data == true){
                    alert("收藏成功。")
                }
                else{
                    alert("收藏失败。")
                }
            });
        };

        //取消收藏
        const del_collect = ()=>{
            //console.log("del_collect待完成的代码");
            //调用删除收藏的接口
            Del_a_collection(collectparam).then(resp => {
                console.log("取消收藏成功 = ",resp.data.data);
                if(resp.data.data == true){
                    alert("取消收藏成功。")
                }
                else{
                    alert("取消收藏失败。")
                }
            });
        };

        onMounted(()=>{
            console.log("In Plant context = ", context.root.$route.path)//获取地址
        });

        return {
            plant,
            add_collect,
            del_collect,
            is_col,
            //fields: ['PlantID','PlantName','Characters','Location']
        }
    }
}
</script>




<style scoped="scoped">
	.Plant{
		width: 100vw;
		height: 100vh;
		box-sizing: border-box;
	}
    .contain{
		width: 60%;
		height: 60%;
		position: relative;
        margin-top: 300px;
		left: 50%;
		transform: translate(-50%,-50%);
		background-color: #fff;
		border-radius: 20px;
		box-shadow: 0 0 3px #f0f0f0,
					0 0 6px #f0f0f0;
	}
	.big-box{
		width: 100%;
		height: 100%;
		position: absolute;
		top: 100;
		left: 30%;
		transform: translateX(0%);
		transition: all 1s;
	}
	.big-contain{
		width: 100%;
		height: 100%;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}
    .btitle{
		font-size: 1.5em;
		font-weight: bold;
        text-align: center;
		color: rgb(57,167,176);
	}
	.bform{
		width: 100%;
		height: 70%;
		padding: 2em 0;
		display: flex;
		flex-direction: column;
		justify-content: space-around;
		align-items: center;
	}
    li{
        list-style: none;
    }
    p{
        text-align: left;
        font-size: 0.2rem;
        margin:auto;
        font-weight: bold;
        color: rgb(57,167,176);
    }
	.bform .errTips{
		display: block;
		width: 50%;
		text-align: left;
		color: red;
		font-size: 0.7em;
		margin-left: 1em;
	}
	.bform .input{
		width: 50%;
		height: 30px;
		border: none;
		outline: none;
		border-radius: 10px;
		padding-left: 2em;
		background-color: #f0f0f0;
	}
	.bbutton{
        display: block;
		width: 20%;
		height: 40px;
		border-radius: 24px;
		border: none;
		outline: none;
		background-color: rgb(57,167,176);
		color: #fff;
		font-size: 0.9em; 
        margin-top: 20px;
        margin-left: auto;
        margin-right: auto;
        text-align: center;
		cursor: pointer;
	}

</style>
