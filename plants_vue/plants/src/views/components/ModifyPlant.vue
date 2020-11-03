<template>
	<div class="login-register">
		<div class="contain">
					<div class="btitle">修改植物信息</div>
					<div class="bform">
						<p><span>植物名称:</span><input type="text" placeholder="植物名称" v-model="form.username"></p>
						<p><span>植物性状:</span><input type="sex" placeholder="植物性状" v-model="form.userpwd"></p>
						<p><span>门:</span><input type="door1" placeholder="门" v-model="form.userpwdz"></p>
						<p><span>纲:</span><input type="door2" placeholder="纲" v-model="form.userpwdz"></p>
						<p><span>目:</span><input type="door3" placeholder="目" v-model="form.userpwdz"></p>
						<p><span>科:</span><input type="door4" placeholder="科" v-model="form.userpwdz"></p>
						<p><span>属:</span><input type="door5" placeholder="属" v-model="form.userpwdz"></p>
						<p><span>种:</span><input type="door6" placeholder="种" v-model="form.userpwdz"></p>
						<p><span>植物分布:</span><input type="where" placeholder="植物分布" v-model="form.userpwd"></p>
						<p><span>发布时间:</span><input type="pushtime" placeholder="发布时间" v-model="form.userpwdz"></p>
					</div>
					<button class="bbutton" @click="login">保存设置</button>
			

			
		</div>
	</div>
</template>

<script>
	export default{
		name:'login-register',
		data(){
			return {
				isLogin:false,
				existed: false,
				form:{
					username:'',
					useremail:'',
					userpwd:''
				}
			}
		},
		methods:{
			changeType() {
			},
			login() {
              this.$router.replace('/Resetuserinfo')
			},
			register(){

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
