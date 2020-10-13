<template>
  <div class="home">
    <Header />
    <b-container>
      <div style="height:1000px;background-color:red">
        body部分
      </div>
    </b-container>

    <b-container>
      <div style="height:50px;background-color:blue">
        footer部分
      </div>
    </b-container>
  </div>
</template>

<script>
import Header from "../components/Header.vue"
export default {
  name: "home",
  components: {
    Header
  }
};
</script>
