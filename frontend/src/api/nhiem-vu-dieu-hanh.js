import { ApiConstant } from "@/constants";
import service from "@/utils/request";

class NhiemVuDieuHanhApi {
  getAll = ({ params }) => {
    const url = ApiConstant.route.NHIEM_VU_DIEU_HANH;

    return service.get(url, { params });
  };

  create = (item) => {
    const url = ApiConstant.route.NHIEM_VU_DIEU_HANH;

    return service.post(url, { ...item });
  };

  edit = (item) => {
    const url = `${ApiConstant.route.NHIEM_VU_DIEU_HANH}${item.maNhanDang}/`;

    return service.put(url, item);
  };

  delete = (item) => {
    const url = `${ApiConstant.route.NHIEM_VU_DIEU_HANH}${item.maNhanDang}/`;
    return service.delete(url);
  };
}

const nhiemVuDieuHanh = new NhiemVuDieuHanhApi();

export default nhiemVuDieuHanh;
