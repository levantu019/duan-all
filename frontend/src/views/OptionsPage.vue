<template>
  <div class="view-options">
    <div
      v-if="this.selectionLayer.length === 0"
      class="header d-flex align-center justify-center"
    >
      <h2>HỆ THỐNG QUẢN TRỊ CSDL NỀN ĐỊA LÝ QUỐC GIA</h2>
    </div>
    <div
      class="d-flex justify-content align-center"
      :class="this.selectionLayer.length === 0 ? 'content' : ''"
    >
      <v-col>
        <h2 class="mb-2">Lớp dữ liệu chuyên đề</h2>
        <v-row v-if="this.selectionLayer.length === 0">
          <v-col
            v-for="option in listOptions"
            :key="option.id"
            class="left-side d-flex align-center justify-center"
            lg="3"
            xs="3"
            cols="12"
          >
            <v-card class="mx-auto" max-width="344">
              <v-img :src="option.image" height="95px"></v-img>

              <v-card-title> {{ option.name }} </v-card-title>

              <v-card-subtitle> {{ option.sub }} </v-card-subtitle>

              <v-card-actions>
                <v-btn
                  @click="selectLayer(option.id)"
                  color="orange lighten-2"
                  text
                  >Khám phá
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
        <v-row v-if="this.selectionLayer.length === 0">
          <v-col>
            <h2>Trang thiếu bị khí tài</h2>
            <v-card class="ml-12" max-width="344">
              <v-img
                src="https://photo-cms-sggp.zadn.vn/w570/Uploaded/2022/dufkxmeyxq/2022_03_16/https3a2f2fd1e00ek4ebabmscloudfrontnet2fproduction2fa68047e22ffc4a3b81c7f985c3d01a44_jzab.jpg"
                height="95px"
              ></v-img>

              <v-card-title> Trang bị khí tài </v-card-title>

              <v-card-subtitle> Trang bị khí tài </v-card-subtitle>

              <v-card-actions>
                <v-btn color="orange lighten-2" text @click="redirectToKhiTai"
                  >Khám phá
                </v-btn>
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
      </v-col>

      <map-component
        :maLop="selectionLayer"
        v-if="this.selectionLayer.length !== 0"
      />
    </div>
    <div v-if="this.selectionLayer.length !== 0" class="button-back">
      <v-row>
        <v-col cols="12">
          <v-text-field
            v-model="search"
            clear-icon="mdi-close-circle"
            clearable
            label="Tìm kiếm trên bản đồ"
            type="text"
            background-color="white"
            solo
            prepend-inner-icon="mdi-menu"
            @click:prepend-inner="drawer = true"
          >
            <template slot="append">
              <v-icon class="icon-search" @click="handlerSearch"
                >mdi-magnify</v-icon
              >
            </template>
          </v-text-field>
        </v-col>
      </v-row>
    </div>
    <!-- <div class="layers" v-if="this.selectionLayer.length !== 0">
      <v-navigation-drawer v-model="drawer" :mini-variant.sync="mini" permanent>
        <v-list-item class="px-2">
          <v-list-item-avatar>
            <v-img src="/img/layers.png"></v-img>
          </v-list-item-avatar>

          <v-list-item-title>Lớp địa hình</v-list-item-title>

          <v-btn icon @click.stop="mini = !mini">
            <v-icon>mdi-chevron-left</v-icon>
          </v-btn>
        </v-list-item>

        <v-divider></v-divider>

        <v-list dense>
          <v-list-item v-for="item in items" :key="item.title" link>
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <div
                style="
                  display: flex;
                  align-items: center;
                  justify-content: space-between;
                "
              >
                <p>{{ item.title }}</p>
                <v-checkbox style="margin-top: 0px"></v-checkbox>
              </div>
            </v-list-item-content>
          </v-list-item>
        </v-list>
      </v-navigation-drawer>
    </div> -->
    <div class="information" v-if="this.selectionLayer.length !== 0">
      <v-navigation-drawer
        v-model="drawer"
        width="100%"
        temporary
        absolute
        hide-overlay
      >
        <v-list-item class="px-2"> </v-list-item>

        <!-- <v-divider></v-divider> -->

        <!-- <v-list>
          <v-list-item v-for="item in items" :key="item.title" link>
            <v-list-item-icon>
              <v-icon>{{ item.icon }}</v-icon>
            </v-list-item-icon>

            <v-list-item-content>
              <v-list-item-title>{{ item.title }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list> -->

        <v-card :loading="loading" class="mx-auto my-12" max-width="374">
          <template slot="progress">
            <v-progress-linear
              color="deep-purple"
              indeterminate
            ></v-progress-linear>
          </template>

          <v-img
            height="250"
            src="https://cdn.vuetifyjs.com/images/cards/cooking.png"
          ></v-img>

          <v-card-title>Con Cưng</v-card-title>

          <v-card-text>
            <v-row align="center" class="mx-0">
              Đánh giá:
              <v-rating
                :value="4.5"
                color="amber"
                dense
                half-increments
                readonly
                size="14"
              ></v-rating>

              <div class="grey--text ms-4">57 bài đánh giá</div>
            </v-row>

            <!-- <div class="my-4 text-subtitle-1">$ • Italian, Cafe</div> -->

            <div class="my-4 text-subtitle-1">Cửa hàng quần áo trẻ em</div>
          </v-card-text>

          <v-divider class="mx-4"></v-divider>

          <v-card-actions class="justify-space-around">
            <div class="action-wrapper">
              <v-btn color="primary" class="ma-2 white--text" fab>
                <v-icon dark> mdi-directions </v-icon>
              </v-btn>
              <p class="subtitle-1">Đường đi</p>
            </div>
            <div class="action-wrapper">
              <v-btn color="primary" class="ma-2 white--text" fab outlined>
                <v-icon dark> mdi-bookmark-outline </v-icon>
              </v-btn>
              <p class="subtitle-1">Lưu</p>
            </div>
            <div class="action-wrapper">
              <v-btn color="primary" class="ma-2 white--text" fab outlined>
                <v-icon dark>mdi-map-marker-circle </v-icon>
              </v-btn>
              <p class="subtitle-1">Gần đó</p>
            </div>
            <div class="action-wrapper">
              <v-btn color="primary" class="ma-2 white--text" fab outlined>
                <v-icon dark> mdi-share-variant-outline</v-icon>
              </v-btn>
              <p class="subtitle-1">Chia sẻ</p>
            </div>
          </v-card-actions>
          <v-divider class="mx-4"></v-divider>

          <v-card-title>Thời gian mở cửa</v-card-title>

          <v-card-text>
            <v-chip-group
              v-model="selection"
              active-class="deep-purple accent-4 white--text"
              column
            >
              <v-chip>5:30PM</v-chip>

              <v-chip>7:30PM</v-chip>

              <v-chip>8:00PM</v-chip>

              <v-chip>9:00PM</v-chip>
            </v-chip-group>
          </v-card-text>
        </v-card>
      </v-navigation-drawer>
    </div>
    <!-- <div class="layers">Test</div> -->
  </div>
</template>

<script>
import MapComponent from "@/components/ol/MapComponent.vue";
export default {
  components: { MapComponent },
  created() {},
  data() {
    return {
      listOptions: [
        {
          id: "NDL18092205",
          name: "Lớp giao thông",
          sub: "Lớp chuyên đề",
          action: "",
          image: "/img/GiaoThong.jfif",
        },
        {
          id: "NDL18092201",
          name: "Lớp biên giới địa giới",
          sub: "Lớp chuyên đề",
          action: "",
          image: "/img/BienGioiDiaGioi.PNG",
        },
        {
          id: "NDL18092202",
          name: "Lớp cơ sở đo đạc",
          sub: "Lớp chuyên đề",
          action: "",
          image: "/img/CoSoDoDac.PNG",
        },
        {
          id: "NDL18092203",
          name: "Lớp dân cư",
          sub: "Lớp chuyên đề",
          action: "",
          image: "/img/DanCu.PNG",
        },
        {
          id: "NDL18092204",
          name: "Lớp địa hình",
          sub: "Lớp chuyên đề",
          action: "",
          image: "/img/DiaHinh.jpg",
        },
        {
          id: "NDL18092206",
          name: "Lớp phủ bề mặt",
          sub: "Lớp chuyên đề",
          action: "",
          image: "/img/PhuBeMat.png",
        },
        {
          id: "NDL18092207",
          name: "Lớp thủy văn",
          sub: "Lớp chuyên đề",
          action: "",
          image: "/img/ThuyVan.png",
        },
        {
          id: "NDL18092208",
          name: "Lớp soạn thảo văn kiện",
          sub: "Lớp chuyên đề",
          action: "",
          image: "/img/SoanThaoKeHoach.png",
        },
      ],
      selectionLayer: "",
      drawer: false,
      items: [
        { title: "Đường bình độ", icon: "mdi-layers" },
        { title: "Đường bình độ sâu", icon: "mdi-layers" },
        { title: "Điểm độ cao", icon: "mdi-layers" },
        { title: "Điểm độ sâu", icon: "mdi-layers" },
        { title: "Địa hình đặc biệt trên đất liền", icon: "mdi-layers" },
      ],
      search: "",
    };
  },
  methods: {
    selectLayer(maLop) {
      if (maLop !== "NDL18092208") {
        this.selectionLayer = maLop;
      } else {
        this.$router.push({ name: "quan-tri-dieu-hanh-nhiem-vu" });
      }
    },
    backToViewOptions() {
      this.selectionLayer = "";
    },
    handlerSearch() {},
    redirectToKhiTai() {
      this.$router.push({ name: "trang-bi-khi-tai" });
    },
  },
};
</script>

<style scoped>
.content {
  height: calc(100vh - 80px);
}
.view-options {
  height: 100vh;
  position: relative;
}
.header {
  height: 80px;
  background-color: #4472c4;
}

.header h2 {
  color: white;
}
.hidden-sm-and-down .v-icon {
  color: red !important;
}
.v-input__icon.v-input__icon--append-outer > .v-icon {
  color: red !important;
}
.btn-login {
  width: calc(100% - 19.34px);
}
.button-back {
  position: absolute;
  top: 20px;
  left: 20px;
  display: flex;
  z-index: 9999;
  width: 350px;
}
.information {
  position: absolute;
  top: 0px;
  left: 0px;
  bottom: 0px;
  width: 400px;
}
.icon-search:hover {
  color: blue;
}
.layers {
  position: absolute;
}
.action-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
}
</style>
