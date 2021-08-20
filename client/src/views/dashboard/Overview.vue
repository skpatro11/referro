<template>
  <div>
    <DashboardNav />
    <div class="order-overview">
      <ProgramList
        :programs="programs"
        :selectedProgram="selectedProgramForOrder"
        @selected="fetchGraphForOrder"
      />
      <div v-if="true">
        <LineGraph :data="data" :labels="labels" :title="title" />
      </div>
      <div v-else-if="runSpinner">
        <Spinner />
      </div>
      <div v-else>
        <h3>There is no information Available</h3>
      </div>
    </div>

    <div class="members-overview">
      <ProgramList
        :programs="programs"
        :selectedProgram="selectedProgramForMember"
        @selected="fetchGraphForMember"
      />
      <div v-if="true">
        <LineGraph :data="data" :labels="labels" :title="title" />
      </div>
      <div v-else-if="runSpinner">
        <Spinner />
      </div>
      <div v-else>
        <h3>There is no information Available</h3>
      </div>
    </div>
  </div>
</template>
<script>
import DashboardNav from "../../components/dashboard/DashboardNav.vue";
import ProgramList from "../../components/dashboard/ProgramList.vue";
import LineGraph from "../../components/dashboard/LineGraph.vue";
import Spinner from "../../components/Spinner.vue";

import { mapGetters } from "vuex";
import axios from "axios";

export default {
  components: {
    DashboardNav,
    ProgramList,
    Spinner,
    LineGraph,
  },
  computed: {
    ...mapGetters({
      user: "user",
    }),
  },
  data() {
    return {
      programs: [],
      selectedProgramForOrder: null,
      selectedProgramForMember: null,
      runSpinner: true,
      data: [10, 20, 15, 25, 50],
      labels: [
        // "10/08/2021",
        // "10/08/2021",
        // "10/08/2021",
        // "10/08/2021",
        // "10/08/2021",
      ],
      title: "Orders",
    };
  },
  methods: {
    async fetchGraphForOrder(id) {
      this.selectedProgramForOrder = id;
      axios.get(`${process.env.VUE_APP_ROOT_API}/v1/overview/programs/${id}/orders/stats`)
        .then(({data}) => {
          // console.log(Object.keys(data))
          this.labels = Object.keys(data)
        })
    },
    async fetchGraphForMember(id) {
      this.selectedProgramForMember = id;
    },
  },
  async mounted() {
    const res = await axios.get(
      `${process.env.VUE_APP_ROOT_API}/v1/programs/`,
      {}
    );

    this.programs = res.data.results;

    if (this.programs.length !== 0) {
      this.selectedProgramForOrder = this.programs[0].id;
      this.selectedProgramForMember = this.programs[0].id;
      this.fetchGraphForOrder(this.programs[0].id);
      this.fetchGraphForMember(this.programs[0].id);
    }
    this.runSpinner = false;
  },
};
</script>

<style>
</style>