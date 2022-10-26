<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-data-table
          :headers="headers"
          :items="listNhiemVuBoPhan"
          :search="search"
          class="elevation-1"
          height="calc(100vh - 260px)"
          :footer-props="{
            'items-per-page-text': 'Hiển thị 1 trang',
            'items-per-page-options': [10, 15, 20],
          }"
          fixed-header
          :loading="isLoading"
          loading-text="Loading...Please wait"
        >
          <v-divider></v-divider>
          <template v-slot:top>
            <v-toolbar flat color="white">
              <div class="d-flex">
                <v-text-field
                  v-model="search"
                  append-icon="mdi-magnify"
                  label="Tìm kiếm"
                  dense
                  outlined
                  single-line
                  hide-details
                ></v-text-field>
                <v-btn
                  color="primary"
                  class="ml-2 white--text"
                  :disabled="isAdding"
                >
                  <v-icon dark>mdi-plus</v-icon>Thêm mới
                </v-btn>
              </div>
            </v-toolbar>
          </template>

          <template v-slot:[`item.pheDuyet`]="{ item }">
            <v-chip
              v-if="item.pheDuyet"
              class="ma-2"
              color="green"
              text-color="white"
            >
              Đã Phê Duyệt
            </v-chip>
            <v-chip v-else class="ma-2" color="red" text-color="white">
              Chưa phê duyệt
            </v-chip>
          </template>

          <template v-slot:[`item.tenNVDH`]="{ item }">
            <span>{{ item.maNVDH | convertNVDH(listNhiemVu) }}</span>
          </template>

          <template v-slot:[`item.tenDV`]="{ item }">
            <span>{{ item.maDV | convertDV(listDonVi) }}</span>
          </template>

          <template v-slot:[`item.moTaNVBP`]="{ item }">
            <span>{{ item.moTaNVBP }}</span>
          </template>
          <template v-slot:[`item.tenNVBP`]="{ item }">
            <span>{{ item.tenNVBP }}</span>
          </template>
          <template v-slot:[`item.actions`]="{ item }">
            <v-icon color="green" class="mr-2" @click="pheDuyet(item)">
              mdi-checkbox-marked-circle
            </v-icon>
            <v-icon color="red" @click="showThongBao(item)">
              mdi-note-text-outline
            </v-icon>
          </template>
          <template v-slot:[`item.ngayBDNVBP`]="{ item }">
            <span>{{ item.ngayBDNVBP }}</span>
          </template>
          <template v-slot:[`item.ngayKTNVBP`]="{ item }">
            <span>{{ item.ngayKTNVBP }}</span>
          </template>
          <template v-slot:[`item.trangThaiNVBP`]="{ item }">
            <span>{{ item.trangThaiNVBP | convertStatus(listTrangThai) }}</span>
          </template>

          <template v-slot:[`body.append`]>
            <span></span>
          </template>
        </v-data-table>
      </v-col>
    </v-row>
    <v-dialog v-model="dialog" max-width="500">
      <v-card>
        <v-card-title class="text-h5"> Ghi chú phương án </v-card-title>

        <v-card-text>
          <v-textarea
            name="input-7-1"
            label="Ghi chú"
            value=""
            outlined
            hide-details
            v-model="note"
          ></v-textarea>
        </v-card-text>

        <v-card-actions>
          <v-spacer></v-spacer>

          <v-btn color="green darken-1" text @click="dialog = false">
            Hủy
          </v-btn>

          <v-btn color="green darken-1" text @click="saveThongBao()">
            OK
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-container>
</template>

<script>
import nhiemVuDieuHanh from "@/api/nhiem-vu-dieu-hanh";
import donVi from "@/api/don-vi";
import nhiemVuBoPhan from "@/api/nhiem-vu-bo-phan";

import { mapMutations } from "vuex";

export default {
  data() {
    return {
      menu2: false,
      menu3: false,
      search: "",
      isLoading: false,
      isAdding: false,
      isEditing: false,
      headers: this.$appConfig.pheDuyetNhiemVuBoPhan.headers,
      listNhiemVuBoPhan: [],
      listNhiemVu: [],
      listDonVi: [],
      listTrangThai: [],
      editedIndex: -1,
      editedItem: {
        ...this.$appConfig.giaoNhiemVu.defaultItem,
      },
      dialog: false,
      note: "",
      defaultItem: {
        ...this.$appConfig.giaoNhiemVu.defaultItem,
      },
      nameRules: [(v) => !!v || "Name is required"],
    };
  },
  async created() {
    try {
      this.isLoading = true;

      //Call API get data from BE
      const [nhiemVuDH, donvi, trangThaiNV, nhiemVuBP] = await Promise.all([
        nhiemVuDieuHanh.getAll({}),
        donVi.getAll({}),
        nhiemVuBoPhan.getTrangThaiBPNV({}),
        nhiemVuBoPhan.getAll({}),
      ]);

      // transform data

      this.listNhiemVu = nhiemVuDH;

      this.listDonVi = donvi;

      this.listTrangThai = trangThaiNV;

      this.listNhiemVuBoPhan = nhiemVuBP.filter((item) => !item.pheDuyet);

      this.isLoading = false;
    } catch (error) {
      console.log(error);
    }
  },

  methods: {
    ...mapMutations("map", {
      toggleSnackbar: "TOGGLE_SNACKBAR",
    }),
    async pheDuyet(item) {
      try {
        this.editedIndex = this.listNhiemVuBoPhan.indexOf(item);

        this.editedItem = Object.assign({}, item);

        const requestData = {
          pheDuyet: true,
          id: this.editedItem.maNhanDang,
          trangThaiNVBP: 3,
        };

        let result = await nhiemVuBoPhan.update(requestData);

        if (!!result && this.editedIndex > -1) {
          this.listNhiemVuBoPhan.splice(this.editedIndex, 1);

          // //update Data
          // this.initData()

          //Thong bao
          this.toggleSnackbar({
            type: "success",
            message: "Phê Duyệt thành công điều hành thành công",
            state: true,
            timeout: 2000,
          });
        }
      } catch (error) {
        console.log(error);
      }
    },
    showThongBao(item) {
      this.editedIndex = this.listNhiemVuBoPhan.indexOf(item);
      this.editedItem = Object.assign({}, item);

      this.note = item.thongBao || "";
      this.dialog = true;
    },

    async saveThongBao() {
      try {
        const requestData = {
          thongBao: this.note,
          id: this.editedItem.maNhanDang,
        };
        let result = await nhiemVuBoPhan.update(requestData);

        if (!!result && this.editedIndex > -1) {
          Object.assign(this.listNhiemVuBoPhan[this.editedIndex], result);

          //Thong bao
          this.toggleSnackbar({
            type: "success",
            message: "Thêm điểm nhiệm vụ điều hành thành công",
            state: true,
            timeout: 2000,
          });

          this.dialog = false;
        }
      } catch (error) {
        console.log(error);
      }
    },
    closeThongBao() {
      this.editedItem = Object.assign({}, this.defaultItem);
      this.editedIndex = -1;

      this.dialog = false;
    },
  },
  filters: {
    convertNVDH: (nvdh, listNV) => {
      if (!nvdh) return "";
      return listNV.filter((nv) => nv.maNhanDang === nvdh)[0].tenNVDH;
    },
    convertDV: (maDV, listDV) => {
      if (!maDV) return "";

      return listDV.filter((dv) => dv.maNhanDang === maDV)[0].tenDonVi;
    },
    convertStatus: (maStatus, listStatus) => {
      if (!maStatus) return "";

      return listStatus.filter((stt) => stt.value === maStatus)[0].text;
    },
  },
};
</script>

<style>
.theme--light.v-data-table.v-data-table--fixed-header thead th {
  background: rgb(160, 159, 159) !important;
}
</style>
