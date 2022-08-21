import { ApiConstant } from "@/constants";
import service from "@/utils/request";

class VungNhiemVuDieuHanh {
  getAll = ({ params }) => {
    const url = ApiConstant.route.VUNG_NHIEM_VU_DIEU_HANH;

    return service.get(url, { params });
  };
}

const vungNhiemVuDieuHanh = new VungNhiemVuDieuHanh();

export default vungNhiemVuDieuHanh;
