import { ref } from "vue";
import axios from "axios";

const error = ref(null);

const login = async (email, password) => {
  error.value = null;

  try {
    const url = "https://referro.herokuapp.com/authentication/token/";

    const res = await axios.post(url, {
      email,
      password,
    });
    error.value = null;
    localStorage.setItem("token", res.data.access);
    return res;
  } catch (err) {
    console.log(err.message);
    error.value = "Incorrect login credentials";
  }
};

const useLogin = () => {
  return { error, login };
};

export default useLogin;
