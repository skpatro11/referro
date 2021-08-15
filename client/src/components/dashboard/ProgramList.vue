<template>
  <div class="programs">
    <div
      class="program"
      v-for="program in programs"
      :key="program.id"
      @click="fetchData(program.id)"
      :class="[selectedProgram === program.id ? 'selected' : '']"
    >
      {{ program.name }}
    </div>
  </div>
</template>

<script>
export default {
  props: ["programs", "selectedProgram"],
  emits: ["selected"],
  methods: {
    fetchData(id) {
      this.$emit("selected", id);
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
  border: 2px dotted var(--clr-dark);
  color: #00587a;
}
</style>