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

    TUYEN_NHIEM_VU_DIEU_HANH: `${preURL_API}/tuyen-nvdh/`,

    DON_VI: `${preURL_API}/don-vi/`,

    TRANG_THAI_NVBP: `${preURL_API}/nvbp/trangthai-nvbp/`,

    NHIEM_VU_BO_PHAN: `${preURL_API}/nvbp/`,

    PHE_DUYET_PHUONG_AN_VI_TRI: `${preURL_API}/phe-duyet-phuong-an-vi-tri/`,

    PHUONG_AN_VI_TRI: `${preURL_API}/phuong-an-vi-tri/`,
  },
};
