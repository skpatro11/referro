<template>
  <div class="container">
    <Nav />
    <router-view />
  </div>
</template>

<script>
import Nav from "../src/components/Nav.vue";

export default {
  components: {
    Nav,
  },
  created() {
    const tokenString = localStorage.getItem("token");
    if (tokenString) {
      this.$store.commit("SET_AUTH_TOKEN", tokenString);
      this.$store.dispatch("setUser");
    }
  },
};
</script>


<style>
#app {
  /* -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale; */
  text-align: center;
  color: #2c3e50;
}
#nav {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 20px auto;
}
.brand {
  color: #0f3057;
  font-size: 25px;
  font-weight: bold;
  cursor: pointer;
}
a {
  color: black;
  text-decoration: none;
  font-size: 18px;
  margin: 5px 10px;
}
.router-link-active {
  color: #0f3057;
  font-weight: bold;
}
</style>
