<template>
  <div class="welcome container">
    <p>Welcome</p>
    <div v-if="showLogin">
      <h2>Login</h2>
      <Login @login="enterDashboard" />
      <p>
        No accounts yet? <span @click="showLogin = false">Signup</span> instead
      </p>
    </div>
    <div v-else>
      <h2>Sign up</h2>
      <Signup @signup="enterDashboard" />
      <p>
        Already registered? <span @click="showLogin = true">Login</span> instead
      </p>
    </div>
  </div>
</template>

<script>
import Signup from "../components/Signup.vue";
import Login from "../components/Login.vue";
import { ref } from "vue";
import { useRouter } from "vue-router";

export default {
  components: { Signup, Login },
  setup() {
    const showLogin = ref(true);
    const router = useRouter();

    const enterDashboard = () => {
      router.push({ name: "Overview" });
    };

    return { showLogin, enterDashboard };
  },
};
</script>

<style>
.welcome {
  text-align: center;
  padding: 50px 0;
  color: #00587a;
  border-radius: 10px;
  margin: 10px auto;
}
.container {
  width: 90%;
  max-width: 960px;
  margin: 40px auto;
  border-radius: 20px;
  box-shadow: 2px 4px 6px rgba(28, 6, 49, 0.1);
  background: white;
}
.welcome form {
  /* color: white; */
  width: 300px;
  margin: 20px auto;
}
.welcome label {
  display: block;
  margin: 20px 0 10px;
}
.welcome input {
  width: 100%;
  padding: 10px;
  border-radius: 20px;
  outline: none;
  color: #999;
  border: 1px solid #eee;
  margin: 10px auto;
}
.welcome button {
  margin: 20px auto;
  outline: none;
}
.welcome span {
  cursor: pointer;
  text-decoration: underline;
  font-weight: bold;
}
.container {
  width: 90%;
  max-width: 960px;
  margin: 80px auto;
  border-radius: 20px;
  box-shadow: 2px 4px 6px rgba(28, 6, 49, 0.1);
  background: white;
}
.error {
  color: #ff3f80;
  font-size: 14px;
}
.container button {
  cursor: pointer;
  text-decoration: none;
  background: #5ae4ca;
  color: white;
  font-weight: bold;
  border: 0;
  border-radius: 20px;
  padding: 10px 20px;
}
</style>