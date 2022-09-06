import { ApiConstant } from "@/constants";
import service from "@/utils/request";

class PheDuyetPhuongAnViTri {
  getAll = ({ params }) => {
    const url = ApiConstant.route.PHE_DUYET_PHUONG_AN_VI_TRI;

    return service.get(url, { params });
  };

  create = (item) => {
    const url = ApiConstant.route.PHE_DUYET_PHUONG_AN_VI_TRI;

    return service.post(url, { ...item });
  };

  edit = (item) => {
    const url = `${ApiConstant.route.PHE_DUYET_PHUONG_AN_VI_TRI}${item.id}/`;

    return service.put(url, { ...item });
  };

  delete = (item) => {
    const url = `${ApiConstant.route.PHE_DUYET_PHUONG_AN_VI_TRI}${item.id}/`;
    return service.delete(url);
  };

  getStatus = ({ params }) => {
    const url =
      ApiConstant.route.PHE_DUYET_PHUONG_AN_VI_TRI + "trangthai-cmpavt/";

    return service.get(url, { params });
  };
}

const pheDuyetPhuongAnViTri = new PheDuyetPhuongAnViTri();

export default pheDuyetPhuongAnViTri;
