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
}

const phuongAnTuyen = new PhuongAnTuyen();

export default phuongAnTuyen;
