<template>
  <DashboardNav />
  <div>Hi, {{ user }}</div>
</template>

<script>
import DashboardNav from "../../components/DashboardNav.vue";
import { mapGetters } from 'vuex'


export default {
  components: {
    DashboardNav,
  },
  computed: {
    ...mapGetters({
      user: 'user'
    })
  },
  data() {
    return {
      profile: null
    };
  },
};
</script>

<style>
</style>