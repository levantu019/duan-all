import { ApiConstant } from "@/constants";
import service from "@/utils/request";

class PheDuyetPAGanLLApi {
  getAll = ({ params }) => {
    const url = ApiConstant.route.PHE_DUYET_PHUONG_AN_GAN_LL;

    return service.get(url, { params });
  };

  // getTrangThaiBPNV = ({ params }) => {
  //   const url = ApiConstant.route.TRANG_THAI_NVBP;

  //   return service.get(url, { params });
  // };

  // create = (item) => {
  //   const url = ApiConstant.route.NHIEM_VU_BO_PHAN;

  //   return service.post(url, { ...item });
  // };

  // edit = (item) => {
  //   const url = `${ApiConstant.route.NHIEM_VU_BO_PHAN}${item.maNVBP}/`;

  //   return service.put(url, item);
  // };

  // delete = (item) => {
  //   const url = `${ApiConstant.route.NHIEM_VU_BO_PHAN}${item.maNVBP}/`;
  //   return service.delete(url);
  // };

  getStatus = ({ params }) => {
    const url =
      ApiConstant.route.PHE_DUYET_PHUONG_AN_GAN_LL + "trangthai-cmgll/";

    return service.get(url, { params });
  };
}

const pheDuyetPAGanLLApi = new PheDuyetPAGanLLApi();

export default pheDuyetPAGanLLApi;
