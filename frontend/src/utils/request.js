import axios from "axios";
import queryString from "query-string";
//import store from "@/store";
//import { getToken } from "@/utils/auth";

// create an axios instance
const service = axios.create({
  baseURL: process.env.VUE_APP_BASE_API, // url = base url + request url
  headers: {
    "content-type": "application/json",
  },
  timeout: 5000, // request timeout,
  paramsSerializer: (params) => queryString.stringify(params),
});

// request interceptor
service.interceptors.request.use(
  (config) => {
    // do something before request is sent

    // if (store.getters.token) {
    // let each request carry token
    // ['X-Token'] is a custom headers key
    // please modify it according to the actual situation

    //const token = getToken();
    //config.headers.Authorization = token ? `Bearer ${token}` : "";
    // config.headers['Authorization'] = 'Bearer ' || getToken()

    //  }

    return config;
  },
  (error) => {
    // do something with request error
    //  console.log(error); // for debug
    return Promise.reject(error);
  }
);

// response interceptor
service.interceptors.response.use(
  /**
   * If you want to get http information such as headers or status
   * Please return  response => response
   */

  /**
   * Determine the request status by custom code
   * Here is just an example
   * You can also judge the status by HTTP Status Code
   */
  (response) => {
    if (response && response.data) {
      return response.data;
    }

    return response;
  },
  (error) => {
    throw error;
  }
);

export default service;
