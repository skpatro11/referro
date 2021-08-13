<template>
  <div class="d-flex align-items-center justify-content-between">
    <div class="process-content d-flex flex-column text-start ms-5">
      <h4>{{ title }}</h4>
      <p>
        {{ desc }}
      </p>
    </div>
    <div
      class="step-circle d-flex align-items-center justify-content-center m-5"
    >
      {{ step }}
    </div>
    <img :src="require(`../../assets/${image}`)" class="img-fluid" />
  </div>
</template>

<script>
export default {
  name: "ProcessAlter",
  props: ["image", "step", "title", "desc"],
  components: {},
};
</script>

<style></style>
