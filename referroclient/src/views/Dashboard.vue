<template>
  <DashboardNav />
</template>

<script>
import DashboardNav from "../components/DashboardNav.vue";

export default {
  components: {
    DashboardNav,
  },
};
</script>

<style>
.dashboard-actions {
  /* border: 2px solid black; */
  padding: 5px 0px;
  width: 70%;
  display: flex;
  flex-direction: row;
  margin-left: 5%;
  border-bottom: 1px solid rgba(0, 140, 74, 0.2);
}
/* .dashboard-actions li {
  text-decoration: none;
  list-style-type: none;
}
.dashboard-actions li a {
  font-size: 18px;
} */
</style>