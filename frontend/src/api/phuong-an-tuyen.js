import { ApiConstant } from "@/constants";
import service from "@/utils/request";

class PhuongAnTuyen {
  getAll = ({ params }) => {
    const url = ApiConstant.route.PHUONG_AN_TUYEN;

    return service.get(url, { params });
  };

  read = (maPAT) => {
    const url = ApiConstant.route.PHUONG_AN_TUYEN + maPAT + "/";

    return service.get(url);
  };
  create = (item) => {
    const url = ApiConstant.route.PHUONG_AN_TUYEN;

    return service.post(url, { ...item });
  };

  edit = (item) => {
    const url = `${ApiConstant.route.PHUONG_AN_TUYEN}${item.id}/`;

    return service.put(url, { ...item });
  };

  getStatus = ({ params }) => {
    const url = ApiConstant.route.PHUONG_AN_TUYEN + "trangthai-pat/";

    return service.get(url, { params });
  };
}

const phuongAnTuyen = new PhuongAnTuyen();

export default phuongAnTuyen;
