<template>
	<div class="login-register">
		
      <Header />
		<div class="contain">
					<div class="btitle">修改资料</div>
					<div class="bform">
						<input type="text" placeholder="用户名" v-model="user.new_name">
					</div>
					<button class="bbutton" type="submit" @click="OnReset">保存设置</button>
		</div>
		<!-- <Footer /> -->
	</div>
</template>

<script>
import Header from "../components/Header";
import Footer from "../components/Footer";
import { stripscript } from "../apis/validate"
import { reactive, ref, onMounted} from "@vue/composition-api";//ref定义常量;reactive定义对象
import { Reset_userinfo } from "../apis/read"

export default{
		name:'login-register',
		components:{
			Header,
			Footer
		},
		setup(props, context){

			const user = reactive({
				new_name : '',
				userID : ''
			});

			user.userID = window.sessionStorage.UserID
            console.log('In Reset user.userID = ',user.userID)
			
			
			const OnReset = ()=>{
				if(stripscript(user.new_name) == false || user.new_name == ''){
               		alert("输入信息有误，请确认后重新输入。")
            	} 
				else{
					
					//发起请求获得结果
					Reset_userinfo(user).then(resp => {
						console.log("In login resp = ",resp);
						console.log("In login resp.data.data = ",resp.data.data)
						if (resp.data.resCode == 0){
							alert('修改成功');
							context.root.$router.push({
                            	path:'/userinfo/'
                        	});
						}
						else{
							//停留在当前页面
							alert('修改失败');
						}
					});
				}	
			};

			return{
				user,
				OnReset
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
		height: 60%;
		opacity:0.75;
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
		width: 70%;
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
		height: 40%;
		padding: 2em 0;
		display: flex;
		flex-direction: column;
		justify-content: space-around;
		align-items: center;
	}
	.bform .errTips{
		display: block;
		width: 50%;
		text-align: left;
		color: red;
		font-size: 0.7em;
		margin-left: 1em;
	}
	.bform input{
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
        margin-left: auto;
        margin-right: auto;
        text-align: center;
		cursor: pointer;
	}

</style>
