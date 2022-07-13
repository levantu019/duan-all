import { ApiConstant } from "@/constants";
import service from "@/utils/request";

class DiemNhiemVuDieuHanh {
  getAll = ({ params }) => {
    const url = ApiConstant.route.DIEM_NHIEM_VU_DIEU_HANH;

    return service.get(url, { params });
  };
}

const diemNhiemVuDieuHanh = new DiemNhiemVuDieuHanh();

export default diemNhiemVuDieuHanh;
