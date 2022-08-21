import { ApiConstant } from "@/constants";
import service from "@/utils/request";

class TuyenNhiemVuDieuHanh {
  getAll = ({ params }) => {
    const url = ApiConstant.route.TUYEN_NHIEM_VU_DIEU_HANH;

    return service.get(url, { params });
  };

  create = (item) => {
    const url = `${ApiConstant.route.TUYEN_NHIEM_VU_DIEU_HANH}/`;

    return service.post(url, { ...item });
  };

  edit = (item) => {
    const url = `${ApiConstant.route.TUYEN_NHIEM_VU_DIEU_HANH}/${item.id}/`;

    return service.put(url, { ...item });
  };

  delete = (item) => {
    const url = `${ApiConstant.route.TUYEN_NHIEM_VU_DIEU_HANH}/${item.id}/`;
    return service.delete(url);
  };
}

const tuyenNhiemVuDieuHanh = new TuyenNhiemVuDieuHanh();

export default tuyenNhiemVuDieuHanh;
