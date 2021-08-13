import { createRouter, createWebHistory } from "vue-router";
// Public
import Home from "../views/Home.vue";
import About from "../views/About.vue";
import Docs from "../views/Docs.vue";
import PageNotFound from "../views/PageNotFound.vue";

// Dashboard
import Overview from "../views/dashboard/Overview.vue";
import Programs from "../views/dashboard/Programs.vue";
import Members from "../views/dashboard/Members.vue";
import Orders from "../views/dashboard/Orders.vue";
import Billing from "../views/dashboard/Billing.vue";
import Support from "../views/dashboard/Support.vue";
import Login from "../views/auth/Login.vue";

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
    path: "/docs",
    name: "Docs",
    component: Docs,
  },
  {
    path: "/auth/login",
    name: "Login",
    component: Login,
  },
  {
    // beforeEnter: requireAuth,
    path: "/dashboard/overview",
    name: "Overview",
    component: Overview,
    meta: { requiresAuth: true },
  },
  {
    // beforeEnter: requireAuth,
    path: "/dashboard/billing",
    name: "Billing",
    component: Billing,
    meta: { requiresAuth: true },
  },
  {
    // beforeEnter: requireAuth,
    path: "/dashboard/programs",
    name: "Programs",
    component: Programs,
    meta: { requiresAuth: true },
  },
  {
    // beforeEnter: requireAuth,
    path: "/dashboard/members",
    name: "Members",
    component: Members,
    meta: { requiresAuth: true },
  },
  {
    // beforeEnter: requireAuth,
    path: "/dashboard/orders",
    name: "Orders",
    component: Orders,
    meta: { requiresAuth: true },
  },
  {
    // beforeEnter: requireAuth,
    path: "/dashboard/support",
    name: "Support",
    component: Support,
    meta: { requiresAuth: true },
  },
  {
    path: "/:catchAll(.*)",
    name: "PageNotFound",
    component: PageNotFound,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

router.beforeEach((to, from, next) => {
  const loggedIn = localStorage.getItem("token");

  if (to.matched.some((record) => record.meta.requiresAuth) && !loggedIn) {
    next("/auth/login");
  } else {
    next();
  }
});

export default router;
