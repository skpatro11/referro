import { createRouter, createWebHistory } from "vue-router";
import Home from "../views/Home.vue";
import About from "../views/About.vue";
import Contact from "../views/Contact.vue";
import Auth from "../views/Auth.vue";
import Overview from "../components/Dashboard/Overview.vue";
import Programs from "../components/Dashboard/Programs.vue";
import Members from "../components/Dashboard/Members.vue";
import Orders from "../components/Dashboard/Orders.vue";
import Billing from "../components/Dashboard/Billing.vue";
import Support from "../components/Dashboard/Support.vue";

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
    path: "/contact",
    name: "Contact",
    component: Contact,
  },
  {
    path: "/auth",
    name: "Auth",
    component: Auth,
  },
  {
    path: "/dashboard/overview",
    name: "Overview",
    component: Overview,
  },
  {
    path: "/dashboard/billing",
    name: "Billing",
    component: Billing,
  },
  {
    path: "/dashboard/programs",
    name: "Programs",
    component: Programs,
  },
  {
    path: "/dashboard/members",
    name: "Members",
    component: Members,
  },
  {
    path: "/dashboard/orders",
    name: "Orders",
    component: Orders,
  },
  {
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
