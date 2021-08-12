<template>
  <DashboardNav />
  <div v-if="programs.length">
    <div class="programs" v-for="program in programs" :key="program.id">
      <ProgramCard :program="program" />
    </div>
  </div>
  <div v-else>
    <Spinner />
  </div>
</template>

<script>
import DashboardNav from "../DashboardNav.vue";
import ProgramCard from "../ProgramCard.vue";
import Spinner from "../Spinner.vue";
import { authInstance } from "../../services";

export default {
  components: {
    DashboardNav,
    ProgramCard,
    Spinner,
  },
  data() {
    return {
      programs: [],
    };
  },
  async mounted() {
    const res = await authInstance.get("programs/");
    this.programs = res.data;
  },
};
</script>

<style>
</style>
