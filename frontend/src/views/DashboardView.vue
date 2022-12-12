<template>
  <div v-if="this.$route.name !== 'dang-nhap'">
    <header-component :title="title" />
    <nav-component />
    <v-main>
      <v-container fluid class="pa-0">
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
  created() {
    const route = this.$route.matched[0].name;
    if (route === "quan-tri-dieu-hanh-nhiem-vu") {
      this.title = "Quản trị - điều hành thực hành nhiệm vụ";
    } else if (route === "quan-tri-co-so-du-lieu") {
      this.title = "Quản trị cơ sở dữ liệu nền địa lý QĐTS";
    }
  },
  mounted() {},

  data() {
    return {
      title: "Ko",
    };
  },
};
</script>

<style></style>
