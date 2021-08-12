<template>
  <form class="d-flex flex-column" @submit.prevent="handleSubmit">
    <div class="mb-3 text-start">
      <label class="form-label" for="email">Email</label>
      <input class="form-control" type="email" required v-model="email" />
    </div>
    <div class="mb-3 text-start">
      <label class="form-label" for="password">Password</label>
      <input class="form-control" type="password" required v-model="password" />
    </div>
    <div class="error">{{ error }}</div>
    <button class="btn mt-3">Log in</button>
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
      await login(email.value, password.value);
      if (!error.value) {
        context.emit("login");
      }
    };
    return { email, password, handleSubmit, error };
  },
};
</script>

<style></style>
