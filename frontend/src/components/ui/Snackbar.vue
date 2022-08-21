<template>
  <v-snackbar
    :color="snackbar.type"
    top
    :timeout="snackbar.timeout"
    v-model="snackbar.state"
    icon="mdi-info"
  >
    <v-icon class="mr-3">mdi-information</v-icon>
    {{ snackbar.message }}
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
