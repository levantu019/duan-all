<template>
  <div class="group-view">
    <Header />
    <v-main>
      <v-container>
        <v-row>
          <v-col cols="7">
            <v-sheet elevation="8" height="300" width="100%" rounded="lg">
              <v-toolbar dense color="primary"
                ><v-toolbar-title class="white--text title text-uppercase"
                  >Bản đồ {{ groupInfo.tenNhom }}</v-toolbar-title
                >
              </v-toolbar>
              <div class="info-layer">
                <ul class="content">
                  <li><b>Tên bản đồ:</b> {{ groupInfo.tenNhom }}</li>
                  <li><b>Hệ quy chiếu:</b> VN2000</li>
                  <li><b>Ngày lập:</b> 11/11/2022</li>
                  <li><b>Đơn vị cung cấp:</b> Học viện KTQS</li>
                  <li><b>Mô tả bản đồ:</b> {{ groupInfo.moTaNhom }}</li>
                </ul>
              </div>
            </v-sheet>
          </v-col>
          <v-col cols="5"
            ><v-sheet
              elevation="8"
              height="100%"
              rounded="lg"
              outlined
              width="100%"
            >
              <v-toolbar dense color="primary"
                ><v-toolbar-title class="white--text title text-uppercase"
                  >Bản đồ</v-toolbar-title
                >
              </v-toolbar>
              <div class="overview-map">
                <v-card class="mx-auto">
                  <v-img
                    class="white--text align-end"
                    src="@/assets/images/overviewMap.png"
                    height="250px"
                  >
                    <v-card-actions>
                      <div
                        class="btn-view-layer title text-uppercase"
                        @click="viewMap"
                      >
                        Xem bản đồ
                      </div>
                    </v-card-actions></v-img
                  >

                  <!-- <v-card-title> Top western road trips </v-card-title> -->
                </v-card>
                <!-- <v-img
                  max-height="240"
                  src="@/assets/images/overviewMap.png"
                  alt=""
                /> -->
              </div>
            </v-sheet>
          </v-col>
        </v-row>
        <v-row>
          <v-toolbar dense color="primary"
            ><v-toolbar-title class="white--text title text-uppercase"
              >Các lớp bản đồ liên quan</v-toolbar-title
            >
          </v-toolbar>
        </v-row>
        <v-row>
          <v-col
            v-for="layer in layers.filter((layer) => layer.hienThiLopChuyenDe)"
            :key="layer.maNhanDang"
            cols="6"
          >
            <v-sheet elevation="8" rounded="lg" height="250" width="100%">
              <v-row>
                <v-col cols="5">
                  <v-img
                    max-height="230"
                    src="http://localhost:8080/geoserver/dieutrabien/wms?service=WMS&version=1.1.0&request=GetMap&layers=dieutrabien%3Adiemdocao&bbox=107.375991821289%2C13.0079402923584%2C108.863075256348%2C14.5999126434326&width=717&height=768&srs=EPSG%3A4756&styles=&format=image%2Fpng"
                  >
                    <template v-slot:placeholder>
                      <v-row
                        class="fill-height ma-0"
                        align="center"
                        justify="center"
                      >
                        <v-progress-circular
                          indeterminate
                          color="grey lighten-5"
                        ></v-progress-circular>
                      </v-row>
                    </template>
                  </v-img>
                </v-col>
                <v-col cols="7">
                  <ul class="layer-relate">
                    <li class="title text-uppercase font-weight-bold"></li>
                    <li class="text-h6 primary--text">
                      {{ layer.tenHienThiLop || layer.tenLop }}
                    </li>
                    <li>Đang cập nhật dữ liệu</li>
                    <li>Số lượng đối tượng: 0</li>
                  </ul>
                </v-col>
              </v-row>
            </v-sheet>
          </v-col>
          <!-- <v-col cols="6"
            ><v-sheet elevation="8" height="250" outlined width="100%">
            </v-sheet
          ></v-col> -->
        </v-row>
      </v-container>
    </v-main>
    <Footer />
  </div>
</template>
<script>
import Header from "@/components/layouts/TruongSaPortal/Header.vue";
import Footer from "@/components/layouts/TruongSaPortal/Footer.vue";

import lopDuLieu from "@/api/lop-du-lieu";
import nhomDuLieu from "@/api/nhom-du-lieu";

export default {
  components: {
    Header,
    Footer,
  },
  data() {
    return {
      groupInfo: {
        tenNhom: "",
        moTaNhom: "",
      },
      groupID: "",
      layers: [],
    };
  },

  async created() {
    this.groupID = this.$route.params.id;

    //call nhom du lieu

    this.groupInfo = await nhomDuLieu.getById(this.groupID);

    //call api get layer with groupName
    const res = await lopDuLieu.getAll({});

    this.layers = res.filter((layer) => {
      return layer.maNhom === this.groupID;
    });
  },
  methods: {
    viewMap() {
      this.$router.push({
        name: "dashboard",
        params: { groupId: this.groupID },
      });
    },
  },
};
</script>
<style scoped>
.info-layer {
  padding: 20px;
  height: 100%;
  width: 100%;
}

.layer-relate {
  list-style: none;
}
.btn-view-layer {
  background-color: rgba(35, 104, 224, 0.658);
  height: 50px;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
  border-radius: 8px;
}
.loading-img {
  background-color: black;
}

.parent-class >>> .v-toolbar__content {
  padding: 0px !important;
}
</style>
