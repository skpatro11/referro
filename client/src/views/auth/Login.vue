<template>
  <div class="auth-container rounded text-start mx-auto mt-5">
    <h2 class="mb-4">Sign in to your account</h2>
    <form class="d-flex flex-column" @submit.prevent="handleLogin">
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
  </div>
</template>

<script>
export default {
    data () {
    return {
      email: '',
      password: '',
      error: null
    }
  },
  methods: {
    handleLogin () {
      this.$store
        .dispatch('login', {
          email: this.email,
          password: this.password
        })
        .then(() => {
          this.$store.dispatch('setUser')
          this.$router.push({ name: 'Overview' })
        })
        .catch(err => {
          this.error = err.response.data.error
        })
    }
  }
}
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