<template>
  <v-app-bar app class="header">
    <!-- -->
    <div class="l-header">
      <img class="logo" src="@/assets/images/logoBQP.svg" />
      <v-toolbar-title class="ml-2 white--text font-weight-bold"
        >GIS PORTAL
        <p class="mb-0">Cổng thông tin GIS quần đảo Trường Sa</p>
      </v-toolbar-title>
    </div>
    <v-spacer></v-spacer>
    <div class="mr-4">
      <v-btn color="white" v-for="link in links" :key="link" text>
        {{ link }}
      </v-btn>
    </div>
    <v-avatar>
      <img src="@/assets/images/usename.png" alt="John" />
    </v-avatar>
  </v-app-bar>
</template>

<script>
import { MENU } from "@/constants";
export default {
  data() {
    return {
      links: MENU.options,
    };
  },
};
</script>

<style scoped>
.logo {
  width: 50px;
  height: 50px;
}
.header {
  background-image: url("@/assets/images/headerQDTS.png");
  background-position: center;
  background-repeat: no-repeat;
  background-size: cover;
}
.l-header {
  display: flex;
  align-items: center;
  justify-content: center;
}
.r-header {
  display: flex;
}
</style>
