import { ApiConstant } from "@/constants";
import service from "@/utils/request";

class LopDuLieu {
  getAll = ({ params }) => {
    const url = ApiConstant.route.LOP_DU_LIEU;

    return service.get(url, { params });
  };
}

const lopDuLieu = new LopDuLieu();

export default lopDuLieu;
