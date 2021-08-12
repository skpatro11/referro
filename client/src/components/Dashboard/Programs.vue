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
      headers: {
        Authorization: "Bearer " + localStorage.getItem("token"),
      },
    });
    this.programs = res.data;
  },
};
</script>

<style>
</style>
