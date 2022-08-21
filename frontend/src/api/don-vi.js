import { ApiConstant } from "@/constants";
import service from "@/utils/request";

class DonViApi {
  getAll = ({ params }) => {
    const url = ApiConstant.route.DON_VI;

    return service.get(url, { params });
  };

  // create = (item) => {
  //   const url = ApiConstant.route.NHIEM_VU_DIEU_HANH;

  //   return service.post(url, { ...item });
  // };

  // edit = (item) => {
  //   const url = `${ApiConstant.route.NHIEM_VU_DIEU_HANH}${item.maNVDH}/`;

  //   return service.put(url, item);
  // };

  // delete = (item) => {
  //   const url = `${ApiConstant.route.NHIEM_VU_DIEU_HANH}${item.maNVDH}/`;
  //   return service.delete(url);
  // };
}

const donViApi = new DonViApi();

export default donViApi;
