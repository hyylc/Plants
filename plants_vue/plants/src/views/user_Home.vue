<template>
  <div class="home">
    <Header />
    <ul>
      <li>
        
         <a href='/Monocotyledoneae'>单子叶植物纲</a>
         
      </li>
    </ul>
    <Footer />

  </div>
</template>


<script>
import Header from "../components/Header.vue"
import Footer from "../components/Footer.vue"
export default {
  name: "home",
  components: {
    Header,
    Footer
  },
  data() {
    return{
      plants:[
        {name:"梧桐",position:"被子植物",show:false},
        {name:"蒲公英",position:"裸子植物",show:false},
        {name:"牵牛花",position:"被子植物",show:false},
        {name:"百合",position:"被子植物",show:false},
        {name:"杨树",position:"被子植物",show:false},
        {name:"柳树",position:"被子植物",show:false} 
      ]
    }
  }
};
</script>


<style scoped>
.home{
  width: 100%;
  max-width: 1200px;
  margin: 40px auto;
  padding: 0 20px;
  box-sizing:border-box;
}
ul {
  display: flex;
  flex-wrap: wrap;
  list-style-type: none;
  padding: 0;
}
li {
  flex-grow: 1;
  flex-basis: 200px;
  text-align: center;
  padding: 30px;
  border: 1dx solid #222;
  margin: 10px;
}
</style>
