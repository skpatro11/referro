<template>
  <div>
    <div
      class="modal fade"
      :id="program.id"
      tabindex="-1"
      aria-labelledby="exampleModalLabel"
      aria-hidden="true"
    >
      <div class="modal-dialog modal-dialog-centered modal-lg">
        <div class="modal-content">
          <div class="modal-body text-start">
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
          <div class="d-flex align-items-baseline justify-content-between mt-1">
            <div class="d-flex align-items-baseline">
              <span class="access_token">{{ program.access_token }}</span>
              <button href="#" class="btn-sm ms-4">COPY</button>
            </div>
            <button
              id="editProgram"
              class="btn-underline-sm ms-2"
              data-bs-toggle="modal"
              :data-bs-target="['#' + program.id]"
            >
              <svg
                width="21"
                height="21"
                viewBox="0 0 19 19"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
              >
                <g clip-path="url(#clip0)">
                  <path
                    d="M8.75 3.5H3.5C3.10218 3.5 2.72064 3.65804 2.43934 3.93934C2.15804 4.22064 2 4.60218 2 5V15.5C2 15.8978 2.15804 16.2794 2.43934 16.5607C2.72064 16.842 3.10218 17 3.5 17H14C14.3978 17 14.7794 16.842 15.0607 16.5607C15.342 16.2794 15.5 15.8978 15.5 15.5V10.25"
                    stroke="#00703B"
                    stroke-opacity="0.7"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  />
                  <path
                    d="M14.375 2.37499C14.6734 2.07663 15.078 1.909 15.5 1.909C15.922 1.909 16.3266 2.07663 16.625 2.37499C16.9234 2.67336 17.091 3.07804 17.091 3.49999C17.091 3.92195 16.9234 4.32663 16.625 4.62499L9.5 11.75L6.5 12.5L7.25 9.49999L14.375 2.37499Z"
                    stroke="#00703B"
                    stroke-opacity="0.7"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  />
                </g>
                <defs>
                  <clipPath id="clip0">
                    <rect
                      width="18"
                      height="18"
                      fill="white"
                      transform="translate(0.5 0.5)"
                    />
                  </clipPath>
                </defs>
              </svg>
            </button>
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
        `${process.env.VUE_APP_ROOT_API}/programs/access_token/${this.program.id}/`
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
