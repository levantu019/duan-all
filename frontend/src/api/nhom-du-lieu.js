import { ApiConstant } from "@/constants";
import service from "@/utils/request";

class NhomDuLieu {
  getAll = ({ params }) => {
    const url = ApiConstant.route.NHOM_DU_LIEU;

    return service.get(url, { params });
  };

  getById = (id) => {
    const url = `${ApiConstant.route.NHOM_DU_LIEU}${id}/`;
    return service.get(url);
  };
}

const nhomDuLieu = new NhomDuLieu();

export default nhomDuLieu;
