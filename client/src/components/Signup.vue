<template>
  <form @submit.prevent="handleSubmit">
    <div class="input-field">
      <label for="username">Username</label>
      <input
        type="text"
        required
        placeholder="display name"
        v-model="displayName"
      />
    </div>
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
    <button>Sign up</button>
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
