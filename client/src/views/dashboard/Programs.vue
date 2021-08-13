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
import DashboardNav from "../../components/DashboardNav.vue";
import ProgramCard from "../../components/ProgramCard.vue";
import Spinner from "../../components/Spinner.vue";
import axios from "axios";

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
    const res = await axios.get("https://referro.herokuapp.com/programs/", {
    });
    this.programs = res.data;
  },
};
</script>

<style>
</style>
