<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-data-table
          :headers="headers"
          :items="listPAGanLL"
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

          <template v-slot:[`item.xx`]="{ item }">
            <v-select
              :items="listNhiemVu"
              v-model="editedItem.tenGanLL"
              label="Tên nhiệm vụ"
              v-if="item.maNhanDang === editedItem.maNhanDang"
              dense
              item-text="tenNVDH"
              item-value="maNhanDang"
              :hide-details="true"
            ></v-select>
            <span v-else>{{ item.tenGanLL }}</span>
          </template>

          <template v-slot:[`item.trangThaiLL`]="{ item }">
            <v-select
              :items="listTrangThai"
              v-model="editedItem.trangThaiLL"
              label="Trạng thái"
              v-if="item.maNhanDang === editedItem.maNhanDang"
              dense
              :hide-details="true"
            ></v-select>
            <span v-else>{{ item.trangThaiLL }}</span>
          </template>

          <template v-slot:[`item.noiDungNhiemVuGanLL`]="{ item }">
            <v-text-field
              v-model="editedItem.noiDungNhiemVuGanLL"
              :hide-details="true"
              dense
              single-line
              v-if="item.maNhanDang === editedItem.maNhanDang"
            ></v-text-field>
            <span v-else>{{ item.noiDungNhiemVuGanLL }}</span>
          </template>
          <template v-slot:[`item.quanSoGanLL`]="{ item }">
            <v-text-field
              v-model="editedItem.quanSoGanLL"
              :hide-details="true"
              dense
              label=""
              required
              v-if="item.maNhanDang === editedItem.maNhanDang"
            ></v-text-field>
            <span v-else>{{ item.quanSoGanLL }}</span>
          </template>
          <template v-slot:[`item.tenGanLL`]="{ item }">
            <v-text-field
              v-model="editedItem.tenGanLL"
              :hide-details="true"
              dense
              label=""
              :rules="nameRules"
              required
              v-if="item.maNhanDang === editedItem.maNhanDang"
            ></v-text-field>
            <span v-else>{{ item.tenGanLL }}</span>
          </template>
          <template v-slot:[`item.donViGanLL`]="{ item }">
            <v-text-field
              v-model="editedItem.donViGanLL"
              :hide-details="true"
              dense
              label=""
              :rules="nameRules"
              required
              v-if="item.maNhanDang === editedItem.maNhanDang"
            ></v-text-field>
            <span v-else>{{ item.donViGanLL }}</span>
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
          <!-- <template v-slot:[`item.ngayBDNVBP`]="{ item }">
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
          </template> -->
          <template v-slot:[`item.pavt`]="{ item }">
            <v-select
              :items="listPAViTri"
              v-model="editedItem.pavt"
              label="Phương án vị trí"
              v-if="item.maNhanDang === editedItem.maNhanDang"
              dense
              :hide-details="true"
              item-text="properties.tenPAVT"
              item-value="id"
            ></v-select>
            <span v-else>{{ item.pavt }}</span>
          </template>
          <template v-slot:[`item.pat`]="{ item }">
            <v-select
              :items="listPATuyen"
              v-model="editedItem.pat"
              label="Phương án tuyến"
              v-if="item.maNhanDang === editedItem.maNhanDang"
              dense
              :hide-details="true"
              item-text="properties.tenPATuyen"
              item-value="id"
            ></v-select>
            <span v-else>{{ item.pat }}</span>
          </template>
          <template v-slot:[`item.pav`]="{ item }">
            <v-select
              :items="listPAVung"
              v-model="editedItem.pav"
              label="Phương án vùng"
              v-if="item.maNhanDang === editedItem.maNhanDang"
              dense
              :hide-details="true"
              item-text="properties.tenPAVung"
              item-value="id"
            ></v-select>
            <span v-else>{{ item.pav }}</span>
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
import phuongAnLL from "@/api/phuong-an-ll";
import phuongAnViTri from "@/api/phuong-an-vi-tri";
import phuongAnTuyen from "@/api/phuong-an-tuyen";
import phuongAnVung from "@/api/phuong-an-vung";

export default {
  data() {
    return {
      menu2: false,
      menu3: false,
      search: "",
      isLoading: false,
      isAdding: false,
      isEditing: false,
      headers: this.$appConfig.quanTriPAGanLucLuong.headers,

      listPAGanLL: [],
      listPAViTri: [],
      listPATuyen: [],
      listPAVung: [],
      listTrangThai: [
        {
          text: "Phương án mới, chưa phê duyệt",
          value: 1,
        },
        {
          value: 2,
          text: "Phương án mới, đã phê duyệt",
        },
        {
          value: 3,
          text: "Phương án chỉnh sửa, đã phê duyệt",
        },
        {
          value: 4,
          text: "Phương án chỉnh sửa, chưa phê duyệt",
        },
      ],

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
      const [paGanLL, paVT, paTuyen, paVung] = await Promise.all([
        phuongAnLL.getAll({}),
        phuongAnViTri.getAll({}),
        phuongAnTuyen.getAll({}),
        phuongAnVung.getAll({}),
      ]);

      this.listPAGanLL = paGanLL;
      this.listPAViTri = paVT.features;
      this.listPATuyen = paTuyen.features;
      this.listPAVung = paVung.features;

      this.isLoading = false;
    } catch (error) {
      console.log(error);
    }
  },

  methods: {
    editItem(item) {
      this.isEditing = true;

      this.editedIndex = this.listPAGanLL.indexOf(item);

      this.editedItem = { ...item };
    },

    async deleteItem(item) {
      const index = this.listPAGanLL.indexOf(item);
      if (confirm("Bạn có muốn xóa nhiệm vụ không?")) {
        await phuongAnLL.delete(item);
        this.listPAGanLL.splice(index, 1);
      }
    },

    close(isSaved) {
      this.editedItem = { ...this.defaultItem };
      this.editedIndex = -1;

      this.isAdding && !isSaved && this.listPAGanLL.shift();

      this.isAdding = false;
      this.isEditing = false;
    },

    addNew() {
      this.isAdding = true;

      const addObj = { ...this.defaultItem };

      this.listPAGanLL.unshift(addObj);

      this.editItem(addObj);
    },
    async save() {
      try {
        let { tenNVBP, moTaNVBP, trangThaiNVBP, maNVDH, maDV } =
          this.editedItem;

        // if (
        //   tenNVBP.length === 0 ||
        //   moTaNVBP.length === 0 ||
        //   trangThaiNVBP === null ||
        //   maNVDH === null ||
        //   maDV === null
        // )
        //   return;
        // //Thong bao

        let result;
        if (this.isAdding) {
          result = await phuongAnLL.create(this.editedItem);
        } else if (this.isEditing) {
          result = await phuongAnLL.edit(this.editedItem);
        }

        if (!!result && this.editedIndex > -1) {
          Object.assign(this.listPAGanLL[this.editedIndex], result);
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
