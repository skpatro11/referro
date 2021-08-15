<template>
  <div>
    <div class="hero text-center">
      <div class="my-5">
        <h1>Complete Referral System <br />for your Business</h1>
        <a @click="handleGetstarted" class="btn hero-btn mt-5" href="#"
          >Get Started</a
        >
      </div>
      <img src="../assets/hero-image.png" class="img-fluid" />
    </div>
    <div class="our-process">
      <h2 class="my-5">Our Process</h2>
      <Process
        image="program-illus.png"
        step="1"
        title="Create a Referral Scheme"
        desc="A company can create a program to make a referral scheme for an organisation. There can be multiple programs i.e. different types of referral scheme for a single organisation"
      />
      <ProcessAlter
        image="access-token-illus.png"
        step="2"
        title="Generate Access Token"
        desc="After a referral program has been created, the user can generate a access token to obtain the access to the api and connect with our server.
An individual or organization can manage the referral program with the help of access token."
      />
      <Process
        image="member-illus.png"
        step="3"
        title="Referers are added"
        desc="A member i.e. referrer can be created automatically during the signup process or manually through a link afterwards using our service. The member will get a unique id through which other user can be referrerd."
      />
      <ProcessAlter
        image="orders-illus.png"
        step="4"
        title="Rewards is claimed"
        desc="When a user is sucessfully referred an order will be generated automatically through which the member/referrer can claim their rewards."
      />
    </div>
  </div>
</template>

<script>
// @ is an alias to /src
import Process from "../components/home/Process.vue";
import ProcessAlter from "../components/home/ProcessAlter.vue";

export default {
  name: "Home",
  components: { Process, ProcessAlter },
  methods: {
    handleGetstarted() {
      this.$router.push({ name: "Programs" });
    },
  },
};
</script>

<style>
.hero {
  margin-top: 5em;
}
.hero h1 {
  font-size: 3.75rem;
  color: var(--clr-text);
  font-weight: 700;
}

.hero .hero-btn {
  padding: 1em 3em;
  font-size: 1.1rem;
  font-weight: 600;
  background: var(--clr-text);
  color: var(--clr-bg);
  transition: 400ms;
}

.hero .hero-btn:hover {
  background: rgb(0, 78, 43);
  box-shadow: 0px 4px 9px rgba(0, 112, 59, 0.2);
}

.our-process {
  margin: 5em 0;
}

.our-process h2 {
  font-size: 3rem;
  font-weight: 700;
}

.our-process h4 {
  font-size: 2rem;
  color: var(--clr-text);
}

.our-process p {
  color: var(--clr-text);
  line-height: 32px;
}

.our-process .step-circle {
  width: 2em;
  height: 2em;
  border-radius: 50%;
  background: var(--clr-text);
  color: var(--clr-bg);
  font-size: 2rem;
  font-weight: 600;
}

.process-content {
  width: 50%;
}
</style>
