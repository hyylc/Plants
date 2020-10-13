<template>
  <div class="home">
    <Header />
    <b-container>
      <div style="height:1000px;background-color:red">
        body部分
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
