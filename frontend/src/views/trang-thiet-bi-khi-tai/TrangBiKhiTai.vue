<template>
  <div>
    <header-component title="Trang thiết bị khí tài" />
    <nav-component-khi-tai />
    <v-main>
      <v-container fluid>
        <v-row>
          <v-col cols="12">
            <v-data-table
              :headers="headers"
              :items="[]"
              class="elevation-1"
              height="calc(50vh - 235px)"
              :footer-props="{
                'items-per-page-text': 'Hiển thị 1 trang',
                'items-per-page-options': [10, 15, 20],
              }"
              fixed-header
              :loading="isLoading"
              loading-text="Loading...Please wait"
              item-key="name"
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
                      @click="addNewPosition()"
                      :disabled="isAdding"
                    >
                      <v-icon dark>mdi-plus</v-icon>Thêm mới
                    </v-btn>
                  </div>
                </v-toolbar>
              </template>
              <!-- <template v-slot:[`item.tenDiem`]="{ item }">
                <v-text-field
                  v-model="editedItem.properties.tenDiem"
                  :hide-details="true"
                  dense
                  label="Tên điểm"
                  required
                  :rules="nameRules"
                  v-if="item.id === editedItem.id"
                ></v-text-field>
                <span v-else>{{ item.properties.tenDiem }}</span>
              </template>
              <template v-slot:[`item.actions`]="{ item }">
                <div v-if="item.id === editedItem.id">
                  <v-icon color="red" class="mr-2" @click="close(false)">
                    mdi-window-close
                  </v-icon>
                  <v-icon color="green" @click="save">
                    mdi-content-save
                  </v-icon>
                </div>
                <div v-else>
                  <v-icon
                    color="yellow"
                    class="mr-2"
                    @click="zoomToPoint(item)"
                  >
                    mdi-map-marker
                  </v-icon>
                  <v-icon color="green" class="mr-2" @click="editItem(item)">
                    mdi-square-edit-outline
                  </v-icon>
                  <v-icon color="red" @click="deleteItem(item)">
                    mdi-delete
                  </v-icon>
                </div>
              </template>
              <template v-slot:[`item.nvdh`]="{ item }">
                <v-select
                  :items="listNhiemVu"
                  v-model="editedItem.properties.nvdh"
                  label="Nhiệm vụ"
                  v-if="item.id === editedItem.id"
                  dense
                  :hide-details="true"
                  required
                  :rules="nameRules"
                  item-text="tenNVDH"
                  item-value="maNhanDang"
                ></v-select>
                <span v-else>{{
                  item.properties.nvdh | convertNVDH(listNhiemVu)
                }}</span>
              </template>
              <template v-slot:[`item.moTaDiem`]="{ item }">
                <v-text-field
                  v-model="editedItem.properties.moTaDiem"
                  :hide-details="true"
                  dense
                  single-line
                  v-if="item.id === editedItem.id"
                ></v-text-field>
                <span v-else>{{ item.properties.moTaDiem }}</span>
              </template>
              <template v-slot:[`item.ngayDiem`]="{ item }">
                <v-menu
                  v-model="menu2"
                  :close-on-content-click="false"
                  transition="scale-transition"
                  offset-y
                  min-width="auto"
                  v-if="item.id === editedItem.id"
                >
                  <template v-slot:activator="{ on, attrs }">
                    <v-text-field
                      prepend-icon="mdi-calendar"
                      v-model="editedItem.properties.ngayDiem"
                      readonly
                      v-bind="attrs"
                      v-on="on"
                    ></v-text-field>
                  </template>
                  <v-date-picker
                    v-model="editedItem.properties.ngayDiem"
                    @input="menu2 = false"
                    no-title
                  ></v-date-picker>
                </v-menu>

                <span v-else>{{ item.properties.ngayDiem }}</span>
              </template> -->
              <template v-slot:[`body.append`]>
                <span></span>
              </template>
            </v-data-table>
          </v-col>
        </v-row>
        <v-row>
          <MapComponent />
        </v-row>
      </v-container>
    </v-main>

    <v-footer app color="#4472c4">
      <h4 class="white--text">Cập nhật dữ liệu gần nhất: 5/2022</h4>
      <v-spacer></v-spacer>
      <h4 class="white--text">Phiên bản: V1.0</h4>
    </v-footer>
  </div>
</template>

<script>
import HeaderComponent from "@/components/layouts/HeaderComponent.vue";
import NavComponentKhiTai from "@/components/layouts/NavComponentKhiTai.vue";
import MapComponent from "@/components/ol/MapComponent.vue";
export default {
  components: {
    HeaderComponent,
    NavComponentKhiTai,
    MapComponent,
  },
  data() {
    return {
      headers: [
        {
          text: "Thao tác",
          value: "actions",
          sortable: false,
          width: "130px",
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
        {
          text: "Tên vùng",
          value: "tenVung",
          sortable: false,
          align: "center",
          divider: true,
        },
        {
          text: "Mô tả vùng",
          value: "moTaVung",
          sortable: false,
          align: "center",
          divider: true,
        },
        {
          text: "Thời gian",
          value: "ngayVung",
          sortable: false,
          align: "center",
          divider: true,
        },
      ],
      isLoading: false,
      isAdding: false,
    };
  },
};
</script>

<style>
.theme--light.v-data-table.v-data-table--fixed-header thead th {
  background: rgb(160, 159, 159) !important;
}
</style>
