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
import { authInstance } from "../../services";

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
    const res = await authInstance.get("programs/");
    this.programs = res.data;
    if (this.programs) {
      this.fetchOrders(this.programs[0].id);
      this.selectedProgram = this.programs[0].id;
    }
  },
  methods: {
    async fetchOrders(id) {
      console.log("orders called");
      const res = await authInstance.get(`programs/${id}/orders`);
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