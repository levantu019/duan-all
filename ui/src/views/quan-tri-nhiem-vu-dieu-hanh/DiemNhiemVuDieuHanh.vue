<template>
  <v-container>
    <v-row>
      <v-col cols="12">
        <v-data-table
          :headers="headers"
          :items="listDiemNhiemVu"
          :search="search"
          class="elevation-1"
          height="calc(50vh - 235px)"
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
                <v-btn color="primary" class="ml-2 white--text" @click="addNew">
                  <v-icon dark>mdi-plus</v-icon>Thêm mới
                </v-btn>
              </div>
            </v-toolbar>
          </template>

          <!-- <template v-slot:[`item.maDiem`]="{ item }">
            <v-text-field
              v-model="editedItem.maDiem"
              :hide-details="true"
              dense
              single-line
              v-if="item.maDiem === editedItem.maDiem"
            ></v-text-field>
            <span v-else>{{ item.maDiem }}</span>
          </template> -->
          <template v-slot:[`item.tenDiem`]="{ item }">
            <v-text-field
              v-model="editedItem.tenDiem"
              :hide-details="true"
              dense
              single-line
              v-if="item.maDiem === editedItem.maDiem"
            ></v-text-field>
            <span v-else>{{ item.tenDiem }}</span>
          </template>
          <template v-slot:[`item.actions`]="{ item }">
            <div v-if="item.maDiem === editedItem.maDiem">
              <v-icon color="red" class="mr-3" @click="close">
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
          <template v-slot:[`item.nvdh`]="{ item }">
            <v-select
              :items="listKieuNhiemVu"
              v-model="editedItem.kieuNVDH"
              label="Nhiệm vụ"
              v-if="item.maNVDH === editedItem.maNVDH"
              dense
              :hide-details="true"
              required
              :rules="nameRules"
            ></v-select>
            <span v-else>{{ item.kieuNVDH }}</span>
          </template>
          <template v-slot:[`item.moTaDiem`]="{ item }">
            <v-text-field
              v-model="editedItem.moTaDiem"
              :hide-details="true"
              dense
              single-line
              v-if="item.maNVDH === editedItem.maNVDH"
            ></v-text-field>
            <span v-else>{{ item.moTaNV }}</span>
          </template>
          <template v-slot:[`item.ngayDiem`]="{ item }">
            <v-menu
              v-model="menu2"
              :close-on-content-click="false"
              transition="scale-transition"
              offset-y
              min-width="auto"
              v-if="item.maDiem === editedItem.maDiem"
            >
              <template v-slot:activator="{ on, attrs }">
                <v-text-field
                  prepend-icon="mdi-calendar"
                  v-model="item.ngayDiem"
                  readonly
                  v-bind="attrs"
                  v-on="on"
                ></v-text-field>
              </template>
              <v-date-picker
                v-model="item.ngayDiem"
                @input="menu2 = false"
                no-title
              ></v-date-picker>
            </v-menu>

            <span v-else>{{ item.ngayDiem }}</span>
          </template>
          <template v-slot:[`body.append`]>
            <divider />
          </template>
        </v-data-table>
      </v-col>
    </v-row>
    <v-row>
      <MapComponent />
    </v-row>
  </v-container>
</template>

<script>
import diemNhiemVuDieuHanh from "@/api/diem-nhiem-vu-dieu-hanh";
import MapComponent from "@/components/ol/MapComponent.vue";

export default {
  components: {
    MapComponent,
  },
  data() {
    return {
      search: "",
      menu2: false,
      isLoading: false,
      isAdding: false,
      headers: [
        {
          text: "Thao tác",
          value: "actions",
          sortable: false,
          width: "100px",
          align: "center",
          divider: true,
        },

        {
          text: "Nhiệm vụ",
          value: "nvdh",
          sortable: false,
          align: "center",
          divider: true,
        },
        // {
        //   text: "Mã Điểm",
        //   value: "maDiem",
        //   sortable: false,
        //   align: "center",
        //   divider: true,
        // },
        {
          text: "Tên điểm",
          value: "tenDiem",
          sortable: false,
          align: "center",
          divider: true,
        },
        {
          text: "Mô tả điểm",
          value: "moTaDiem",
          sortable: false,
          align: "center",
          divider: true,
        },
        {
          text: "Thời gian",
          value: "ngayDiem",
          sortable: false,
          align: "center",
          divider: true,
        },
      ],
      listDiemNhiemVu: [],
      editedIndex: -1,
      editedItem: {
        maDiem: 0,
        tenDiem: "",
        moTaDiem: "",
        ngayDiem: "",
        nvdh: 0,
      },
      defaultItem: {
        maDiem: 0,
        tenDiem: "",
        moTaDiem: "",
        ngayDiem: "",
        nvdh: 0,
      },
    };
  },
  async created() {
    try {
      this.isLoading = true;

      const data = await diemNhiemVuDieuHanh.getAll({});

      const listFeatures = data.results.features;

      this.listDiemNhiemVu = listFeatures.map((feature) => ({
        ...feature["properties"],
        maDiem: feature.id,
      }));
      this.isLoading = false;
    } catch (error) {
      console.log(error);
    }
  },

  methods: {
    editItem(item) {
      this.editedIndex = this.listDiemNhiemVu.indexOf(item);
      this.editedItem = Object.assign({}, item);
    },

    deleteItem(item) {
      const index = this.listDiemNhiemVu.indexOf(item);
      confirm("Are you sure you want to delete this item?") &&
        this.desserts.splice(index, 1);
    },

    close() {
      this.editedItem = Object.assign({}, this.defaultItem);
      this.editedIndex = -1;

      this.isAdding && this.listDiemNhiemVu.shift();

      this.isAdding = false;
    },
    addNew() {
      this.isAdding = true;

      const addObj = Object.assign({}, this.defaultItem);
      addObj.maDiem = "0" + (this.listDiemNhiemVu.length + 1);

      this.listDiemNhiemVu.unshift(addObj);

      this.editItem(addObj);
    },
    save() {
      if (this.editedIndex > -1) {
        Object.assign(this.listDiemNhiemVu[this.editedIndex], this.editedItem);
      }
      this.close();
    },
  },
};
</script>

<style>
.theme--light.v-data-table.v-data-table--fixed-header thead th {
  background: rgb(160, 159, 159) !important;
}
</style>
