<template>
  <div id="nav">
    <router-link v-if="currentRouteName === 'Docs'" class="brand" to="/docs"
      >Referro <span class="docs">DOCS</span>
    </router-link>
    <router-link v-else class="brand" to="/">Referro</router-link>
    <div class="actions">
      <router-link to="/">Home</router-link>
      <router-link to="/dashboard/programs">Dashboard</router-link>
      <router-link to="/about">About</router-link>
      <router-link to="/docs">Docs</router-link>
      <router-link v-if="!loggedIn" to="/auth/login">Login</router-link>
      <span v-if="loggedIn" id="logout">
        <span @click="handleLogout">Logout</span>
        <img class="mx-2" src="../assets/Frame-2.svg" alt="" />
        <svg
          xmlns="http://www.w3.org/2000/svg"
          width="20"
          height="20"
          fill="currentColor"
          class="bi bi-box-arrow-right d-none"
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
import { mapGetters } from "vuex";

export default {
  computed: {
    ...mapGetters({
      loggedIn: "loggedIn",
    }),
    currentRouteName() {
      return this.$route.name;
    },
  },
  methods: {
    handleLogout() {
      this.$store.dispatch("logout");
      this.$router.push({ name: "Home" });
    },
  },
};
</script>

<style>
#logout {
  cursor: pointer;
  margin-left: 10px;
  color: var(--clr-dark);
}
.docs {
  color: var(--clr-text);
}
</style>