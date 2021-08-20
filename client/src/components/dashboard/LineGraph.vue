<template>
  <canvas ref="myGraph" id="myChart" width="1000" height="500"></canvas>
</template>

<script>
export default {
  props: ["graphData"],
  data() {
    return {
      myChart: {},
      config: {},
    };
  },
  watch: {
    graphData: {
      deep: true,
      handler() {
        console.log(this.graphData);
        this.myChart.destroy();
        this.load();
      },
    },
  },
  methods: {
    async load() {
      try {
        console.log(this.graphData);

        const data = {
          labels: this.graphData.labels,
          datasets: [
            {
              label: "phone pe",
              data: this.graphData.data,
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
                text: this.graphData.title,
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
};
</script>

<style>
</style>