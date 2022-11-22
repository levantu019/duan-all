<template>
  <div class="home">
    <v-main>
      <v-container>
        <v-content>
          <v-row>
            <v-col cols="6" md="6" sm="12">
              <h1
                class="title text-uppercase white--text text-center text-h3 font-weight-bold"
              >
                HỆ THỐNG THÔNG TIN ĐỊA LÝ (GIS) <br />QUẦN ĐẢO TRƯỜNG SA
              </h1>
              <ul class="description mt-5">
                <li class="white--text">
                  Cách tiếp cập trực tuyến thực hiện công tác quản lý, tra cứu
                  CSDL nền địa lý thống nhất, đồng bộ và bảo mật.
                </li>
                <li class="white--text">
                  Dữ liệu dùng chung được cập nhật tập trung, đồng thời được
                  chia sẻ cho các đơn vị theo từng lĩnh vực đặc thù.
                </li>
                <li class="white--text">
                  Hệ thống có khả năng truy cập mọi lúc, mọi nơi và trên mọi
                  thiết bị.
                </li>
              </ul>
            </v-col>
            <v-col class="d-flex" cols="6" md="6" sm="12">
              <img class="logo mx-auto" src="@/assets/images/logoBQP.svg" />
            </v-col>
          </v-row>
        </v-content>
        <v-content>
          <v-row class="d-flex align-content-center">
            <v-col
              class="mt-5"
              v-for="(menu, i) in menuCard"
              :key="i"
              cols="3"
              md="3"
              sm="6"
            >
              <v-card
                class="mx-auto d-flex flex-column card"
                max-width="344"
                height="100%"
                elevation="12"
              >
                <v-img
                  :src="menu.img"
                  height="80"
                  width="100"
                  class="mx-auto img-card"
                ></v-img>

                <v-card-title
                  class="text-uppercase mx-auto white--text text-h6 font-weight-bold"
                  >{{ menu.title }}</v-card-title
                >

                <v-card-subtitle class="white--text mt-1">
                  {{ menu.sub }}
                </v-card-subtitle>

                <v-card-actions class="mx-auto">
                  <v-btn
                    color="primary"
                    elevation="6"
                    class="rounded"
                    @click="routeToView(menu)"
                  >
                    Xem thêm
                  </v-btn>
                  <v-spacer></v-spacer>
                </v-card-actions>
              </v-card>
            </v-col>
          </v-row>
        </v-content>
      </v-container>
    </v-main>
    <Footer />
  </div>
</template>

<script>
import Footer from "@/components/layouts/TruongSaPortal/Footer.vue";

export default {
  components: {
    Footer,
  },
  data() {
    return {
      menuCard: [
        {
          title: "Quản trị",
          sub: "Quản trị thông tin người dùng, hệ thống và cơ sở dữ liệu nền địa lý.",
          img: require("@/assets/images/quantri.png"),
          route: "",
        },
        {
          title: "CỔNG THÔNG TIN ĐỊA LÝ (GIS)",
          sub: "Cung cấp giải pháp tìm kiếm, khai thác và chia sẻ dữ liệu đến người dùng.",
          img: require("@/assets/images/congthongtin.png"),
          route: {
            name: "options-view",
            params: {},
          },
        },
        {
          title: "HỆ HỖ TRỢ RA QUYẾT ĐỊNH",
          sub: "Cho phép hỗ trợ soạn thảo kế hoạch, phân tích hỗ trợ ra quyết định không gian.",
          img: require("@/assets/images/hotroraquyetdinh.png"),
          route: "",
        },
        {
          title: "BIÊN TẬP BẢN ĐỒ WEBGIS",
          sub: "Công cụ cho phép trinh bày các lớp dữ liệu trên nền tảng WebGIS.",
          img: require("@/assets/images/bientapbando.png"),
          route: "",
        },
      ],
    };
  },
  methods: {
    routeToView(menu) {
      if (!!menu.route) {
        this.$router.push(menu.route);
      }
    },
  },
};
</script>

<style scoped>
.home {
  width: 100vw;
  height: 100vh;
  background-image: url("@/assets/images/backgroundBQP.jpg");
  height: 100%;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}

.img-card {
  margin-top: -50px;
}
.logo {
  width: 250px;
  height: 250px;
}

.wrap-row {
  height: 100%;
}

.card {
  background-image: url("@/assets/images/backgroundcard.png");
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
</style>
