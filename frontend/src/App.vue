<template>
  <div id="app">
    <router-view v-if="this.$route.name === 'dang-nhap'" />
    <router-view v-if="this.$route.name !== 'dang-nhap'" />
  </div>
</template>
<script>
// import { EventBus } from "./EventBus";

export default {
  mounted() {
    this.$router.push({ name: "nhiem-vu-cap-dieu-hanh" });

    //EventBus.$emit("app-mounted");
  },
};
</script>

<style scoped></style>
