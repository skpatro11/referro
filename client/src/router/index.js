import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import About from "../views/About.vue";
import Auth from "../views/Auth.vue";
import Overview from "../components/Dashboard/Overview.vue";
import Programs from "../components/Dashboard/Programs.vue";
import Members from "../components/Dashboard/Members.vue";
import Orders from "../components/Dashboard/Orders.vue";
import Billing from "../components/Dashboard/Billing.vue";
import Support from "../components/Dashboard/Support.vue";

const requireAuth = (to, from, next) => {
  if (localStorage.getItem("token") !== null) {
    next();
  } else {
    next({ name: "Auth" });
  }
};

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/about",
    name: "About",
    component: About,
  },
  {
    path: "/auth",
    name: "Auth",
    component: Auth,
  },
  {
    beforeEnter: requireAuth,
    path: "/dashboard/overview",
    name: "Overview",
    component: Overview,
  },
  {
    beforeEnter: requireAuth,
    path: "/dashboard/billing",
    name: "Billing",
    component: Billing,
  },
  {
    beforeEnter: requireAuth,
    path: "/dashboard/programs",
    name: "Programs",
    component: Programs,
  },
  {
    beforeEnter: requireAuth,
    path: "/dashboard/members",
    name: "Members",
    component: Members,
  },
  {
    beforeEnter: requireAuth,
    path: "/dashboard/orders",
    name: "Orders",
    component: Orders,
  },
  {
    beforeEnter: requireAuth,
    path: "/dashboard/support",
    name: "Support",
    component: Support,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
