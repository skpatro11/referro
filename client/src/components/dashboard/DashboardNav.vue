<template>
  <div class="dashboard-nav">
    <div class="dashboard-actions">
      <router-link class="router" :to="{ name: 'Overview' }"
        >Overview</router-link
      >
      <router-link class="router" :to="{ name: 'Programs' }"
        >Programs</router-link
      >
      <router-link class="router" :to="{ name: 'Members' }"
        >Members</router-link
      >
      <router-link class="router" :to="{ name: 'Orders' }">Orders</router-link>
      <router-link class="router" :to="{ name: 'Billing' }"
        >Billing</router-link
      >
      <router-link class="router" :to="{ name: 'Support' }"
        >Support</router-link
      >
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped>
.dashboard-actions {
  width: 70%;
  display: flex;
  flex-direction: row;
  border-bottom: 1px solid rgba(0, 140, 74, 0.2);
}

.router {
  display: block;
  margin-bottom: 0;
  padding-bottom: 10px;
}
.router:hover {
  color: hsla(152, 100%, 22%, 1);
}
.router-link-active {
  border-bottom: 2px solid var(--clr-dark);
}
</style>
