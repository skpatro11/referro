<template>
  <div id="nav">
    <div class="brand">Referro</div>
    <div class="actions">
      <router-link to="/">Home</router-link>
      <router-link to="/auth">Auth</router-link>
      <router-link v-if="isAuthenticated" to="/dashboard/programs"
        >Dashboard</router-link
      >
      <router-link to="/contact">Contact</router-link>
      <router-link to="/about">About</router-link>
      <span v-if="isAuthenticated" id="logout" @click="handleLogout"
        ><svg
          xmlns="http://www.w3.org/2000/svg"
          width="16"
          height="16"
          fill="currentColor"
          class="bi bi-box-arrow-right"
          viewBox="0 0 16 16"
        >
          <path
            fill-rule="evenodd"
            d="M10 12.5a.5.5 0 0 1-.5.5h-8a.5.5 0 0 1-.5-.5v-9a.5.5 0 0 1 .5-.5h8a.5.5 0 0 1 .5.5v2a.5.5 0 0 0 1 0v-2A1.5 1.5 0 0 0 9.5 2h-8A1.5 1.5 0 0 0 0 3.5v9A1.5 1.5 0 0 0 1.5 14h8a1.5 1.5 0 0 0 1.5-1.5v-2a.5.5 0 0 0-1 0v2z"
          />
          <path
            fill-rule="evenodd"
            d="M15.854 8.354a.5.5 0 0 0 0-.708l-3-3a.5.5 0 0 0-.708.708L14.293 7.5H5.5a.5.5 0 0 0 0 1h8.793l-2.147 2.146a.5.5 0 0 0 .708.708l3-3z"
          /></svg
      ></span>
    </div>
  </div>
</template>

<script>
export default {
  computed: {
    isAuthenticated() {
      console.log(this.$store.state.isAuthenticated);
      return this.$store.state.isAuthenticated;
    },
  },
  methods: {
    handleLogout() {
      this.isAuthenticated = false;
      this.$store.state.isAuthenticated = false;
      localStorage.removeItem("token");
      this.$router.push({ name: "Home" });
    },
  },
};
</script>

<style>
#logout {
  cursor: pointer;
  margin-left: 10px;
  color: #0f3057;
}
</style>