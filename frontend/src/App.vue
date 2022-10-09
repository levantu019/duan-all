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
    // window.location.href = "/dang-nhap";
    this.$router.push({ name: "quan-tri-dieu-hanh-nhiem-vu" });
    //EventBus.$emit("app-mounted");
  },
  methods: {},
  components: { Snackbar },
};
</script>

<style>
.ol-zoom {
  left: unset !important;
  right: 8px;
}
</style>
