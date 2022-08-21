<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-data-table
          :headers="headers"
          :items="listNhiemVu"
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
            <v-text-field
              v-model="editedItem.tenNVDH"
              :hide-details="true"
              dense
              label="Tên nhiệm vụ"
              :autofocus="true"
              :rules="nameRules"
              required
              v-if="item.maNVDH === editedItem.maNVDH"
            ></v-text-field>
            <span v-else>{{ item.tenNVDH }}</span>
          </template>
          <template v-slot:[`item.moTaNV`]="{ item }">
            <v-text-field
              v-model="editedItem.moTaNV"
              :hide-details="true"
              dense
              single-line
              v-if="item.maNVDH === editedItem.maNVDH"
            ></v-text-field>
            <span v-else>{{ item.moTaNV }}</span>
          </template>
          <template v-slot:[`item.chihuyNVDH`]="{ item }">
            <v-text-field
              v-model="editedItem.chihuyNVDH"
              :hide-details="true"
              dense
              label="Người điều hành"
              :rules="nameRules"
              required
              v-if="item.maNVDH === editedItem.maNVDH"
            ></v-text-field>
            <span v-else>{{ item.chihuyNVDH }}</span>
          </template>
          <template v-slot:[`item.actions`]="{ item }">
            <div v-if="item.maNVDH === editedItem.maNVDH">
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
          <template v-slot:[`item.ngayBDNVDH`]="{ item }">
            <v-menu
              v-model="menu2"
              :close-on-content-click="false"
              transition="scale-transition"
              offset-y
              min-width="auto"
              v-if="item.maNVDH === editedItem.maNVDH"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  v-model="editedItem.ngayBDNVDH"
                  prepend-icon="mdi-calendar"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                v-model="editedItem.ngayBDNVDH"
                @input="menu2 = false"
                no-title
              ></v-date-picker>
            </v-menu>

            <span v-else>{{ item.ngayBDNVDH }}</span>
          </template>
          <template v-slot:[`item.ngayKTNVDH`]="{ item }">
            <v-menu
              v-model="menu3"
              :close-on-content-click="false"
              transition="scale-transition"
              offset-y
              min-width="auto"
              v-if="item.maNVDH === editedItem.maNVDH"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  v-model="editedItem.ngayKTNVDH"
                  readonly
                  prepend-icon="mdi-calendar"
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                v-model="editedItem.ngayKTNVDH"
                @input="menu3 = false"
                no-title
              ></v-date-picker>
            </v-menu>
            <span v-else>{{ item.ngayKTNVDH }}</span>
          </template>
          <template v-slot:[`item.vanbanNVDH`]="{ item }">
            <v-btn icon color="red">
              <v-icon>mdi-file-pdf-box</v-icon> {{ item[0] }}
            </v-btn>
          </template>
          <template v-slot:[`item.kieuNVDH`]="{ item }">
            <v-select
              :items="listKieuNhiemVu"
              v-model="editedItem.kieuNVDH"
              label="Kiểu nhiệm vụ"
              v-if="item.maNVDH === editedItem.maNVDH"
              dense
              :hide-details="true"
              required
              :rules="nameRules"
            ></v-select>
            <span v-else>{{ item.kieuNVDH }}</span>
          </template>
          <template v-slot:[`item.trang_thai`]="{ item }">
            <v-text-field
              :hide-details="true"
              dense
              single-line
              v-if="item.maNVDH === editedItem.maNVDH"
            ></v-text-field>
            <span v-else>{{ item.trang_thai }}</span>
          </template>
          <template v-slot:no-data>
            <v-btn color="primary" @click="initialize">Reset</v-btn>
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

export default {
  data() {
    return {
      menu2: false,
      menu3: false,
      search: "",
      isLoading: false,
      isAdding: false,
      isEditing: false,
      headers: this.$appConfig.nhiemVuDieuHanh.headers,
      listNhiemVu: [],
      listKieuNhiemVu: [],
      editedIndex: -1,
      editedItem: {
        ...this.$appConfig.nhiemVuDieuHanh.defaultItem,
      },
      defaultItem: {
        ...this.$appConfig.nhiemVuDieuHanh.defaultItem,
      },
      nameRules: [(v) => !!v || "Name is required"],
    };
  },
  async created() {
    try {
      this.isLoading = true;

      const [nhiemVu, kieuNV] = await Promise.all([
        nhiemVuDieuHanh.getAll({}),
        kieuNhiemVu.getAll({}),
      ]);

      this.listNhiemVu = nhiemVu.results.map((item) => {
        let kieuNVDH = kieuNV.filter((m) => m.value === item.kieuNVDH)[0].text;
        return {
          ...item,
          kieuNVDH,
        };
      });
      this.listKieuNhiemVu = kieuNV;

      this.isLoading = false;
    } catch (error) {
      console.log(error);
    }
  },

  methods: {
    editItem(item) {
      this.isEditing = true;

      this.editedIndex = this.listNhiemVu.indexOf(item);

      let converKieuNV = this.listKieuNhiemVu.filter((kieu) => {
        return kieu.text.toLowerCase() === item.kieuNVDH.toLowerCase();
      })[0].value;

      item = { ...item, kieuNVDH: converKieuNV };

      this.editedItem = { ...item };
    },

    async deleteItem(item) {
      const index = this.listNhiemVu.indexOf(item);
      if (confirm("Bạn có muốn xóa nhiệm vụ không?")) {
        await nhiemVuDieuHanh.delete(item);
        this.listNhiemVu.splice(index, 1);
      }
    },

    close(isSaved) {
      this.editedItem = { ...this.defaultItem };
      this.editedIndex = -1;

      this.isAdding && !isSaved && this.listNhiemVu.shift();

      this.isAdding = false;
      this.isEditing = false;
    },

    addNew() {
      this.isAdding = true;

      const addObj = { ...this.defaultItem };

      this.listNhiemVu.unshift(addObj);

      this.editItem(addObj);
    },
    async save() {
      try {
        let { tenNVDH, chihuyNVDH, kieuNVDH } = this.editedItem;

        if (
          tenNVDH.length === 0 ||
          chihuyNVDH.length === 0 ||
          kieuNVDH === null
        )
          return;
        //Thong bao

        let result;
        if (this.isAdding) {
          result = await nhiemVuDieuHanh.create(this.editedItem);
        } else if (this.isEditing) {
          result = await nhiemVuDieuHanh.edit(this.editedItem);
        }

        result.kieuNVDH = this.listKieuNhiemVu.filter(
          (item) => item.value === result.kieuNVDH
        )[0].text;

        if (!!result && this.editedIndex > -1) {
          Object.assign(this.listNhiemVu[this.editedIndex], result);
          //Thong bao
        }
      } catch (error) {
        console.log(error);
      }

      this.close(true);
    },
  },
};
</script>

<style>
.theme--light.v-data-table.v-data-table--fixed-header thead th {
  background: rgb(160, 159, 159) !important;
}
</style>
