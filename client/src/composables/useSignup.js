import { ref } from "vue";
import axios from "axios";

const error = ref(null);

const signup = async (email, password, displayName) => {
  error.value = null;
  try {
    const url = "https://referro.herokuapp.com/authentication/token/";

    // const res = await projectAuth.createUserWithEmailAndPassword(
    //   email,
    //   password
    // );

    const res = await axios(url, {
      displayName,
      email,
      password,
    });

    if (!res) {
      throw new Error("Could not complete the signup");
    }
    // console.log(res.user);
    await res.user.updateProfile({ displayName });
    error.value = null;
    // console.log(res.user);
    return res;
  } catch (err) {
    // console.log(err.message);
    error.value = err.message;
  }
};

const useSignup = () => {
  return { error, signup };
};

export default useSignup;
