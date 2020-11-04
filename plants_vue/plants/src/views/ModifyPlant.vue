<template>
	<div class="login-register">
		<Header />
		<div class="contain">
					<div class="btitle">修改植物信息</div>
					<div class="bform">
						
              		<ul>
						<p><span>植物名称:</span><input type="text" v-model="plantinfo.PlantName" ></p>
						<p><span>植物性状:</span><input type="sex"  v-model="plantinfo.Characters"></p>
						<p><span>门:</span><input type="door1"  v-model="plantinfo.Phylum"></p>
						<p><span>纲:</span><input type="door2"  v-model="plantinfo.Class"></p>
						<p><span>目:</span><input type="door3"  v-model="plantinfo.Order"></p>
						<p><span>科:</span><input type="door4"  v-model="plantinfo.Family"></p>
						<p><span>属:</span><input type="door5"  v-model="plantinfo.Genus"></p>
						<p><span>种:</span><input type="door6"  v-model="plantinfo.Specices"></p>
						<p><span>植物分布:</span><input type="where" v-model="plantinfo.Location"></p>
               		</ul>
					</div>
					<button class="bbutton" @click="Oncollect">保存设置</button>
			

			
		</div>
		
      <Footer />
	</div>
</template>

<script>
import Header from "../components/Header";
import Footer from "../components/Footer";
import { stripscript } from "../apis/validate"
import { reactive, ref, onMounted} from "@vue/composition-api";//ref定义常量;reactive定义对象
import { Get_one_plant1 , Modify_plantinfo} from "../apis/read"


	export default{
		name:'login-register',
		components:{
        Header,
        Footer
    	},
    setup(props, context){
        const now_url = ref(context.root.$route.path)//ref用.value才能获取到url值

        //传递参数，目标链接和查询数据的特点
        const plantParam = reactive({
            plant_id : '',//用于传递请求的链接，这里是植物的id(/plant/<int:plant_id>)
		});
		
		plantParam.plant_id = now_url.value.match(/\d+/g);
		console.log("url = ",plantParam.plant_id)

        const plantinfo = reactive({
			PlantID : '',
			PlantName :'',
			Characters :'',
			Phylum :'',
			Class :'',
			Order :'',
			Family :'',
			Genus :'',
			Specices :'',
			Location :''
        });

		plantinfo.PlantID = now_url.value.match(/\d+/g);
		
        //发起请求获得结果
        Get_one_plant1(plantParam).then(resp => {
            console.log("resp = ",resp);
			plantinfo.PlantName = resp.data.data[0].PlantName;
			plantinfo.Characters = resp.data.data[0].Characters;
			plantinfo.Phylum = resp.data.data[0].Phylum;
			plantinfo.Class = resp.data.data[0].Class;
			plantinfo.Order = resp.data.data[0].Order;
			plantinfo.Family = resp.data.data[0].Family;
			plantinfo.Genus = resp.data.data[0].Genus;
			plantinfo.Specices = resp.data.data[0].Specices;
			plantinfo.Location = resp.data.data[0].Location;
			console.log("after get plantname = ",plantinfo.PlantName)
        });

        const Oncollect = ()=>{
			console.log("待完成的代码");
			console.log("now Genus = ",plantinfo.Genus)
			console.log("now Specices = ",plantinfo.Specices)
			console.log("now Location = ",plantinfo.Location)
			console.log("now Family = ",plantinfo.Family)
			Modify_plantinfo(plantinfo).then(resp => {
				console.log("resp = ",resp);
			});

        };

        onMounted(()=>{
            console.log("In Plant context = ", context.root.$route.path)//获取地址
        });

        return {
            plantinfo,
			Oncollect
            //fields: ['PlantID','PlantName','Characters','Location']
        }
    }
	}
</script>

<style scoped="scoped">
	.login-register{
		width: 100vw;
		height: 100vh;
		box-sizing: border-box;
	}
	.contain{
		width: 60%;
		height: 100%;
		position: relative;
		top: 50%;
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
		top: 0;
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
