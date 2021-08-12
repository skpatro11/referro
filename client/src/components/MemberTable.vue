<template>
  <table>
    <tr>
      <th>Referal Id</th>
      <th>Username</th>
      <th>Created On</th>
      <th>Active</th>
    </tr>
    <tr v-for="member in members" :key="member.id">
      <td>{{ member.id }}</td>
      <td>{{ member.username }}</td>
      <td>{{ member.program }}</td>
      <td>{{ member.is_active }}</td>
    </tr>
  </table>
</template>

<script>
export default {
  props: ["members", "prev", "next"],
};
</script>

<style>
</style>