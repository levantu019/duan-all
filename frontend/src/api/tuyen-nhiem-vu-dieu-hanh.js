import { ApiConstant } from "@/constants";
import service from "@/utils/request";

class TuyenNhiemVuDieuHanh {
  getAll = ({ params }) => {
    const url = ApiConstant.route.TUYEN_NHIEM_VU_DIEU_HANH;

    return service.get(url, { params });
  };
}

const tuyenNhiemVuDieuHanh = new TuyenNhiemVuDieuHanh();

export default tuyenNhiemVuDieuHanh;
