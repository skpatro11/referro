<template>
  <DashboardNav />
  <div class="programs">
    <div
      class="program"
      v-for="program in programs"
      :key="program.id"
      @click="fetchMembers(program.id)"
    >
      {{ program.name }}
    </div>
  </div>
  <div v-if="showTable">
    <MemberTable :members="members" :prev="prev" :next="next" />
  </div>
</template>

<script>
import DashboardNav from "../DashboardNav.vue";
import MemberTable from "../MemberTable.vue";
import { authInstance } from "../../services/";

export default {
  components: {
    DashboardNav,
    MemberTable,
  },
  data() {
    return {
      programs: [],
      showTable: false,
      members: [],
      prev: null,
      next: null,
    };
  },
  async mounted() {
    const res = await authInstance.get("programs/");
    this.programs = res.data;
    if (this.programs) {
      this.fetchMembers(this.programs[0].id);
    }
  },
  methods: {
    async fetchMembers(id) {
      const res = await authInstance.get(`programs/${id}/members/`);
      if (res.data) {
        this.showTable = true;
      }
      this.members = res.data.results;
      this.prev = res.data.prev;
      this.next = res.data.next;
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
</style>