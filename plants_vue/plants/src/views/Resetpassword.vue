<template>
	<div class="login-register">
      <Header />
		<div class="contain">
					<div class="btitle">修改密码</div>
					<div class="bform">
						<input type="text" placeholder="输入密码" v-model="user.userpwd">
						<input type="text" placeholder="输入新密码" v-model="user.newuserpwd">
						<input type="text" placeholder="再次输入新密码" v-model="user.renewuserpwd">
					</div>
					<button class="bbutton" @click="changepass">修改密码</button>
		</div>
		<Footer />
	</div>
</template>

<script>
import Header from "../components/Header";
import Footer from "../components/Footer";
import { stripscript } from "../apis/validate";
import { reactive, ref, onMounted} from "@vue/composition-api";//ref定义常量;reactive定义对象
import { Get_userinfo } from "../apis/read";
import { Reset_userpwd } from "../apis/read";

	export default{
		name:'login-register',
		components:{
			Header,
			Footer
		},
		setup(props, context){

			const user = reactive({
				userpwd : '',
				newuserpwd : '',
				renewuserpwd : '',
				userID : ''
			});

			const getuser = reactive({
				password : ''
			});

			user.userID = window.sessionStorage.UserID
            console.log('In Reset user.userID = ',user.userID)
			
			Get_userinfo(user).then(resp => {
				console.log("In reset response.data.data.UserPassword = ",resp.data.data[0].UserPassword)
				console.log("In reset user.userpwd = ",user.userpwd)
				getuser.password = resp.data.data[0].UserPassword
				
			});

			const changepass = ()=>{// == false????这里要修改，用stripscript判断有没有非法字符
				if(stripscript(user.userpwd) == false || user.userpwd == ''||stripscript(user.newuserpwd) == false || user.newuserpwd == ''||stripscript(user.renewuserpwd) == false || user.renewuserpwd == ''
				){
               		alert("输入信息有误，请确认后重新输入。")
				}
				else if(user.newuserpwd != user.renewuserpwd ){
               		alert("两次输入密码不一致，请确认后重新输入。")
				}
				else if ((user.userpwd != getuser.password)){
					alert("原密码错误，请确认后重新输入。")
				}
				else{
					//发起请求获得结果
					//这里的函数时并发运行的，不能写在一起。
					//resp是接口最后的返回值，不能接口套接口，所以把get_userinfo写在前面了
					Reset_userpwd(user).then(resp => {
						console.log("In reset resp.data.data = ",resp.data.data)
						if (resp.data.resCode == 0){
							alert('修改成功');
							//修改成功后跳回个人中心
							context.root.$router.push({
                            	path:'/userinfo/'+user.userID
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
				changepass
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
