<template>
  <canvas ref="myGraph" id="myChart" width="500" height="500"></canvas>
</template>

<script>
export default {
  props: ["data", "labels", "title"],
  data() {
    return {
      myChart: {},
      config: {},
    };
  },
  methods: {
    async load() {
      try {
        const data = {
          labels: this.labels,
          datasets: [
            {
              label: "phone pe",
              data: this.data,
              borderColor: "green",
              backgroundColor: "#B5FFDC",
            },
          ],
        };

        const config = {
          type: "line",
          data: data,
          options: {
            responsive: false,
            plugins: {
              legend: {
                position: "top",
              },
              title: {
                display: true,
                text: this.title,
              },
            },
          },
        };

        this.myChart = new Chart(this.$refs.myGraph, config);
      } catch (err) {
        console.log(err);
      }
    },
  },
  mounted() {
    this.load();
  },
  watch: {
    labels: function(newVal, oldVal) {
      console.log(oldVal)
      console.log(newVal)

      this.myChart.update()
    }
  }
};
</script>

<style>
</style>