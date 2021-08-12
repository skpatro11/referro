<template>
  <div class="auth-container rounded text-start mx-auto">
    <div v-if="showLogin">
      <h2 class="mb-4">Sign in to your account</h2>
      <Login @login="enterDashboard" />
      <p class="mt-4">
        Don't have a account?
        <span @click="showLogin = false"> <u>Create Here</u></span>
      </p>
    </div>
    <div v-else>
      <h2 class="mb-4">Create a new account</h2>
      <Signup @signup="enterDashboard" />
      <p class="mt-4">
        Already registered?
        <span @click="showLogin = true"><u>Login Here</u></span>
      </p>
    </div>
  </div>
</template>

<script>
import Signup from "../components/Signup.vue";
import Login from "../components/Login.vue";
import { ref } from "vue";
import { useRouter } from "vue-router";
import store from "../store";

export default {
  components: { Signup, Login },
  setup() {
    const showLogin = ref(true);
    const router = useRouter();

    console.log(store.state.isAuthenticated);

    const enterDashboard = () => {
      store.state.isAuthenticated = true;
      console.log(store.state.isAuthenticated);
      router.push({ name: "Programs" });
    };

    return { showLogin, enterDashboard };
  },
};
</script>

<style>
.auth-container {
  background: #dbffee;
  border: 1px solid #a8ffd6;
  box-shadow: 0px 3px 10px rgba(0, 0, 0, 0.07);
  padding: 3em 4.5em;
  max-width: 600px;
}

.auth-container h2 {
  font-size: 1.56rem;
  font-weight: 500;
}
.auth-container label {
  color: rgba(0, 112, 59, 0.9);
}
.auth-container input {
  background: #b5ffdc;
  padding: 0.6em 1em;
  color: var(--clr-text);
  border: none;
}

.auth-container button {
  background: var(--clr-dark);
  color: var(--clr-primary);
  padding: 0.6em 0em;
}

.error {
  color: #ff3f80;
  font-size: 14px;
}

.auth-container .form-control:focus {
  background: #b5ffdc;
}
</style>
