<template>
  <div class="header">
    <v-menu offset-x>
      <template v-slot:activator="{ attrs, on: menu }">
        <v-tooltip bottom>
          <template v-slot:activator="{ on: tooltip }">
            <v-btn
              icon
              large
              color="white"
              v-bind="attrs"
              v-on="{ ...tooltip, ...menu }"
            >
              <v-icon dark> mdi-menu </v-icon>
            </v-btn>
          </template>

          <span>Công cụ</span>
        </v-tooltip>
      </template>

      <v-list>
        <v-list-item-group v-model="tool">
          <v-list-item v-for="tool in tools" :key="tool" link color="primary">
            <v-list-item-icon>
              <v-icon>mdi-tools</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title v-text="tool"></v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-menu>

    <h2 class="ml-3 white--text text-uppercase">{{ title }}</h2>
    <v-spacer></v-spacer>
    <div class="info-account d-flex align-center">
      <!-- <v-menu offset-y>
        <template v-slot:activator="{ on }">
          <v-badge color="pink" :content="messages" :value="messages" overlap>
            <v-btn v-on="on" elevation="0" fab small color="#ECF3FF" depressed>
              <v-icon dark color="black"> mdi-bell </v-icon>
            </v-btn>
          </v-badge>
        </template>
        <v-list>
          <v-list-item v-for="(note, index) in notes" :key="index" link>
            <v-list-item-icon>
              <v-icon>mdi-note</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>{{ note }}</v-list-item-title>
            </v-list-item-content></v-list-item
          >
        </v-list>
      </v-menu> -->
      <v-menu offset-y>
        <template v-slot:activator="{ on }">
          <v-btn icon v-on="on">
            <v-avatar size="36">
              <img alt="Avatar" src="@/assets/images/usename.png" />
            </v-avatar>
          </v-btn>
        </template>
        <v-list>
          <v-list-item link>
            <v-list-item-icon>
              <v-icon>mdi-logout-variant</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title>Đăng xuất</v-list-item-title>
            </v-list-item-content></v-list-item
          >
        </v-list>
      </v-menu>
      <h4 class="mx-5 white--text">Phạm Hữu Hoàng</h4>
    </div>
  </div>
</template>

<script>
export default {
  props: ["title"],
  sockets: {
    note: function (note) {
      console.log(note);
      this.notes.unshift(note);
      this.messages++;
    },
  },
  data() {
    return {
      // title: this.$appConfig.title,
      tool: null,
      tools: ["Công cụ bản đồ", "Công cụ..."],
      messages: 0,
      notes: [],
    };
  },
};
</script>

<style scoped>
.header {
  display: flex;
  align-items: center;
  background-color: #4472c4;
  /* width: 100%; */
  height: 50px;
}
.header h2 {
  color: white;
}
</style>
