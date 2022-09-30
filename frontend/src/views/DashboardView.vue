<template>
  <div v-if="this.$route.name !== 'dang-nhap'">
    <header-component title="Quản trị - điều hành thực hành nhiệm vụ" />
    <nav-component />
    <v-main>
      <v-container fluid>
        <router-view />
      </v-container>
    </v-main>

    <v-footer app color="#4472c4">
      <h4 class="white--text">Cập nhật dữ liệu gần nhất: 5/2022</h4>
      <v-spacer></v-spacer>
      <h4 class="white--text">Phiên bản: V1.0</h4>
    </v-footer>
  </div>
</template>

<script>
import HeaderComponent from "@/components/layouts/HeaderComponent.vue";
import NavComponent from "@/components/layouts/NavComponent.vue";
export default {
  components: {
    HeaderComponent,
    NavComponent,
  },
};
</script>

<style></style>
