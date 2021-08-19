<template>
  <div>
    <div
      class="modal fade"
      :id="program.id"
      tabindex="-1"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-lg">
        <div class="modal-content">
          <div class="modal-body">
            <div class="d-flex justify-content-between">
              <h2 class="mb-4">Edit a referral program {{ program.name }}</h2>
              <button
                type="button"
                class="btn-close"
                data-bs-dismiss="modal"
                aria-label="Close"
              ></button>
            </div>
            <form @submit="updateProgram">
              <div class="mb-3">
                <label for="program-name" class="form-label"
                  >Program Name</label
                >
                <input
                  type="text"
                  v-model="program.name"
                  class="form-control input-field"
                  id="program-name"
                  required="true"
                />
              </div>
              <div class="mb-3">
                <label for="incentive" class="form-label">Incentive</label>
                <input
                  v-model="program.incentive"
                  type="number"
                  class="form-control input-field"
                  id="password"
                  required="true"
                />
              </div>
              <button type="submit" class="btn mt-2">Update</button>
            </form>
          </div>
        </div>
      </div>
    </div>
    <div class="text-start mt-3">
      <div>
        ID: <span>{{ program.id }}</span>
      </div>
      <div class="card mt-2">
        <div
          class="
            card__header
            d-flex
            align-items-baseline
            justify-content-between
          "
        >
          <h5>{{ program.name }}</h5>
          <p>₹{{ program.incentive }}</p>
          <button
            id="editProgram"
            class="btn-underline-sm ms-2"
            data-bs-toggle="modal"
            :data-bs-target="['#' + program.id]"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              width="16"
              height="16"
              fill="currentColor"
              class="bi bi-pencil-square"
              viewBox="0 0 16 16"
            >
              <path
                d="M15.502 1.94a.5.5 0 0 1 0 .706L14.459 3.69l-2-2L13.502.646a.5.5 0 0 1 .707 0l1.293 1.293zm-1.75 2.456-2-2L4.939 9.21a.5.5 0 0 0-.121.196l-.805 2.414a.25.25 0 0 0 .316.316l2.414-.805a.5.5 0 0 0 .196-.12l6.813-6.814z"
              />
              <path
                fill-rule="evenodd"
                d="M1 13.5A1.5 1.5 0 0 0 2.5 15h11a1.5 1.5 0 0 0 1.5-1.5v-6a.5.5 0 0 0-1 0v6a.5.5 0 0 1-.5.5h-11a.5.5 0 0 1-.5-.5v-11a.5.5 0 0 1 .5-.5H9a.5.5 0 0 0 0-1H2.5A1.5 1.5 0 0 0 1 2.5v11z"
              />
            </svg>
          </button>
        </div>
        <div class="card__body mt-1" v-show="program.access_token">
          <div class="d-flex align-items-baseline">
            Access Token
            <button
              id="regenerateToken"
              class="btn-underline-sm ms-2"
              @click="generateToken"
            >
              Re-generate
            </button>
          </div>
          <div class="d-flex align-items-baseline mt-1">
            <span class="access_token">{{ program.access_token }}</span>
            <button href="#" class="btn-sm ms-4">COPY</button>
          </div>
        </div>
        <div v-show="!program.access_token">
          <button
            id="generateToken"
            class="btn-outline-sm"
            @click="generateToken"
          >
            Generate Access Token
          </button>
        </div>
        <div class="rect-1"></div>
        <div class="rect-2"></div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  props: ["program"],
  methods: {
    async generateToken() {
      const res = await axios.get(
        `${process.env.VUE_APP_ROOT_API}/v1/programs/${this.program.id}/access_token/`
      );
      this.program.access_token = res.data.access_token;
    },
    async updateProgram() {
      const res = await axios.put(
        `${process.env.VUE_APP_ROOT_API}/programs/${this.program.id}/`,
        {
          name: this.program.name,
          incentive: parseFloat(this.program.incentive),
        }
      );
      console.log(res.data);
    },
  },
};
</script>

<style>
.card {
  padding: 1.8em;
  background: linear-gradient(90deg, #dbffee 0%, rgba(219, 255, 238, 0) 100%);
  border: 1px solid #a8ffd6;
  width: 600px;
  position: relative;
  overflow: hidden;
}

.card__header h5 {
  font-size: 1.3rem;
  font-weight: 600;
  color: var(--clr-text);
}

.card__header p {
  font-size: 1.12rem;
  font-weight: 600;
  color: var(--clr-text);
}

.card__body {
  font-size: 1rem;
  color: var(--clr-text);
}

.access_token {
  font-size: 0.8rem;
}

.btn-sm {
  font-size: 0.7rem;
  padding: 0.3em 1.2em;
  border-radius: 15px;
  background: hsla(152, 100%, 85%, 1);
  text-transform: uppercase;
}

.btn-underline-sm {
  color: var(--clr-text);
  font-size: 0.8rem;
  padding: 0.3em 1.2em;
  border-radius: 15px;
  background: transparent;
  text-transform: uppercase;
  text-decoration: underline;
}

.btn-outline-sm {
  color: var(--clr-text);
  font-size: 0.8rem;
  padding: 0.3em 1.2em;
  border-radius: 15px;
  background: transparent;
  border: 1px solid var(--clr-text);
  text-transform: uppercase;
}

.rect-1 {
  position: absolute;
  height: 200px;
  width: 95px;
  border-radius: 100px;
  transform: rotate(-60deg);
  bottom: -90%;
  right: -10%;
  background: hsla(152, 100%, 92%, 1);
  z-index: -1;
}
.rect-2 {
  position: absolute;
  height: 200px;
  width: 95px;
  border-radius: 100px;
  transform: rotate(-60deg);
  top: -55%;
  right: -15%;
  background: hsla(152, 100%, 92%, 1);
  z-index: -1;
}
</style>
