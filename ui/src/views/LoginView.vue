<template>
  <v-app>
    <div class="login">
      <div class="header d-flex align-center justify-center">
        <h2>HỆ THỐNG QUẢN TRỊ CSDL NỀN ĐỊA LÝ QUẦN ĐẢO TRƯỜNG SA</h2>
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
              src="@/assets/img/Logo_MTA_new.png"
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
              >
                <template slot="append-outer">
                  <v-icon color="red">*</v-icon>
                </template>
              </v-text-field>

              <v-combobox :items="items" label="Quyền người dùng" outlined>
                <template slot="append-outer">
                  <v-icon color="red">*</v-icon>
                </template>
              </v-combobox>

              <v-btn color="#4472C4" class="mr-4 pa-6 btn-login white--text">
                Đăng Nhập</v-btn
              >
            </v-form>
          </v-col>
        </v-row>
      </div>
    </div>
  </v-app>
</template>

<script>
export default {
  data() {
    return {
      showPassword: false,
      items: ["Quyền quản trị", "Quyền nhập liệu"],
    };
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
>>>>>>> 0e10d96 (page Nhiem vu dieu hanh)
