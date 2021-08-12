import { ref } from "vue";
import axios from "axios";

const error = ref(null);

const login = async (email, password) => {
  error.value = null;

  try {
    const res = await axios.post(
      "https://referro.herokuapp.com/authentication/token/",
      {
        email,
        password,
      }
    );
    localStorage.setItem("token", res.data.access);

    error.value = null;
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
