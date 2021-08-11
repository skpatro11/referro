<template>
  <DashboardNav />
  <div class="programs">
    <ProgramCard />
    <ProgramCard />
    <ProgramCard />
  </div>
</template>

<script>
import DashboardNav from "../DashboardNav.vue";
import ProgramCard from "../ProgramCard.vue";

export default {
  components: {
    DashboardNav,
    ProgramCard,
  },
};
</script>

<style>
.programs {
  /* border: 2px solid black; */
  margin-left: 5%;
}
</style>
