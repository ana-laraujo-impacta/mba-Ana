import { useNavigate } from "react-router-dom";

export const useLogin = () => {
  const navigate = useNavigate();

  const goToLogin: () => void = () => {
    navigate("/login");
  };

  return { goToLogin };
};
