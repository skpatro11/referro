<template>
  <form class="d-flex flex-column" @submit.prevent="handleSubmit">
    <div class="mb-3">
      <label class="form-label" for="username">Username</label>
      <input class="form-control" type="text" required v-model="displayName" />
    </div>
    <div class="mb-3">
      <label class="form-label" for="email">Email</label>
      <input class="form-control" type="email" required v-model="email" />
    </div>
    <div class="mb-3">
      <label class="form-label" for="password">Password</label>
      <input class="form-control" type="password" required v-model="password" />
    </div>
    <div class="error">{{ error }}</div>
    <button class="mt-3">Sign up</button>
  </form>
</template>

<script>
import { ref } from "vue";
import useSignup from "../composables/useSignup";

export default {
  setup(props, context) {
    const { error, signup } = useSignup();

    const displayName = ref("");
    const email = ref("");
    const password = ref("");

    const handleSubmit = async () => {
      await signup(email.value, password.value, displayName.value);
      // console.log("User Signed up");
      if (!error.value) {
        context.emit("signup");
      }
    };

    return { displayName, email, password, handleSubmit, error };
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
