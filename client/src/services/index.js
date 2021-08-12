import axios from "axios";

const baseInstance = axios.create({
  baseURL: "https://referro.herokuapp.com/",
  timeout: 1000,
});

const authInstance = axios.create({
  baseURL: "https://referro.herokuapp.com/",
  headers: {
    Authorization: "Bearer " + localStorage.getItem("token"),
  },
});

export { baseInstance, authInstance };
