<template>
  <DashboardNav />
  <div>{{ token }}</div>
</template>

<script>
import DashboardNav from "../DashboardNav.vue";

export default {
  components: {
    DashboardNav,
  },
  data() {
    return {
      token: localStorage.getItem("token"),
    };
  },
};
</script>

<style>
</style>