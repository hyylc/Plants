<template>
	<div class="login-register">
		<Header />
		<div class="contain">
			<div class="big-box" :class="{active:isLogin.flag}">
				<div class="big-contain" v-if="isLogin.flag === true">
					<div class="btitle">账户登录</div>
					<div class="bform">
						<!-- autocomplete=false -->
						<input v-model="user.username" type="text"  placeholder="用户名" >
						<input v-model="user.password" type="password"  placeholder="密码" >
					</div>
					<button class="bbutton" @click="Onlogin" type="submit" >登录</button>
				</div>
				<div class="big-contain" v-else>
					<div class="btitle">创建账户</div>
					<div class="bform">
						<input v-model="user1.username" type="text"  placeholder="用户名" >
						<input v-model="user1.password" type="password"  placeholder="密码" >
						<input v-model="user1.password2" type="password"  placeholder="再次密码" >
					</div>
					<button class="bbutton" @click="register">注册</button>
				</div>
			</div>
			<div class="small-box" :class="{active:isLogin.flag}">
				<div class="small-contain" v-if="isLogin.flag === true">
					<div class="stitle">你好，朋友!</div>
					<p class="scontent">开始注册，快来探索植物的奥秘</p>
					<button @click="changeType" class="sbutton" >注册</button>
				</div>
				<div class="small-contain" v-else>
					<div class="stitle">欢迎回来!</div>
					<p class="scontent">与大伙一起探索植物的奥秘</p>
					<button @click="changeType" class="sbutton" >登录</button>
				</div>
			</div>
		</div>
		<!-- <Footer /> -->
	</div>
</template>

<script>
import Header from "../components/Header";
import Footer from "../components/Footer";
import { stripscript } from "../apis/validate.js"
import { reactive, ref, onMounted} from "@vue/composition-api";//ref定义常量;reactive定义对象
import { do_login } from "../apis/read"
import { do_register } from "../apis/read"

export default{
		name:'login-register',
		components:{
		Header,
		Footer
		},

		setup(props, context){
			window.sessionStorage.setItem('UserID','')
			// onMounted(()=>{
			// 	console.log("In onMounted username = ",user.username);
			// 	console.log("In onMounted password = ",user.password);
			// 	console.log("In onMounted password = ",user.password2);
			// 	alert(user.username);
			// 	alert(user.password);
			// 	alert(user.password2)
			// });
			//数据绑定
			const user = reactive({
				username:'',
				password:''
			});

			const user1 = reactive({
				username:'',
				password:'',
				password2:''
			});

			const isLogin = reactive({
				flag:true
			}) 


			const changeType = ()=>{
				isLogin.flag = !isLogin.flag
				user1.username = ''
				user1.password = ''
				user1.password2 = ''
				user.username = ''
				user.password = ''
			};

			// function changeType(){
			// 	isLogin.flag = !isLogin.flag
			// }

			const Onlogin = ()=>{
				console.log("In Onlogin username = ",user.username);
				console.log("In Onlogin password = ",user.password);

				if(stripscript(user.username) == false || user.username == '' || user.password == false || user.password == ''){
					alert("输入信息有误，请确认后重新输入。")
				} 
				else{
					//发起请求获得结果
					do_login(user).then(resp => {
						console.log("In login resp = ",resp);
						console.log("In login resp.data.data = ",resp.data.data)
						if (resp.data.resCode == 0){
							///登录成功,保存session,跳转到用户首页
							alert('登录成功！');


							console.log("UserID = ",resp.data.data.UserID)
							//UserID保持到窗口关闭
							window.sessionStorage.setItem('UserID',resp.data.data.UserID)
							if(resp.data.data.UserType == 'u'){
								context.root.$router.push({
									path:'/',
								});
							}
							else{
								context.root.$router.push({
									path:'/Aindex',
								});
							}
							
						}
						else{
							//停留在当前页面
							alert('用户名或密码错误，请重新输入');
						}
					});
				}
			};

			const register = ()=>{
				console.log("In register username = ",user1.username);
				console.log("In register password = ",user1.password);
				console.log("In register password = ",user1.password2);

				if(stripscript(user1.username) == false || user1.username == '' || 
				user1.password == false || user1.password == ''||user1.password2 == false || user1.password2 == ''){
					alert("输入信息有误，请确认后重新输入。")
				} 
				else if(user1.password != user1.password2){
					alert("两次密码不一致，请确认后重新输入。")
				} 
				else{
					//发起请求获得结果
					do_register(user1).then(resp => {
						console.log("In register resp = ",resp);
						console.log("In register resp.data.message = ",resp.data.message)
						if (resp.data.resCode == 0){
							///登录成功,保存session,跳转到用户首页
							alert('注册成功！');
							
							isLogin.flag = !isLogin.flag;
							//console.log("UserID = ",resp.data.data.UserID)
						}
						else{
							//停留在当前页面
							alert('用户名或密码输入有误，请重新输入');
						}
					});
				}
			};

			return{
				Header,
				Footer,
				user,
				user1,
				Onlogin,
				register,
				isLogin,
				changeType
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
		width: 20%;
		height: 40px;
		border-radius: 24px;
		border: none;
		outline: none;
		background-color: rgb(57,167,176);
		color: #fff;
		font-size: 0.9em;
		cursor: pointer;
	}
	.small-box{
		width: 30%;
		height: 100%;
		background: linear-gradient(135deg,rgb(57,167,176),rgb(56,183,145));
		position: absolute;
		top: 0;
		left: 0;
		transform: translateX(0%);
		transition: all 1s;
		border-top-left-radius: inherit;
		border-bottom-left-radius: inherit;
	}
	.small-contain{
		width: 100%;
		height: 100%;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}
	.stitle{
		font-size: 1.5em;
		font-weight: bold;
		color: #fff;
	}
	.scontent{
		font-size: 0.8em;
		color: #fff;
		text-align: center;
		padding: 2em 4em;
		line-height: 1.7em;
	}
	.sbutton{
		width: 60%;
		height: 40px;
		border-radius: 24px;
		border: 1px solid #fff;
		outline: none;
		background-color: transparent;
		color: #fff;
		font-size: 0.9em;
		cursor: pointer;
	}
	
	.big-box.active{
		left: 0;
		transition: all 0.5s;
	}
	.small-box.active{
		left: 100%;
		border-top-left-radius: 0;
		border-bottom-left-radius: 0;
		border-top-right-radius: inherit;
		border-bottom-right-radius: inherit;
		transform: translateX(-100%);
		transition: all 1s;
	}
</style>




	

