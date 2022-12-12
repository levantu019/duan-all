const { defineConfig } = require("@vue/cli-service");
const path = require("path");
module.exports = defineConfig({
  transpileDependencies: ["vuetify"],

  devServer: {
    port: 3003,

    proxy: {
      // "/": {
      //   target: process.env.VUE_APP_BASE_API,
      //   changeOrigin: true,
      // },
      "/geoserver": {
        target: process.env.VUE_APP_GEOSERVER_BASEURL,
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
