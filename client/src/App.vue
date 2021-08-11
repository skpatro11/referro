<template>
  <div id="nav">
    <div class="brand">Referro</div>
    <div class="actions">
      <router-link to="/">Home</router-link>
      <router-link to="/auth">Auth</router-link>
      <router-link to="/dashboard/overview">Dashboard</router-link>
      <router-link to="/contact">Contact</router-link>
      <router-link to="/about">About</router-link>
    </div>
  </div>
  <router-view />
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}
#nav {
  /* border: 2px solid black; */
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 90%;
  margin: 20px auto;
}
.brand {
  color: #0f3057;
  font-size: 25px;
  font-weight: bold;
  cursor: pointer;
}
a {
  color: black;
  text-decoration: none;
  font-size: 18px;
  margin: 5px 10px;
}
.router-link-active {
  color: #0f3057;
  font-weight: bold;
}
</style>
