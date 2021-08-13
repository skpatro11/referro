<template>
  <div class="text-start mt-3">
    <div>
      ID: <span>{{ program.id }}</span>
    </div>
    <div class="card mt-2">
      <div
        class="card__header d-flex align-items-baseline justify-content-between"
      >
        <h5>{{ program.name }}</h5>
        <p>₹{{ program.incentive }}</p>
      </div>
      <div class="card__body mt-1" v-show="program.access_token">
        <div class="d-flex align-items-baseline">
          Access Token
          <button
            id="regenerateToken"
            class="btn-outline-sm ms-2"
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
  bottom: -100%;
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
  top: -60%;
  right: -15%;
  background: hsla(152, 100%, 92%, 1);
  z-index: -1;
}
</style>
