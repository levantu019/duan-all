<template>
  <div class="header">
    <v-menu offset-x>
      <template v-slot:activator="{ attrs, on: menu }">
        <v-tooltip bottom>
          <template v-slot:activator="{ on: tooltip }">
            <v-btn
              icon
              large
              color="white"
              v-bind="attrs"
              v-on="{ ...tooltip, ...menu }"
            >
              <v-icon dark> mdi-menu </v-icon>
            </v-btn>
          </template>

          <span>Công cụ</span>
        </v-tooltip>
      </template>

      <v-list>
        <v-list-item-group v-model="tool">
          <v-list-item v-for="tool in tools" :key="tool" link color="primary">
            <v-list-item-icon>
              <v-icon>mdi-tools</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title v-text="tool"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-menu>

    <h2 class="ml-3 white--text text-uppercase">{{ title }}</h2>
    <v-spacer></v-spacer>
    <div class="info-account d-flex align-center">
      <v-menu offset-y>
        <template v-slot:activator="{ on }">
          <v-btn icon v-on="on">
            <v-avatar size="36">
              <img alt="Avatar" src="@/assets/img/usename.png" />
            </v-avatar>
          </v-btn>
        </template>
        <v-list>
          <v-list-item link>
            <v-list-item-icon>
              <v-icon>mdi-logout-variant</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>Đăng xuất</v-list-item-title>
            </v-list-item-content></v-list-item
          >
        </v-list>
      </v-menu>
      <h4 class="mx-5 white--text">Phan Quốc Yên</h4>
    </div>
  </div>
</template>

<script>
export default {
  props: ["title"],
  data() {
    return {
      // title: this.$appConfig.title,
      tool: null,
      tools: ["Công cụ bản đồ", "Công cụ..."],
    };
  },
};
</script>

<style scoped>
.header {
  display: flex;
  align-items: center;
  background-color: #4472c4;
  /* width: 100%; */
  height: 50px;
}
.header h2 {
  color: white;
}
</style>
>>>>>>> 0e10d96 (page Nhiem vu dieu hanh)
