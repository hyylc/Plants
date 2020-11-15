<template>
  <div id="Plant">
      <Header />
    <div class="contain">
					<div class="btitle">植物信息</div>
					<div class="bform">
				<ul>
                <li v-for="item in plant.info" :key="item.PlantID">
                    <div class="bform">
						<p><span>植物名称:</span><a style="width:200px;heigh:50px;color:#2f4f4f">{{item.PlantName}} </a></p>
						<p><span>植物性状:</span><a style="width:200px;heigh:50px;color:#2f4f4f">{{item.Characters}} </a></p>
						<p><span>门:</span><a style="width:200px;heigh:50px;color:#2f4f4f">{{item.Phylum}} </a></p>
						<p><span>纲:</span><a style="width:200px;heigh:50px;color:#2f4f4f">{{item.Class}} </a></p>
						<p><span>目:</span><a style="width:200px;heigh:50px;color:#2f4f4f">{{item.Order}} </a></p>
						<p><span>科:</span><a style="width:200px;heigh:50px;color:#2f4f4f">{{item.Family}} </a></p>
						<p><span>属:</span><a style="width:200px;heigh:50px;color:#2f4f4f">{{item.Genus}} </a></p>
						<p><span>种:</span><a style="width:200px;heigh:50px;color:#2f4f4f">{{item.Specices}} </a></p>
						<p><span>植物分布:</span><a style="width:200px;heigh:50px;color:#2f4f4f">{{item.Location}} </a></p>
					</div>
                </li>
               </ul>
              	
			</div>
           

			
		</div>
		
      <!-- <Footer /> -->
  </div>
</template>

<script>
import Header from "../components/AHeader";
import Footer from "../components/Footer";
import { reactive, ref, onMounted} from "@vue/composition-api";//ref定义常量;reactive定义对象
import { Get_one_plant2 } from "../apis/read"

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
            url:now_url.value,//'/plantA/:plant_id'
        });

        //返回植物信息
        const plant = reactive({
            info:[]
        });

        //获得植物信息
        Get_one_plant2(plantparam).then(resp => {
            console.log("获得植物信息 = ",resp);
            plant.info = resp.data.data;
        });

        onMounted(()=>{
            console.log("In Plant context = ", context.root.$route.path)//获取地址
        });

        return {
            plant,
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
        opacity:0.75;
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
		/* display: flex;
		flex-direction: column;
		justify-content: space-around; */
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
        //display: block;
		width: 20%;
		height: 40px;
		border-radius: 24px;
		border: none;
		outline: none;
		background-color: rgb(57,167,176);
		color: #fff;
		font-size: 0.9em; 
        margin-left: 120px;
        margin-right: auto;
        text-align: center;
		cursor: pointer;
	}

</style>
