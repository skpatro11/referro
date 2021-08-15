<template>
  <div class="page-not-found">
    <div class="back-img"></div>
    <div class="container">
      <h4 class="orange-text">Page Not Found</h4>
      <p>You Reached a dead end, may be this links may help you navigate</p>
      <img class="page-not-found-img" src="../assets/PageNotFound.png" alt="" />
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style>
.page-not-found {
  /* background-image: linear-gradient(0deg, #f58740, #f06352); */
  width: 100%;
  height: 100vh;
  overflow: hidden;
  display: -ms-flexbox;
  display: flex;
  flex-direction: column;
  -ms-flex-align: center;
  align-items: center;
}
.back-img {
  position: absolute;
  height: 100vh;
  width: 100%;
  z-index: 2;
  /* background-image: url(../assets/login-back.png); */
  background-size: cover;
}
.page-not-found-img {
  /* border: 2px solid red; */
  height: auto;
  width: 200px;
}
.links {
  width: 50%;
  /* border: 2px solid black; */
  margin: 30px auto;
  display: flex;
  justify-content: space-evenly;
}
</style>