const { defineConfig } = require("@vue/cli-service");
const path = require("path");
module.exports = defineConfig({
  transpileDependencies: ["vuetify"],

  devServer: {
    port: 3003,
    proxy: {
      "/api": {
        target: process.env.VUE_APP_BASE_API,
        changeOrigin: true,
      },
    },
  },
  configureWebpack: {
    resolve: {
      alias: {
        "@": path.resolve("src"),
      },
    },
  },
});
