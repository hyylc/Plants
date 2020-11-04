<template>
  <div id="userinfo">
      <Header />
      <b-container>
          <div class="contain">
              <div class="btitle">个人资料</div>
              <ul>
                <li v-for="item in user.userinfo" :key="item.UserID">
                    <div class="bform">
						<p><span>昵称:</span><a>{{item.UserName}}</a></p>
						<p><span>用户类别:</span><a>{{item.UserType}}</a></p>
						<p><span>注册时间:</span><a>{{item.RegisterTime}}</a></p>
					</div>
                </li>
               </ul>
               <button class="bbutton" @click="changeinfo">修改信息</button>	
               <button class="bbutton" @click="changepass">修改密码</button>						
		  </div>
      </b-container>
      <Footer />
  </div>
</template>

<script>
import Header from "../components/Header";
import Footer from "../components/Footer";
import { reactive, ref, onMounted} from "@vue/composition-api";//ref定义常量;reactive定义对象
import { Get_userinfo } from "../apis/read.js"

export default{
    name : "userinfo",
    components:{
        Header,
        Footer
    },
    setup(props, context){
        const now_url = ref(context.root.$route.path)//ref用.value才能获取到url值
        console.log("now_url = ",now_url.value)//确实在value里面

        const user = reactive({
            userinfo:[]
        });

      
        const changeinfo = ()=>{
			 context.root.$router.push({
                        path:'/Resetuserinfo',
             });
        };
         const changepass = ()=>{
			 context.root.$router.push({
                        path:'/Resetpassword',
             });
		};
    

        const userparam = reactive({
            userID : ''
        });
        
        
    

        //获取已登录的用户信息
        userparam.userID = window.sessionStorage.UserID
        console.log("In user userID get from winsow.sessionStorage = ",userparam.userID)

        //发起请求获得结果
        Get_userinfo(userparam).then(resp => {
            console.log('打印返回结果');
            console.log("resp = ",resp);
            user.userinfo = resp.data.data;
            console.log("user.userinfo = ",user.userinfo);
        });

        onMounted(()=>{
            console.log("In user context = ", context.root.$route.path)//获取地址
        });

        return {
            user,
            changeinfo,
            changepass
        }
    }
}
</script>


<style lang='scss' scoped>//lang告诉解释其css符合什么编译器的语法；scoped：当前vue文件生效，没有scoped则全局生效
.login-register{
		width: 100vw;
		height: 100vh;
		box-sizing: border-box;
	}
	.contain{
		width: 60%;
		height: 60%;
		position: relative;
        
        margin-top: 200px;
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
    li{
        list-style: none;
    }
    p{
        text-align: left;
        font-size: 1.2rem;
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
        margin-left: auto;
        margin-right: auto;
        text-align: center;
		cursor: pointer;
	}

</style>