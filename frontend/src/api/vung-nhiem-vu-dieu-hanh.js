import { ApiConstant } from "@/constants";
import service from "@/utils/request";

class VungNhiemVuDieuHanh {
  getAll = ({ params }) => {
    const url = ApiConstant.route.VUNG_NHIEM_VU_DIEU_HANH;

    return service.get(url, { params });
  };
  create = (item) => {
    const url = `${ApiConstant.route.VUNG_NHIEM_VU_DIEU_HANH}`;

    return service.post(url, { ...item });
  };
  edit = (item) => {
    const url = `${ApiConstant.route.VUNG_NHIEM_VU_DIEU_HANH}${item.id}/`;

    return service.put(url, { ...item });
  };
}

const vungNhiemVuDieuHanh = new VungNhiemVuDieuHanh();

export default vungNhiemVuDieuHanh;
