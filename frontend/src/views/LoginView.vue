<template>
  <div class="login">
    <div class="header d-flex align-center justify-center">
      <h2>HỆ THỐNG QUẢN TRỊ CSDL NỀN ĐỊA LÝ QUỐC GIA</h2>
    </div>
    <div class="content d-flex justify-content align-center">
      <v-row>
        <v-col
          class="left-side d-flex align-center justify-center"
          lg="6"
          xs="12"
          cols="12"
        >
          <v-img
            max-height="300"
            max-width="300"
            src="@/assets/images/Logo_MTA_new.png"
            alt=""
          />
        </v-col>
        <v-col lg="6" xs="12" cols="12" class="pa-10">
          <h2 class="text-center mb-5">ĐĂNG NHẬP</h2>
          <v-form ref="form">
            <v-text-field
              prepend-inner-icon="mdi-account"
              outlined
              label="Tên đăng nhập"
              required
              v-model="username"
            >
              <template slot="append-outer">
                <v-icon color="red">*</v-icon>
              </template>
            </v-text-field>
            <v-text-field
              prepend-inner-icon="mdi-lock"
              :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
              :type="showPassword ? 'text' : 'password'"
              outlined
              name="input-10-2"
              label="Mật khẩu"
              class="input-group--focused"
              @click:append="showPassword = !showPassword"
              v-model="password"
            >
              <template slot="append-outer">
                <v-icon color="red">*</v-icon>
              </template>
            </v-text-field>

            <!-- <v-combobox :items="items" label="Quyền người dùng" outlined>
              <template slot="append-outer">
                <v-icon color="red">*</v-icon>
              </template>
            </v-combobox> -->

            <v-btn
              color="#4472C4"
              class="mr-4 pa-6 btn-login white--text"
              @click="login"
            >
              Đăng Nhập</v-btn
            >
          </v-form>
        </v-col>
      </v-row>
    </div>
  </div>
</template>

<script>
import Vue from "vue";

export default {
  data() {
    return {
      showPassword: false,
      items: ["Quyền quản trị", "Quyền nhập liệu"],
      username: "",
      password: "",
    };
  },
  sockets: {},
  methods: {
    login() {
      // this.$socket.emit("userLogin", this.username);
      if (this.username === "usercap1") {
        Vue.prototype.$user = {
          name: "Người điều hành",
          maDV: "DVI19092201",
          quyen: "Cap1",
        };

        this.$router.push({ name: "quan-tri-dieu-hanh-nhiem-vu" });
      } else if (this.username === "usercap21") {
        Vue.prototype.$user = {
          name: "Lực lượng Bộ Binh",
          maDV: "DVI24102202",
          quyen: "Cap2",
        };
        this.$router.push({ name: "quan-tri-dieu-hanh-nhiem-vu" });
      } else {
        Vue.prototype.$user = {
          name: "Lực lượng Cứu hộ",
          maDV: "DVI19092201",
          quyen: "Cap2",
        };
        this.$router.push({ name: "quan-tri-dieu-hanh-nhiem-vu" });
      }

      return;
    },
  },
};
</script>

<style scoped>
.content {
  height: calc(100vh - 80px);
}
.login {
  height: 100vh;
}
.header {
  height: 80px;
  background-color: #4472c4;
}

.header h2 {
  color: white;
}
.hidden-sm-and-down .v-icon {
  color: red !important;
}
.v-input__icon.v-input__icon--append-outer > .v-icon {
  color: red !important;
}
.btn-login {
  width: calc(100% - 19.34px);
}
</style>
