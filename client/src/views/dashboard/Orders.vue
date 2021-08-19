<template>
  <div class="mb-3">
    <DashboardNav />
    <ProgramList
      :programs="programs"
      :selectedProgram="selectedProgram"
      @selected="fetchOrders"
    />
    <div v-if="showTable">
      <OrderTable :orders="orders" />
    </div>
    <div v-else-if="runSpinner">
      <Spinner />
    </div>
    <div v-else>
      <h3>There is no information Available</h3>
    </div>
    <div class="page">
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
import ProgramList from "../../components/dashboard/ProgramList.vue";
import axios from "axios";

export default {
  components: {
    DashboardNav,
    OrderTable,
    Spinner,
    ProgramList,
  },
  data() {
    return {
      programs: [],
      next: null,
      previous: null,
      orders: [],
      showTable: false,
      selectedProgram: null,
      runSpinner: true,
    };
  },
  async mounted() {
    const res = await axios.get(
      `${process.env.VUE_APP_ROOT_API}/v1/programs/`,
      {}
    );

    this.programs = res.data.results;
    if (this.programs.length !== 0) {
      this.selectedProgram = this.programs[0].id;
      this.fetchOrders(this.programs[0].id);
    }
    this.runSpinner = false;
  },
  methods: {
    async fetchOrders(id) {
      const res = await axios.get(
        `${process.env.VUE_APP_ROOT_API}/v1/orders/list/?program_id=${id}`,
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
.page {
  margin: 10px auto;
  display: flex;
  width: 20%;
  height: 40px;
  flex-direction: row;
  align-items: center;
  justify-content: space-evenly;
}
</style>