<template>
  <v-app id="app">
    <snackbar />
    <router-view v-if="this.$route.name === 'dang-nhap'" />
    <router-view v-if="this.$route.name !== 'dang-nhap'" />
  </v-app>
</template>
<script>
import Snackbar from "./components/ui/Snackbar.vue";

export default {
  components: {
    snackbar: Snackbar,
  },
  mounted() {
    this.$router.push({ name: "nhiem-vu-cap-dieu-hanh" });
    //EventBus.$emit("app-mounted");
  },
  methods: {},
  components: { Snackbar },
};
</script>

<style scoped></style>
