<template>
  <DashboardNav />
  <div class="programs">
    <div
      class="program"
      v-for="program in programs"
      :key="program.id"
      @click="fetchOrders(program.id)"
      :class="[selectedProgram === program.id ? 'selected' : '']"
    >
      {{ program.name }}
    </div>
  </div>
  <div v-if="showTable">
    <OrderTable :orders="orders" />
  </div>
  <div v-else>
    <Spinner />
  </div>
</template>

<script>
import DashboardNav from "../DashboardNav.vue";
import OrderTable from "../OrderTable.vue";
import Spinner from "../Spinner.vue";
import axios from "axios";

export default {
  components: {
    DashboardNav,
    OrderTable,
    Spinner,
  },
  data() {
    return {
      programs: [],
      orders: [],
      showTable: false,
      selectedProgram: null,
    };
  },
  async mounted() {
    const res = await axios.get("https://referro.herokuapp.com/programs/", {
      headers: {
        Authorization: "Bearer " + localStorage.getItem("token"),
      },
    });

    this.programs = res.data;
    if (this.programs) {
      this.fetchOrders(this.programs[0].id);
      this.selectedProgram = this.programs[0].id;
    }
  },
  methods: {
    async fetchOrders(id) {
      const res = await axios.get(
        `https://referro.herokuapp.com/programs/${id}/orders/`,
        {
          headers: {
            Authorization: "Bearer " + localStorage.getItem("token"),
          },
        }
      );
      if (res.data) {
        this.showTable = true;
      }
      this.orders = res.data.results;
      this.selectedProgram = id;
    },
  },
};
</script>

<style>
</style>