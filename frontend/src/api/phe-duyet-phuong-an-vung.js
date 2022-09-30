import { ApiConstant } from "@/constants";
import service from "@/utils/request";

class PheDuyetPhuongAnVung {
  getAll = ({ params }) => {
    const url = ApiConstant.route.PHE_DUYET_PHUONG_AN_VUNG;

    return service.get(url, { params });
  };

  create = (item) => {
    const url = ApiConstant.route.PHE_DUYET_PHUONG_AN_VUNG;

    return service.post(url, { ...item });
  };

  edit = (item) => {
    const url = `${ApiConstant.route.PHE_DUYET_PHUONG_AN_VUNG}${item.id}/`;

    return service.put(url, { ...item });
  };

  delete = (item) => {
    const url = `${ApiConstant.route.PHE_DUYET_PHUONG_AN_VUNG}${item.id}/`;
    return service.delete(url);
  };

  getStatus = ({ params }) => {
    const url = ApiConstant.route.PHE_DUYET_PHUONG_AN_VUNG + "trangthai-cmpav/";

    return service.get(url, { params });
  };
}

const pheDuyetPhuongAnVung = new PheDuyetPhuongAnVung();

export default pheDuyetPhuongAnVung;
