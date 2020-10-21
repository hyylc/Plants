<template>
  <div class="home">
    <Header />
    <b-container>
      <div style="height:1000px;background-color:white">
        body部分
         <a href='/Dicotyledoneae'>双子叶植物纲</a>
      </div>
    </b-container>
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
  }
};
</script>
