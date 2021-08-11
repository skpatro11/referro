<template>
  <div class="card">
    <div class="card__header">
      <h5>Zerodha Mutual Fund</h5>
      <p>₹45</p>
    </div>
    <div class="card__body">
      <p>Access Token: IJI88990</p>
      <button href="#" class="btn-sm">COPY</button>
    </div>
    <div class="rect-1"></div>
    <div class="rect-2"></div>
  </div>
</template>

<script>
export default {};
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