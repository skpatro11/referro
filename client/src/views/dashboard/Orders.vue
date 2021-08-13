<template>
  <div class="mb-3">
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
    <div id="page">
      <button
        class="btn btn-sm btn-outline-success"
        v-if="previous"
        @click="handlePrevious"
      >
        previous
      </button>
      <button
        class="btn btn-sm btn-outline-success"
        v-if="next"
        @click="handleNext"
      >
        Next
      </button>
    </div>
  </div>
</template>

<script>
import DashboardNav from "../../components/dashboard/DashboardNav.vue";
import OrderTable from "../../components/dashboard/orders/OrderTable.vue";
import Spinner from "../../components/Spinner.vue";
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
      next: null,
      previous: null,
      orders: [],
      showTable: false,
      selectedProgram: null,
    };
  },
  async mounted() {
    const res = await axios.get(
      `${process.env.VUE_APP_ROOT_API}/programs/`,
      {}
    );

    this.programs = res.data;
    if (this.programs) {
      this.fetchOrders(this.programs[0].id);
      this.selectedProgram = this.programs[0].id;
    }
  },
  methods: {
    async fetchOrders(id) {
      const res = await axios.get(
        `${process.env.VUE_APP_ROOT_API}/programs/${id}/orders/`,
        {
          headers: {
            Authorization: "Bearer " + localStorage.getItem("token"),
          },
        }
      );
      if (res.data) {
        this.showTable = true;
      }

      this.next = res.data.next;
      this.previous = res.data.previous;

      this.orders = res.data.results;
      this.selectedProgram = id;
    },
    handlePrevious() {
      axios.get(this.previous).then(({ data }) => {
        this.orders = data.results;
        this.next = data.next;
        this.previous = data.previous;
      });
    },
    handleNext() {
      axios.get(this.next).then(({ data }) => {
        this.orders = data.results;
        this.next = data.next;
        this.previous = data.previous;
      });
    },
  },
};
</script>

<style>
</style>