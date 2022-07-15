const preURL_API = "/soanthaokehoach";

export const ApiConstant = {
  method: {
    POST: "post",
    GET: "get",
    PUT: "put",
    DELETE: "delete",
  },
  route: {
    NHIEM_VU_DIEU_HANH: `${preURL_API}/nvdh/`,

    KIEU_NHIEM_VU: `${preURL_API}/nvdh/kieu-nvdh/`,

    DIEM_NHIEM_VU_DIEU_HANH: `${preURL_API}/diem-nvdh/`,

    VUNG_NHIEM_VU_DIEU_HANH: `${preURL_API}/vung-nvdh/`,

    TUYEN_NHIEM_VU_DIEU_HANH: `${preURL_API}/tuyen-nvdh`,
  },
};
