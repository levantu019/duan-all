<template>
  <v-snackbar
    :color="snackbar.type"
    top
    right
    absolute
    centered
    tile
    :timeout="snackbar.timeout"
    v-model="snackbar.state"
    icon="mdi-info"
  >
    <!-- <v-alert dense type="info">
      I'm a dense alert with a <strong>type</strong> of info
    </v-alert> -->
    <v-icon class="mr-3">mdi-information</v-icon>
    <strong>{{ snackbar.message }}</strong>
    <template v-slot:action="{ attrs }">
      <v-btn icon v-bind="attrs" @click="hideSnackbar({ state: false })">
        <v-icon>mdi-close</v-icon>
      </v-btn>
    </template>
  </v-snackbar>
</template>

<script>
//Store imports
import { mapGetters, mapMutations } from "vuex";

export default {
  computed: {
    ...mapGetters("map", {
      snackbar: "snackbar",
    }),
  },
  methods: {
    ...mapMutations("map", {
      hideSnackbar: "TOGGLE_SNACKBAR",
    }),
  },
};
</script>
