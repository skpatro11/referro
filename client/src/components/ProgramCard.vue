<template>
  <div class="card">
    <div class="card__header">
      <h5>{{ program.name }}</h5>
      <p>₹{{ program.incentive }}</p>
    </div>
    <div class="card__body" v-show="program.access_token">
      <p class="access_token">
        Access Token: <span>{{ program.access_token }}</span>
      </p>
      <button id="regenerateToken" @click="generateToken">Regenerate</button>
      <button href="#" class="btn-sm">COPY</button>
    </div>
    <div v-show="!program.access_token">
      <button id="generateToken" @click="generateToken">
        Generate Access Token
      </button>
    </div>
    <div class="rect-1"></div>
    <div class="rect-2"></div>
  </div>
</template>

<script>
import { authInstance } from "../services/";

export default {
  props: ["program"],
  methods: {
    async generateToken() {
      const res = await authInstance.get(
        `programs/access_token/${this.program.id}/`
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
  border-radius: 5px;
  max-width: 500px;
  width: 100%;
  position: relative;
  overflow: hidden;
  margin: 10px 0px;
}

.card__header {
  display: flex;
  justify-content: space-between;
  align-content: center;
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
  margin-top: 1em;
  display: flex;
  font-size: 1rem;
  color: var(--clr-text);
}

.card__body button {
  margin-left: 0.7em;
}

.btn-sm {
  font-size: 0.7rem;
  padding: 0.3em 1.2em;
  border-radius: 15px;
  background: hsla(152, 100%, 85%, 1);
  text-transform: uppercase;
  cursor: pointer;
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
#generateToken {
  cursor: pointer;

  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 8px 10px;

  position: static;
  width: 180px;
  height: 40px;
  left: 0px;

  background: #057baa;
  color: white;
  border: none;
  box-shadow: 0px 7px 16px rgba(0, 88, 122, 0.1),
    0px 4px 9px rgba(0, 88, 122, 0.2);
  border-radius: 5px;

  /* Inside Auto Layout */

  flex: none;
  order: 1;
  flex-grow: 0;
  margin: 15px 0px;
}
.access_token {
  text-align: left;
}
.access_token span {
  color: #00587a;
}
</style>