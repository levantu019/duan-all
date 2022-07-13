import Vue from "vue";
import VueRouter from "vue-router";

Vue.use(VueRouter);

const routes = [
  {
    path: "/dang-nhap",
    name: "dang-nhap",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/LoginView.vue"),
  },
  {
    path: "/quan-tri-he-thong",
    name: "quan-tri-he-thong",
    // children: [
    //   {
    //     path: "test",
    //     name: "test",
    //     component: () => import("../components/HelloWorld.vue"),
    //   },
    // ],
    component: () => import("../views/DashboardView.vue"),
  },
  {
    path: "/quan-tri-dieu-hanh-nhiem-vu",
    name: "quan-tri-dieu-hanh-nhiem-vu",
    children: [
      {
        path: "nhiem-vu-cap-dieu-hanh",
        name: "nhiem-vu-cap-dieu-hanh",
        component: () =>
          import("@/views/quan-tri-nhiem-vu-dieu-hanh/QuanTriDieuHanh.vue"),
      },
      {
        path: "diem-nhiem-vu-dieu-hanh",
        name: "diem-nhiem-vu-dieu-hanh",
        component: () =>
          import("@/views/quan-tri-nhiem-vu-dieu-hanh/DiemNhiemVuDieuHanh.vue"),
      },
    ],
    component: () => import("../views/DashboardView.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
