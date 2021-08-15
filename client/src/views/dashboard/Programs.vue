<template>
  <div class="">
    <DashboardNav />
    <ProgramCreate />
    <div v-if="programs.length">
      <div class="programs" v-for="program in programs" :key="program.id">
        <ProgramCard :program="program" />
      </div>
    </div>
    <div v-else-if="runSpinner">
      <Spinner />
    </div>
    <div v-else>
      <h3>There is no information Available</h3>
    </div>
  </div>
</template>

<script>
import DashboardNav from "../../components/dashboard/DashboardNav.vue";
import ProgramCard from "../../components/dashboard/programs/ProgramCard.vue";
import ProgramCreate from "../../components/dashboard/programs/ProgramCreate.vue";
import Spinner from "../../components/Spinner.vue";
import axios from "axios";

export default {
  components: {
    DashboardNav,
    ProgramCard,
    ProgramCreate,
    Spinner,
  },
  data() {
    return {
      programs: [],
      runSpinner: true,
    };
  },
  async mounted() {
    const res = await axios.get(
      `${process.env.VUE_APP_ROOT_API}/programs/`,
      {}
    );
    this.programs = res.data;
    this.runSpinner = false;
  },
};
</script>

<style scoped>
</style>
