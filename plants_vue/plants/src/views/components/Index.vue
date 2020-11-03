<template>
  <div class="index">
    <h1>Hello Users</h1>
    <ul>
      <li v-for="plant in plants" :key="plant.num"
          v-on:click="plant.show =!plant.show">
          <h2>{{plant.name}}</h2>
          <h3 v-show="plant.show">{{plant.position}}</h3>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'index',
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
}
</script>

<style scoped>
.plant{
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
