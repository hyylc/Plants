<template>
  <header>
      <h1>{{title}}</h1>
      <button @click="gotolink" class="btn btn-success">登录</button>
  </header>
</template>

<script>
export default {
  name: 'app-header',
  data(){
    return{
      title:"plant"
    }
  },
   methods:{
        gotolink(){
          //指定跳转地址
          this.$router.replace('/Signin')
        }
      }
}
</script>

<style scoped>
header {
  background: rgb(57,167,176);;
  padding: 10px;
}
h1 {
  color: #222;
  text-align: center;
}
button {
    background-color: #4CAF50;
    border: none;
    color: white;
    display: inline-block;
    font-size: 16px;
}
</style>
