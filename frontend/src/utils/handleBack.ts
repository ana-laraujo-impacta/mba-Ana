import { useNavigate } from "react-router-dom";

export const useBack = () => {
  const navigate = useNavigate();

  const handleBack = () => {
    navigate(-1);
  };

  return { handleBack };
};
