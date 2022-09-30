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
}

const phuongAnVung = new PhuongAnVung();

export default phuongAnVung;
