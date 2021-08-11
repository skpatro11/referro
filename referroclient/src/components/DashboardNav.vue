<template>
  <div class="dashboard-nav">
    <div class="dashboard-actions">
      <router-link :to="{ name: 'Overview' }">Overview</router-link>
      <router-link :to="{ name: 'Programs' }">Programs</router-link>
      <router-link :to="{ name: 'Members' }">Members</router-link>
      <router-link :to="{ name: 'Orders' }">Orders</router-link>
      <router-link :to="{ name: 'Billing' }">Billing</router-link>
      <router-link :to="{ name: 'Support' }">Support</router-link>
    </div>
  </div>
</template>

<script>
export default {};
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
</style>