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
    path: "/chon-che-do-hien-thi",
    name: "chon-che-do-hien-thi",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/OptionsPage.vue"),
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
      {
        path: "tuyen-nhiem-vu-dieu-hanh",
        name: "tuyen-nhiem-vu-dieu-hanh",
        component: () =>
          import(
            "@/views/quan-tri-nhiem-vu-dieu-hanh/TuyenNhiemVuDieuHanh.vue"
          ),
      },
      {
        path: "vung-nhiem-vu-dieu-hanh",
        name: "vung-nhiem-vu-dieu-hanh",
        component: () =>
          import("@/views/quan-tri-nhiem-vu-dieu-hanh/VungNhiemVuDieuHanh.vue"),
      },
      {
        path: "giao-nhiem-vu",
        name: "giao-nhiem-vu",
        component: () => import("@/views/GiaoNhiemVu.vue"),
      },

      //Phe duyet phuong an
      {
        path: "phe-duyet-phuong-an-vi-tri",
        name: "phe-duyet-phuong-an-vi-tri",
        component: () =>
          import("@/views/giam-sat-dieu-hanh/PheDuyetPhuongAnViTri.vue"),
      },
      {
        path: "phe-duyet-phuong-an-tuyen",
        name: "phe-duyet-phuong-an-tuyen",
        component: () =>
          import("@/views/giam-sat-dieu-hanh/PheDuyetPhuongAnTuyen.vue"),
      },
      {
        path: "phe-duyet-phuong-an-vung",
        name: "phe-duyet-phuong-an-vung",
        component: () =>
          import("@/views/giam-sat-dieu-hanh/PheDuyetPhuongAnVung.vue"),
      },
      {
        path: "phe-duyet-phuong-an-luc-luong",
        name: "phe-duyet-phuong-an-luc-luong",
        component: () =>
          import("@/views/giam-sat-dieu-hanh/PheDuyetPhuongAnLucLuong.vue"),
      },
      {
        path: "nhiem-vu-bo-phan",
        name: "nhiem-vu-bo-phan",
        component: () => import("@/views/soan-thao-ke-hoach/NhiemVuBoPhan.vue"),
      },
      {
        path: "quan-tri-phuong-an-vi-tri",
        name: "quan-tri-phuong-an-vi-tri",
        component: () =>
          import("@/views/soan-thao-ke-hoach/QuanTriPAViTri.vue"),
      },
      {
        path: "quan-tri-phuong-an-tuyen",
        name: "quan-tri-phuong-an-tuyen",
        component: () =>
          import("@/views/soan-thao-ke-hoach/QuanTriPATuyen.vue"),
      },
      {
        path: "quan-tri-phuong-an-vung",
        name: "quan-tri-phuong-an-vung",
        component: () => import("@/views/soan-thao-ke-hoach/QuanTriPAVung.vue"),
      },
      {
        path: "quan-tri-phuong-an-gan-luc-luong",
        name: "quan-tri-phuong-an-gan-luc-luong",
        component: () =>
          import("@/views/soan-thao-ke-hoach/QuanTriPAGanLL.vue"),
      },
    ],
    component: () => import("@/views/DashboardView.vue"),
  },
  {
    path: "trang-bi-khi-tai",
    name: "trang-bi-khi-tai",
    component: () => import("@/views/trang-thiet-bi-khi-tai/TrangBiKhiTai.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
