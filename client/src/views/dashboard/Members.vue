<template>
  <div>
    <DashboardNav />
    <div class="programs">
      <ProgramList
        :programs="programs"
        :selectedProgram="selectedProgram"
        @selected="fetchMembers"
      />
    </div>
    <div v-if="showTable">
      <MemberTable :members="members" />
    </div>
    <div v-else-if="runSpinner">
      <Spinner />
    </div>
    <div v-else>
      <h3>There is no information Available</h3>
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
import MemberTable from "../../components/dashboard/members/MemberTable.vue";
import Spinner from "../../components/Spinner.vue";
import ProgramList from "../../components/dashboard/ProgramList.vue";
import axios from "axios";

export default {
  components: {
    DashboardNav,
    MemberTable,
    Spinner,
    ProgramList,
  },
  data() {
    return {
      programs: [],
      showTable: false,
      members: [],
      previous: null,
      next: null,
      selectedProgram: null,
      runSpinner: true,
    };
  },
  async mounted() {
    const res = await axios.get(
      `${process.env.VUE_APP_ROOT_API}/programs/`,
      {}
    );

    this.programs = res.data;

    if (this.programs.length !== 0) {
      this.fetchMembers(this.programs[0].id);
      this.selectedProgram = this.programs[0].id;
    }
    this.runSpinner = false;
  },
  methods: {
    async fetchMembers(id) {
      const res = await axios.get(
        `${process.env.VUE_APP_ROOT_API}/programs/${id}/members`,
        {
          headers: {
            Authorization: "Bearer " + localStorage.getItem("token"),
          },
        }
      );
      if (res.data) {
        this.showTable = true;
      }
      this.members = res.data.results;

      this.prev = res.data.prev;
      this.next = res.data.next;
      this.selectedProgram = id;
    },
    handlePrevious() {
      axios.get(this.previous).then(({ data }) => {
        this.members = data.results;
        this.next = data.next;
        this.previous = data.previous;
      });
    },
    handleNext() {
      axios.get(this.next).then(({ data }) => {
        this.members = data.results;
        this.next = data.next;
        this.previous = data.previous;
      });
    },
  },
};
</script>

<style>
.programs {
  display: flex;
  align-items: center;
  justify-content: flex-start;
  flex-direction: row;
}
.program {
  cursor: pointer;
  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 0px 34px;
  box-sizing: border-box;

  position: static;
  width: auto;
  height: 35px;

  background: linear-gradient(90deg, #dbffee 0%, rgba(219, 255, 238, 0) 100%);
  border: 1px solid #a8ffd6;
  box-sizing: border-box;
  border-radius: 20px;

  /* Inside Auto Layout */

  flex: none;
  order: 1;
  flex-grow: 0;
  margin: 10px 10px;
}
.selected {
  border: 1px solid #00587a;
  color: #00587a;
}
</style>