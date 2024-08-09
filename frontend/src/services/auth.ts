import axios from "axios";
import { API_URL } from "./variables";

export interface LoginParams {
  email: string;
  password: string;
}
export interface LoginResponse {
  _id: string;
  access_token: string;
  message: string;
}

export interface ChangePasswordParams {
  email: string;
  password: string;
  newPassword: string;
}

export const login = async ({
  email,
  password,
}: LoginParams): Promise<LoginResponse> => {
  const response = await axios.post(`${API_URL}/login`, { email, password });
  console.log("response", response);
  console.log("response", response.data);
  return response.data;
};

export const changePassword = async ({
  email,
  password,
  newPassword,
}: ChangePasswordParams): Promise<any> => {
  const response = await axios.post(`${API_URL}/change-password`, {
    email,
    password,
    newPassword,
  });
  return response.data;
};
