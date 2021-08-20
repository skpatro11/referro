<template>
  <div>
    <DashboardNav />
    <div class="order-overview">
      <ProgramList
        :programs="programs"
        :selectedProgram="selectedProgramForOrder"
        @selected="fetchGraphForOrder"
      />
      <div v-if="showOrderGraph">
        <LineGraph :graphData="orderData" />
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
      <div v-if="showMemberGraph">
        <LineGraph :graphData="memberData" />
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
      runSpinner1: true,
      runSpinner2: true,
      showOrderGraph: false,
      showMemberGraph: false,
      orderData: {
        data: [],
        labels: [],
        title: "Orders",
      },
      memberData: {
        data: [],
        labels: [],
        title: "Members",
      },
    };
  },
  methods: {
    async fetchGraphForOrder(id) {
      this.runSpinner1 = true;
      this.selectedProgramForOrder = id;
      axios
        .get(
          `${process.env.VUE_APP_ROOT_API}/v1/overview/programs/${id}/orders/stats`
        )
        .then(({ data }) => {
          this.orderData.data = Object.values(data);
          this.orderData.labels = Object.keys(data);
          this.showOrderGraph = true;
          this.runSpinner1 = false;
        })
        .catch((err) => {
          this.runSpinner1 = false;
        });
    },
    async fetchGraphForMember(id) {
      this.runSpinner2 = true;
      this.selectedProgramForMember = id;
      axios
        .get(
          `${process.env.VUE_APP_ROOT_API}/v1/overview/programs/${id}/members/stats`
        )
        .then(({ data }) => {
          this.memberData.data = Object.values(data);
          this.memberData.labels = Object.keys(data);
          this.showMemberGraph = true;
          this.runSpinner2 = false;
        })
        .catch((err) => {
          this.runSpinner2 = false;
        });
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
  },
};
</script>

<style>
</style>