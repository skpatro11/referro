<template>
  <form @submit.prevent="handleSubmit">
    <div class="input-field">
      <label for="email">Email</label>
      <input type="email" required placeholder="email" v-model="email" />
    </div>
    <div class="input-field">
      <label for="password">Password</label>
      <input
        type="password"
        required
        placeholder="password"
        v-model="password"
      />
    </div>
    <div class="error">{{ error }}</div>
    <button>Log in</button>
  </form>
</template>

<script>
import { ref } from "vue";
import useLogin from "../composables/useLogin";

export default {
  setup(props, context) {
    const email = ref("");
    const password = ref("");

    const { error, login } = useLogin();

    const handleSubmit = async () => {
      // console.log(email.value, password.value)
      await login(email.value, password.value);
      if (!error.value) {
        // console.log("User Logged In")
        context.emit("login");
      }
    };
    return { email, password, handleSubmit, error };
  },
};
</script>

<style>
.input-field {
  display: flex;
  flex-direction: column;
  margin: 1rem 0;
}
</style>
