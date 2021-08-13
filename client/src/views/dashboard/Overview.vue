<template>
  <div>
    <DashboardNav />
    <div>Hi,</div>
  </div>
</template>

<script>
import DashboardNav from "../../components/dashboard/DashboardNav.vue";
import { mapGetters } from "vuex";

export default {
  components: {
    DashboardNav,
  },
  computed: {
    ...mapGetters({
      user: "user",
    }),
  },
  data() {
    return {
      profile: null,
    };
  },
};
</script>

<style>
</style>