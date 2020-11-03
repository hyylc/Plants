<template>
  <footer>
      <p>{{copyright}}</p>
  </footer>
</template>

<script>
export default {
  name: 'app-footer',
  data(){
    return{
      copyright:"plant 2020 hyy txj"
    }
  }
}
</script>

<style scoped>
footer {
  background:#222;
  padding: 3px;
}
p {
  color:rgb(57,167,176);;
  text-align: center;
}

</style>
