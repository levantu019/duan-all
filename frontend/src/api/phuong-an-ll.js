import { ApiConstant } from "@/constants";
import service from "@/utils/request";

class PhuongAnLucLuong {
  getAll = ({ params }) => {
    const url = ApiConstant.route.PHUONG_AN_LUC_LUONG;

    return service.get(url, { params });
  };

  read = (maPAT) => {
    const url = ApiConstant.route.PHUONG_AN_LUC_LUONG + maPAT + "/";

    return service.get(url);
  };

  create = (item) => {
    const url = ApiConstant.route.PHUONG_AN_LUC_LUONG;

    return service.post(url, { ...item });
  };

  edit = (item) => {
    const url = `${ApiConstant.route.PHUONG_AN_LUC_LUONG}${item.maNhanDang}/`;

    return service.put(url, { ...item });
  };
  delete = (item) => {
    const url = `${ApiConstant.route.PHUONG_AN_LUC_LUONG}${item.maNhanDang}/`;
    return service.delete(url);
  };
}

const phuongAnLucLuong = new PhuongAnLucLuong();

export default phuongAnLucLuong;
