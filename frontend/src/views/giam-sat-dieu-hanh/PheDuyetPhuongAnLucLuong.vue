<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-data-table
          :headers="headers"
          :items="listPheDuyetPAGanLL"
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

          <template v-slot:[`item.ganLL`]="{ item }">
            <v-select
              :items="listPAGanLL"
              v-model="editedItem.ganLL"
              label="Tên nhiệm vụ"
              v-if="item.maNhanDang === editedItem.maNhanDang"
              dense
              item-text="tenGanLL"
              item-value="maNhanDang"
              :hide-details="true"
            ></v-select>
            <span v-else>{{ item.ganLL | showTenPA(listPAGanLL) }}</span>
          </template>

          <template v-slot:[`item.cmNoiDungNhiemVuGanLL`]="{ item }">
            <v-text-field
              v-model="editedItem.cmNoiDungNhiemVuGanLL"
              :hide-details="true"
              dense
              single-line
              v-if="item.maNhanDang === editedItem.maNhanDang"
            ></v-text-field>
            <span v-else>{{ item.cmNoiDungNhiemVuGanLL }}</span>
          </template>
          <template v-slot:[`item.cmDonViGanLL`]="{ item }">
            <v-text-field
              v-model="editedItem.cmDonViGanLL"
              :hide-details="true"
              dense
              label=""
              :rules="nameRules"
              required
              v-if="item.maNhanDang === editedItem.maNhanDang"
            ></v-text-field>
            <span v-else>{{ item.cmDonViGanLL }}</span>
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
          <template v-slot:[`item.ngayPheDuyet`]="{ item }">
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
                  v-model="editedItem.ngayPheDuyet"
                  prepend-icon="mdi-calendar"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                v-model="editedItem.ngayPheDuyet"
                @input="menu2 = false"
                no-title
              ></v-date-picker>
            </v-menu>

            <span v-else>{{ item.ngayPheDuyet }}</span>
          </template>
          <template v-slot:[`item.trangThaiCMGanLL`]="{ item }">
            <v-select
              :items="listTrangThai"
              v-model="editedItem.trangThaiCMGanLL"
              label="Trạng thái"
              v-if="item.maNhanDang === editedItem.maNhanDang"
              dense
              :hide-details="true"
            ></v-select>
            <span v-else>{{
              item.trangThaiCMGanLL | convertStatus(listTrangThai)
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
import pheDuyetPAGanLLApi from "@/api/phe-duyet-phuong-an-gan-ll";
import phuongAnLucLuong from "@/api/phuong-an-ll";
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
      headers: this.$appConfig.pheDuyetPhuongAnGanLL.headers,
      listPAGanLL: [],
      listPheDuyetPAGanLL: [],
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
      const [pheDuyetPAGanLL, paGanLL, trangThaiPA] = await Promise.all([
        pheDuyetPAGanLLApi.getAll({}),
        phuongAnLucLuong.getAll({}),
        pheDuyetPAGanLLApi.getStatus({}),
      ]);

      console.log(pheDuyetPAGanLL, paGanLL, trangThaiPA);

      // transform data

      this.listPheDuyetPAGanLL = pheDuyetPAGanLL;
      // .map((item) => {
      //   let paLL = paGanLL.find((pa) => pa.maNhanDang === item.ganLL);
      //   return {
      //     ...item,
      //     tenGanLL: paLL.tenGanLL,
      //   };
      // });

      this.listPAGanLL = paGanLL;

      this.listTrangThai = trangThaiPA;

      this.isLoading = false;
    } catch (error) {
      console.log(error);
    }
  },

  methods: {
    editItem(item) {
      this.isEditing = true;

      this.editedIndex = this.listPheDuyetPAGanLL.indexOf(item);

      this.editedItem = { ...item };
    },

    async deleteItem(item) {
      const index = this.listPheDuyetPAGanLL.indexOf(item);
      if (confirm("Bạn có muốn xóa nhiệm vụ không?")) {
        await nhiemVuBoPhan.delete(item);
        this.listPAGanLL.splice(index, 1);
      }
    },

    close(isSaved) {
      this.editedItem = { ...this.defaultItem };
      this.editedIndex = -1;

      this.isAdding && !isSaved && this.listPheDuyetPAGanLL.shift();

      this.isAdding = false;
      this.isEditing = false;
    },

    addNew() {
      this.isAdding = true;

      const addObj = { ...this.defaultItem };

      this.listPheDuyetPAGanLL.unshift(addObj);

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
          Object.assign(this.listPheDuyetPAGanLL[this.editedIndex], result);
          //Thong bao
        }
      } catch (error) {
        console.log(error);
      }

      this.close(true);
    },
  },
  filters: {
    convertStatus: (trangThaiCMGanLL, listStatus) => {
      if (!trangThaiCMGanLL) return "";

      return listStatus.filter((stt) => stt.value === trangThaiCMGanLL)[0].text;
    },
    showTenPA(ganLL, listPAGanLL) {
      if (!ganLL) return "";

      return listPAGanLL.find((paLL) => paLL.maNhanDang === ganLL).tenGanLL;
    },
  },
};
</script>

<style>
.theme--light.v-data-table.v-data-table--fixed-header thead th {
  background: rgb(160, 159, 159) !important;
}
</style>
