import { ApiConstant } from "@/constants";
import service from "@/utils/request";

class KieuNhiemVu {
  getAll = ({ params }) => {
    const url = ApiConstant.route.KIEU_NHIEM_VU;

    return service.get(url, { params });
  };
}

const kieuNhiemVu = new KieuNhiemVu();

export default kieuNhiemVu;
