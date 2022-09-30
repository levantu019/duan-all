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
    <v-list-item class="px-2 header-nav" link>
      <v-list-item-title v-if="!mini" class="white--text text-h6"
        >Bảng điều khiển</v-list-item-title
      >
      <v-btn v-if="!mini" icon @click.stop="mini = !mini">
        <v-icon>mdi-chevron-left</v-icon>
      </v-btn>
      <v-btn v-if="mini" icon @click.stop="mini = !mini">
        <v-icon>mdi-chevron-right</v-icon>
      </v-btn>
    </v-list-item>

    <v-divider></v-divider>

    <v-list dense>
      <v-list-group
        v-for="item in items"
        color="primary"
        :key="item.title"
        no-action
        @click="routeTo(item.link)"
      >
        <template v-slot:prependIcon>
          <img width="30px" height="30px" :src="item.icon" />
        </template>
        <template v-slot:appendIcon v-if="item.items.length === 0">
          <v-icon></v-icon>
        </template>

        <template v-slot:activator>
          <v-list-item-content>
            <v-list-item-title v-text="item.title"></v-list-item-title>
          </v-list-item-content>
        </template>

        <v-list-item-group color="primary">
          <v-list-item
            class="pl-10"
            v-for="child in item.items"
            :key="child.title"
            link
            dense
            :to="{ name: child.link }"
          >
            <v-list-item-icon>
              <img width="20px" height="20px" :src="child.icon" />
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title v-text="child.title"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list-group>
      <!-- </v-list-item-group> -->
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  created() {
    const route = this.$route.matched[0].name;
    if (route === "quan-tri-dieu-hanh-nhiem-vu") {
      this.items = this.$appConfig.navList;
    }
  },
  methods: {
    routeTo(nameRoute) {
      if (!!nameRoute && this.$route.name !== nameRoute) {
        console.log(nameRoute);
        this.$router.push({ name: nameRoute });
      }
    },
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
