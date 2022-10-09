import { ApiConstant } from "@/constants";
import service from "@/utils/request";

class PhuongAnVung {
  getAll = ({ params }) => {
    const url = ApiConstant.route.PHUONG_AN_VUNG;

    return service.get(url, { params });
  };

  read = (maPAT) => {
    const url = ApiConstant.route.PHUONG_AN_VUNG + maPAT + "/";

    return service.get(url);
  };
  create = (item) => {
    const url = ApiConstant.route.PHUONG_AN_VUNG;

    return service.post(url, { ...item });
  };

  edit = (item) => {
    const url = `${ApiConstant.route.PHUONG_AN_VUNG}${item.id}/`;

    return service.put(url, { ...item });
  };

  getStatus = ({ params }) => {
    const url = ApiConstant.route.PHUONG_AN_VUNG + "trangthai-pav/";

    return service.get(url, { params });
  };
}

const phuongAnVung = new PhuongAnVung();

export default phuongAnVung;
