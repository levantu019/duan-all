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
                  @click="addNew"
                >
                  <v-icon dark>mdi-plus</v-icon>Thêm mới
                </v-btn>
              </div>
            </v-toolbar>
          </template>

          <template v-slot:[`item.tenNVDH`]="{ item }">
            <v-select
              :items="listNhiemVu"
              v-model="editedItem.maNVDH"
              label="Tên nhiệm vụ"
              v-if="item.maNhanDang === editedItem.maNhanDang"
              dense
              item-text="tenNVDH"
              item-value="maNhanDang"
              :hide-details="true"
            ></v-select>
            <span v-else>{{ item.maNVDH | convertNVDH(listNhiemVu) }}</span>
          </template>

          <template v-slot:[`item.tenDV`]="{ item }">
            <v-select
              :items="listDonVi"
              v-model="editedItem.maDV"
              label="Đơn vị"
              v-if="item.maNhanDang === editedItem.maNhanDang"
              dense
              :hide-details="true"
              item-text="tenDonVi"
              item-value="maNhanDang"
            ></v-select>
            <span v-else>{{ item.maDV | convertDV(listDonVi) }}</span>
          </template>

          <template v-slot:[`item.moTaNVBP`]="{ item }">
            <v-text-field
              v-model="editedItem.moTaNVBP"
              :hide-details="true"
              dense
              single-line
              v-if="item.maNhanDang === editedItem.maNhanDang"
            ></v-text-field>
            <span v-else>{{ item.moTaNVBP }}</span>
          </template>
          <template v-slot:[`item.tenNVBP`]="{ item }">
            <v-text-field
              v-model="editedItem.tenNVBP"
              :hide-details="true"
              dense
              label=""
              :rules="nameRules"
              required
              v-if="item.maNhanDang === editedItem.maNhanDang"
            ></v-text-field>
            <span v-else>{{ item.tenNVBP }}</span>
          </template>
          <template v-slot:[`item.actions`]="{ item }">
            <div v-if="item.maNhanDang === editedItem.maNhanDang">
              <v-icon color="red" class="mr-3" @click="close(false)">
                mdi-window-close
              </v-icon>
              <v-icon color="green" @click="save"> mdi-content-save </v-icon>
            </div>
            <div v-else>
              <v-icon color="green" class="mr-3" @click="editItem(item)">
                mdi-square-edit-outline
              </v-icon>
              <v-icon color="red" @click="deleteItem(item)">
                mdi-delete
              </v-icon>
            </div>
          </template>
          <template v-slot:[`item.ngayBDNVBP`]="{ item }">
            <v-menu
              v-model="menu2"
              :close-on-content-click="false"
              transition="scale-transition"
              offset-y
              min-width="auto"
              v-if="item.maNhanDang === editedItem.maNhanDang"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  v-model="editedItem.ngayBDNVBP"
                  prepend-icon="mdi-calendar"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                v-model="editedItem.ngayBDNVBP"
                @input="menu2 = false"
                no-title
              ></v-date-picker>
            </v-menu>

            <span v-else>{{ item.ngayBDNVBP }}</span>
          </template>
          <template v-slot:[`item.ngayKTNVBP`]="{ item }">
            <v-menu
              v-model="menu3"
              :close-on-content-click="false"
              transition="scale-transition"
              offset-y
              min-width="auto"
              v-if="item.maNhanDang === editedItem.maNhanDang"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  v-model="editedItem.ngayKTNVBP"
                  readonly
                  prepend-icon="mdi-calendar"
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                v-model="editedItem.ngayKTNVBP"
                @input="menu3 = false"
                no-title
              ></v-date-picker>
            </v-menu>
            <span v-else>{{ item.ngayKTNVBP }}</span>
          </template>
          <template v-slot:[`item.trangThaiNVBP`]="{ item }">
            <v-select
              :items="listTrangThai"
              v-model="editedItem.trangThaiNVBP"
              label="Trạng thái"
              v-if="item.maNhanDang === editedItem.maNhanDang"
              dense
              :hide-details="true"
            ></v-select>
            <span v-else>{{
              item.trangThaiNVBP | convertStatus(listTrangThai)
            }}</span>
          </template>

          <template v-slot:[`body.append`]>
            <span></span>
          </template>
        </v-data-table>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import nhiemVuDieuHanh from "@/api/nhiem-vu-dieu-hanh";
import kieuNhiemVu from "@/api/kieu-nhiem-vu";
import donVi from "@/api/don-vi";
import nhiemVuBoPhan from "@/api/nhiem-vu-bo-phan";

export default {
  data() {
    return {
      menu2: false,
      menu3: false,
      search: "",
      isLoading: false,
      isAdding: false,
      isEditing: false,
      headers: this.$appConfig.giaoNhiemVu.headers,
      listNhiemVuBoPhan: [],
      listNhiemVu: [],
      listDonVi: [],
      listTrangThai: [],
      editedIndex: -1,
      editedItem: {
        ...this.$appConfig.giaoNhiemVu.defaultItem,
      },
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

      this.listNhiemVuBoPhan = nhiemVuBP;

      this.isLoading = false;
    } catch (error) {
      console.log(error);
    }
  },

  methods: {
    editItem(item) {
      this.isEditing = true;

      this.editedIndex = this.listNhiemVuBoPhan.indexOf(item);

      this.editedItem = { ...item };
    },

    async deleteItem(item) {
      const index = this.listNhiemVuBoPhan.indexOf(item);
      if (confirm("Bạn có muốn xóa nhiệm vụ không?")) {
        await nhiemVuBoPhan.delete(item);
        this.listNhiemVuBoPhan.splice(index, 1);
      }
    },

    close(isSaved) {
      this.editedItem = { ...this.defaultItem };
      this.editedIndex = -1;

      this.isAdding && !isSaved && this.listNhiemVuBoPhan.shift();

      this.isAdding = false;
      this.isEditing = false;
    },

    addNew() {
      this.isAdding = true;

      const addObj = { ...this.defaultItem };

      this.listNhiemVuBoPhan.unshift(addObj);

      this.editItem(addObj);
    },
    async save() {
      try {
        let { tenNVBP, moTaNVBP, trangThaiNVBP, maNVDH, maDV } =
          this.editedItem;

        if (
          tenNVBP.length === 0 ||
          moTaNVBP.length === 0 ||
          trangThaiNVBP === null ||
          maNVDH === null ||
          maDV === null
        )
          return;
        //Thong bao

        let result;
        if (this.isAdding) {
          result = await nhiemVuBoPhan.create(this.editedItem);
        } else if (this.isEditing) {
          result = await nhiemVuBoPhan.edit(this.editedItem);
        }

        console.log(result);

        if (!!result && this.editedIndex > -1) {
          Object.assign(this.listNhiemVuBoPhan[this.editedIndex], result);
          //Thong bao
        }
      } catch (error) {
        console.log(error);
      }

      this.close(true);
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
