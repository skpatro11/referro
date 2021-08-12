<template>
  <DashboardNav />
  <div class="programs">
    <div
      class="program"
      v-for="program in programs"
      :key="program.id"
      @click="fetchOrders(program.id)"
    >
      {{ program.name }}
    </div>
  </div>
  <div v-if="showTable">
    <OrderTable :orders="orders" />
  </div>
</template>

<script>
import DashboardNav from "../DashboardNav.vue";
import OrderTable from "../OrderTable.vue";
import { authInstance } from "../../services";

export default {
  components: {
    DashboardNav,
    OrderTable,
  },
  data() {
    return {
      programs: [],
      orders: [],
      showTable: false,
    };
  },
  async mounted() {
    const res = await authInstance.get("programs/");
    this.programs = res.data;
    if (this.programs) {
      this.fetchOrders(this.programs[0].id);
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
    },
  },
};
</script>

<style>
</style>