<template>
  <div class="table-container">
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
  </div>
</template>

<script>
export default {
  props: ["orders"],
};
</script>

<style>
.table-container {
  display: table;
  background: var(--clr-primary);
  border: 1px solid #a8ffd6;
  border-radius: 5px;
  padding: 1.1em 1.5em;
}
table {
  border-collapse: collapse;
  color: var(--clr-text);
}

.table-container td,
.table-container th {
  text-align: start;
  padding: 0.8rem;
}

th {
  border-bottom: 1px solid var(--clr-text);
  font-size: 1.12em;
}

td {
  border-bottom: 1px solid rgba(0, 112, 59, 0.2);
  /* padding: 1rem 0; */
}

tr:hover {
  background: #cfffea;
}
</style>
