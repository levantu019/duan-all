<template>
  <div class="options-view">
    <Header />
    <v-main>
      <v-container>
        <v-row no-gutters style="flex-wrap: wrap">
          <v-col
            v-for="(option, i) in options"
            :key="i"
            cols="12"
            sm="6"
            md="4"
            lg="3"
            class="group-layer"
            @click="routeGroupView(option)"
          >
            <v-card class="mx-auto ma-2" max-width="300">
              <v-img
                :src="option.image"
                height="280px"
                class="white--text align-end"
                gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
              >
                <v-card-actions>
                  <div class="sub-options title text-uppercase">
                    {{ option.title }}
                  </div>
                </v-card-actions>
              </v-img>
            </v-card>
          </v-col>
        </v-row>
      </v-container>
    </v-main>
    <Footer />
  </div>
</template>
<script>
import Header from "@/components/layouts/TruongSaPortal/Header";
import Footer from "@/components/layouts/TruongSaPortal/Footer";
import { OPTION_LAYER } from "@/constants";

export default {
  components: {
    Header,
    Footer,
  },
  data: () => ({
    options: OPTION_LAYER.options1,
  }),
  methods: {
    routeGroupView(option) {
      // console.log(option);
      this.$router.push(option.route);
    },
  },
};
</script>

<style scoped>
.wrapper-options {
  display: flex;
  flex-wrap: wrap;
}
.btn-choose {
  background-color: rgba(47, 107, 211, 0.5);
}

.sub-options {
  background-color: rgba(47, 107, 211, 0.5);
  height: 50px;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}
.group-layer {
  cursor: pointer;
}
</style>
