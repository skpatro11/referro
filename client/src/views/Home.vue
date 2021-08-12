<template>
  <div class="home">
    <div class="home-header">
      <h1 class="moto">Referral Incentive Made Easy</h1>
      <p class="description">
        Lorem ipsum dolor sit amet consectetur adipisicing elit. Similique enim
        fugiat beatae sed omnis dolorem error numquam facilis dignissimos
        officiis totam, liberes?
      </p>
      <button id="getting-started">Get Started</button>
    </div>
  </div>
</template>

<script>
// @ is an alias to /src

export default {
  name: "Home",
  components: {},
};
</script>

<style>
.home-header {
  /* border: 2px solid black; */
  display: flex;
  flex-direction: column;
  align-content: center;
  justify-content: center;
  width: 50%;
  text-align: left;
  margin-left: 5%;
}
.moto {
  color: #00587a;
  font-size: 60px;
  font-weight: bold;
  margin: 20px 0px;
}
.description {
  font-size: 18px;
  color: #00587a;
  letter-spacing: 1px;
}
#getting-started {
  cursor: pointer;
  font-size: 15px;

  display: flex;
  flex-direction: row;
  justify-content: center;
  align-items: center;
  padding: 8px 81px;

  position: static;
  width: 250px;
  height: 50px;
  left: 0px;
  top: 408px;

  background: #00587a;
  color: white;
  border: none;
  box-shadow: 0px 7px 16px rgba(0, 88, 122, 0.1),
    0px 4px 9px rgba(0, 88, 122, 0.2);
  border-radius: 5px;

  /* Inside Auto Layout */

  flex: none;
  order: 1;
  flex-grow: 0;
  margin: 31px 0px;
}
</style>