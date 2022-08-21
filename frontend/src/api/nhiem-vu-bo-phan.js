import { ApiConstant } from "@/constants";
import service from "@/utils/request";

class NhiemVuBoPhanApi {
  // getAll = ({ params }) => {
  //   const url = ApiConstant.route.NHIEM_VU_DIEU_HANH;

  //   return service.get(url, { params });
  // };

  getTrangThaiBPNV = ({ params }) => {
    const url = ApiConstant.route.TRANG_THAI_NVBP;

    return service.get(url, { params });
  };

  // create = (item) => {
  //   const url = ApiConstant.route.NHIEM_VU_DIEU_HANH;

  //   return service.post(url, { ...item });
  // };

  // edit = (item) => {
  //   const url = `${ApiConstant.route.NHIEM_VU_DIEU_HANH}${item.maNVDH}/`;

  //   return service.put(url, item);
  // };

  // delete = (item) => {
  //   const url = `${ApiConstant.route.NHIEM_VU_DIEU_HANH}${item.maNVDH}/`;
  //   return service.delete(url);
  // };
}

const nhiemVuBoPhan = new NhiemVuBoPhanApi();

export default nhiemVuBoPhan;
