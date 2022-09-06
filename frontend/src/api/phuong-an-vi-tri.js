import { ApiConstant } from "@/constants";
import service from "@/utils/request";

class PhuongAnViTri {
  getAll = ({ params }) => {
    const url = ApiConstant.route.PHUONG_AN_VI_TRI;

    return service.get(url, { params });
  };

  read = (maPAVT) => {
    const url = ApiConstant.route.PHUONG_AN_VI_TRI + maPAVT + "/";

    return service.get(url);
  };
}

const phuongAnViTri = new PhuongAnViTri();

export default phuongAnViTri;
