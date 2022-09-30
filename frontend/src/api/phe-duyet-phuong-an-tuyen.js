import { ApiConstant } from "@/constants";
import service from "@/utils/request";

class PheDuyetPhuongAnTuyen {
  getAll = ({ params }) => {
    const url = ApiConstant.route.PHE_DUYET_PHUONG_AN_TUYEN;

    return service.get(url, { params });
  };

  create = (item) => {
    const url = ApiConstant.route.PHE_DUYET_PHUONG_AN_TUYEN;

    return service.post(url, { ...item });
  };

  edit = (item) => {
    const url = `${ApiConstant.route.PHE_DUYET_PHUONG_AN_TUYEN}${item.id}/`;

    return service.put(url, { ...item });
  };

  delete = (item) => {
    const url = `${ApiConstant.route.PHE_DUYET_PHUONG_AN_TUYEN}${item.id}/`;
    return service.delete(url);
  };

  getStatus = ({ params }) => {
    const url =
      ApiConstant.route.PHE_DUYET_PHUONG_AN_TUYEN + "trangthai-cmpat/";

    return service.get(url, { params });
  };
}

const pheDuyetPhuongAnTuyen = new PheDuyetPhuongAnTuyen();

export default pheDuyetPhuongAnTuyen;
