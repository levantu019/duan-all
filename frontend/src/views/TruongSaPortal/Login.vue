<template>
  <div class="login">
    <v-main>
      <v-container class="d-flex flex-column">
        <div
          class="title text-uppercase white--text text-center text-h4 font-weight-bold"
        >
          Hệ thống thông tin địa lý (GIS) <br />quần đảo trường sa
        </div>
        <div class="mx-auto my-16">
          <img class="logo" src="@/assets/images/logoBQP.svg" />
        </div>
        <div class="wrapper-controls">
          <v-form ref="form" class="form">
            <v-text-field
              prepend-inner-icon="mdi-account"
              outlined
              filled
              label="Tên đăng nhập"
              required
              v-model="username"
              color="white"
              dark
            >
              <template slot="append-outer">
                <v-icon color="red">*</v-icon>
              </template>
            </v-text-field>
            <v-text-field
              prepend-inner-icon="mdi-lock"
              :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
              :type="showPassword ? 'text' : 'password'"
              filled
              outlined
              name="input-10-2"
              label="Mật khẩu"
              class="input-group--focused"
              @click:append="showPassword = !showPassword"
              v-model="password"
              color="white"
              dark
            >
              <template slot="append-outer">
                <v-icon color="red">*</v-icon>
              </template>
            </v-text-field>

            <v-btn
              color="#4472C4"
              class="mr-4 pa-6 btn-login white--text btn-login"
            >
              Đăng Nhập</v-btn
            >
          </v-form>
        </div>
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
      showPassword: false,
      username: "",
      password: "",
    };
  },
};
</script>
<style scoped>
.login {
  width: 100vw;
  height: 100vh;
  background-image: url("@/assets/images/backgroundBQP.jpg");
  height: 100%;
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
.logo {
  width: 250px;
  height: 250px;
}
.wrapper-controls {
  padding: 20px;
  background-image: url("@/assets/images/wrapper-controls.png");
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;

  width: 100%;
  height: 300px;
  display: flex;
  justify-content: center;
  align-items: center;
}

.form {
  width: 100%;
}

.btn-login {
  width: 100%;
}
</style>
