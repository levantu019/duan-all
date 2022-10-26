<template>
  <v-navigation-drawer
    app
    v-model="drawer"
    :mini-variant.sync="mini"
    permanent
    width="340"
    height=""
    class="nav"
    style="top: 50px"
  >
    <v-list-item class="px-2 header-nav">
      <v-list-item-content v-if="!mini" class="white--text text-h6">
        <v-text-field
          clear-icon="mdi-close-circle"
          clearable
          label="Tên đơn vị tìm kiêm"
          type="text"
          background-color="white"
          solo
          hide-details
        >
          <template slot="append">
            <v-icon class="icon-search">mdi-magnify</v-icon>
          </template>
        </v-text-field>
      </v-list-item-content>

      <v-btn v-if="!mini" icon @click.stop="mini = !mini">
        <v-icon>mdi-chevron-left</v-icon>
      </v-btn>
      <v-btn v-if="mini" icon @click.stop="mini = !mini">
        <v-icon>mdi-chevron-right</v-icon>
      </v-btn>
    </v-list-item>

    <v-divider></v-divider>

    <v-list>
      <v-list-item-group
        color="primary"
        v-model="selectDV"
        @change="handlerSelectDV"
      >
        <v-list-item v-for="item in items" :key="item.text" link>
          <v-list-item-icon>
            <v-icon>mdi-home-variant-outline</v-icon>
          </v-list-item-icon>
          <v-list-item-content>
            <v-list-item-title v-text="item.text"></v-list-item-title>
          </v-list-item-content>
        </v-list-item>
      </v-list-item-group>
      <!-- </v-list-item-group> -->
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  created() {
    this.items = [
      { text: "Học viện quân y" },
      { text: "Đơn vị hóa học 1" },
      { text: "Đơn vị tổng cục kỹ thuật" },
      { text: "Nhà máy Z111/TCCNQP" },
      { text: "Cục Bản đồ/BTTM" },
      { text: "Kho 2/Đơn vị hóa học 2" },
      { text: "Kho 3/Đơn vị hóa học 1" },
      { text: "Kho 42/ Đơn vị hóa học 1" },
    ];
  },
  methods: {
    routeTo(nameRoute) {
      if (!!nameRoute && this.$route.name !== nameRoute) {
        this.$router.push({ name: nameRoute });
      }
    },
    handlerSelectDV() {
      this.$emit("selectDV", this.selectDV);
    },

    selectDV: "",
  },
  data() {
    return {
      drawer: null,
      items: null,
      mini: false,
    };
  },
};
</script>

<style scoped>
.header-nav {
  background-color: #729fcf;
}
.list-item-group {
  flex: 1 1 auto;
}
.nav {
  height: calc(100vh - 86px);
}
</style>
