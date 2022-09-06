import { ApiConstant } from "@/constants";
import service from "@/utils/request";

class NhiemVuBoPhanApi {
  getAll = ({ params }) => {
    const url = ApiConstant.route.NHIEM_VU_BO_PHAN;

    return service.get(url, { params });
  };

  getTrangThaiBPNV = ({ params }) => {
    const url = ApiConstant.route.TRANG_THAI_NVBP;

    return service.get(url, { params });
  };

  create = (item) => {
    const url = ApiConstant.route.NHIEM_VU_BO_PHAN;

    return service.post(url, { ...item });
  };

  edit = (item) => {
    const url = `${ApiConstant.route.NHIEM_VU_BO_PHAN}${item.maNVBP}/`;

    return service.put(url, item);
  };

  delete = (item) => {
    const url = `${ApiConstant.route.NHIEM_VU_BO_PHAN}${item.maNVBP}/`;
    return service.delete(url);
  };
}

const nhiemVuBoPhan = new NhiemVuBoPhanApi();

export default nhiemVuBoPhan;
