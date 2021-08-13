<template>
  <div
    class="program"
    v-for="program in programs"
    :key="program.id"
    @click="fetchData(program.id)"
    :class="[selectedProgram === program.id ? 'selected' : '']"
  >
    {{ program.name }}
  </div>
</template>

<script>
export default {
  props: ["programs", "selectedProgram"],
  methods: {
    fetchData(id) {
      this.$emit("selected", id);
    },
  },
};
</script>

<style>
</style>