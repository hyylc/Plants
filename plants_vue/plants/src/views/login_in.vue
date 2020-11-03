<template>
  <div id="login_in">
      <Header />
      <b-container>
        <div style="height:2000px;background-color:pink">
            //注册登录界面
            <input v-model="user.username" type="text" placeholder="输入用户名" class="mr-sm-2 from-control-sm">
             <input v-model="user.password" type="text" placeholder="输入密码" class="mr-sm-2 from-control-sm">
            <button @click="Onlogin"  type="submit" class="btn my-2 my-sm-0 btn-secondary btn-sm">登录</button>
        </div>

      </b-container>
      <Footer />
  </div>
</template>

<script>
import Header from "../components/Header";
import Footer from "../components/Footer";
import { stripscript } from "../apis/validate.js"
import { reactive, ref, onMounted} from "@vue/composition-api";//ref定义常量;reactive定义对象
import { do_login } from "../apis/read.js"

export default{
    name : "login_in",
    components:{
        Header,
        Footer
    },
    setup(props, context){
         

        onMounted(()=>{
            console.log("In onMounted username = ",user.username);
            console.log("In onMounted password = ",user.password);
            alert(user.username);
            alert(user.password)
        });
        //数据绑定
        const user = reactive({
            username:'',
            password:''
        });


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
                        console.log("UserID = ",resp.data.data.UserID)
                        //UserID保持到窗口关闭
                        window.sessionStorage.setItem('UserID',resp.data.data.UserID)
                        context.root.$router.push({
                            path:'/',
                        });
                        
                    }
                    else{
                        //停留在当前页面
                        alert('用户名或密码错误，请重新输入');
                    }
                });
            }
        };

        return{
            Header,
            Footer,
            user,
            Onlogin
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