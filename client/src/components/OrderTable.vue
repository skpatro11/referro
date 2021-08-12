<template>
  <table>
    <tr>
      <th>Member Id</th>
      <th>Program</th>
      <th>Claim Amount</th>
      <th>Charge Amount</th>
      <th>Status</th>
      <th>Created On</th>
    </tr>
    <tr v-for="order in orders" :key="order.id">
      <td>{{ order.member }}</td>
      <td>{{ order.program }}</td>
      <td>{{ order.claim_amount }}</td>
      <td>{{ order.charge_amount }}</td>
      <td>{{ order.status }}</td>
      <td>{{ order.created_at }}</td>
    </tr>
  </table>
</template>

<script>
export default {
  props: ["orders"],
};
</script>

<style>
</style>