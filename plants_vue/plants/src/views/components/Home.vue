<template>
  <div id="home">
  <app-header></app-header>
  <index></index>
  <app-footer></app-footer>
  </div>
</template>

<script>
import  Index from './Index'
import  Header from './Header'
import  Footer from './Footer'

export default {
  name: 'home',
  data(){
    return{
      title:"hello"
    }
  },
  components:{
    "index":Index,
    "app-header":Header,
    "app-footer":Footer
  }
}
</script>

<style scoped>
h1{
  color:purple;
}
</style>
