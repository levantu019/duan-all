import { ApiConstant } from "@/constants";
import service from "@/utils/request";

class DiemNhiemVuDieuHanh {
  getAll = ({ params }) => {
    const url = ApiConstant.route.DIEM_NHIEM_VU_DIEU_HANH;

    return service.get(url, { params });
  };

  create = (item) => {
    const url = ApiConstant.route.DIEM_NHIEM_VU_DIEU_HANH;

    return service.post(url, { ...item });
  };

  edit = (item) => {
    console.log(item);
    const url = `${ApiConstant.route.DIEM_NHIEM_VU_DIEU_HANH}${item.id}/`;

    return service.put(url, { ...item });
  };

  delete = (item) => {
    const url = `${ApiConstant.route.DIEM_NHIEM_VU_DIEU_HANH}${item.id}/`;
    return service.delete(url);
  };
}

const diemNhiemVuDieuHanh = new DiemNhiemVuDieuHanh();

export default diemNhiemVuDieuHanh;
