<template>
  <div class="text-start">
    <button
      type="button"
      class="btn"
      data-bs-toggle="modal"
      data-bs-target="#exampleModal"
    >
      Create New Program
    </button>

    <!-- Modal -->
    <div
      class="modal fade"
      id="exampleModal"
      tabindex="-1"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content">
          <div class="modal-body">
            <div class="d-flex justify-content-between">
              <h2 class="mb-4">Create a referral program</h2>
              <button
                type="button"
                class="btn-close"
                data-bs-dismiss="modal"
                aria-label="Close"
              ></button>
            </div>
            <form @submit="createProgram">
              <div class="mb-3">
                <label for="program-name" class="form-label"
                  >Program Name</label
                >
                <input
                  type="text"
                  v-model="name"
                  class="form-control input-field"
                  id="program-name"
                  required="true"
                />
              </div>
              <div class="mb-3">
                <label for="incentive" class="form-label">Incentive</label>
                <input
                  v-model="incentive"
                  type="number"
                  class="form-control input-field"
                  id="password"
                  required="true"
                />
              </div>
              <button type="submit" class="btn mt-2">Create</button>
            </form>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      name: null,
      incentive: null,
    };
  },
  methods: {
    async createProgram() {
      const res = await axios.post(
        `${process.env.VUE_APP_ROOT_API}/programs/`,
        {
          name: this.name,
          incentive: parseFloat(this.incentive),
        }
      );

      console.log(res.data);
    },
  },
};
</script>

<style scoped>
.modal-lg {
  max-width: 600px;
  border-radius: 10px;
}
.modal-body {
  background: #dbffee;
  border: 1px solid #a8ffd6;
  box-shadow: 0px 3px 10px rgba(0, 0, 0, 0.07);
  padding: 3em 4.5em;
  border-radius: 10px;
}
h2 {
  font-size: 1.56rem;
  font-weight: 500;
}

label {
  color: rgba(0, 112, 59, 0.9);
}

.btn {
  padding: 0.6em 2em;
  font-weight: 600;
  background: var(--clr-text);
  color: var(--clr-bg);
}
</style>
