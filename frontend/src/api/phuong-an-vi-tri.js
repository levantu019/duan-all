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

  create = (item) => {
    const url = ApiConstant.route.PHUONG_AN_VI_TRI;

    return service.post(url, { ...item });
  };

  edit = (item) => {
    const url = `${ApiConstant.route.PHUONG_AN_VI_TRI}${item.id}/`;

    return service.put(url, { ...item });
  };

  getStatus = ({ params }) => {
    const url = ApiConstant.route.PHUONG_AN_VI_TRI + "trangthai-pavt/";

    return service.get(url, { params });
  };
}

const phuongAnViTri = new PhuongAnViTri();

export default phuongAnViTri;
