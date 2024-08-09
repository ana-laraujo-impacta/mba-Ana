import { useState } from "react";
import { useMutation, UseMutationResult } from "@tanstack/react-query";
import { login, LoginParams, LoginResponse } from "../../services/auth";
import Button from "../../components/Button/Button";
import Header from "../../components/Header/Header";
import Input from "../../components/Input/Input";
import Divider from "../../components/Divider/Divider";
import Logo from "../../assets/logo.svg";
import styles from "./Login.module.css";
import { useNavigate } from "react-router-dom";

const Login = () => {
  const [email, setEmail] = useState<string>("");
  const [password, setPassword] = useState<string>("");

  const navigate = useNavigate();

  const mutation: UseMutationResult<LoginResponse, any, LoginParams, unknown> =
    useMutation({
      mutationFn: login,
      onSuccess: (data) => {
        alert(data.message);
        console.log("Login successful:", data);
        navigate("/dashboard");
      },
      onError: (error: any) => {
        console.error("Erro ao fazer login:", error);
      },
    });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    mutation.mutate({ email, password });
  };

  return (
    <>
      <Header showArrow={true} />

      <div className={styles.container}>
        <img className={styles.logo} src={Logo} alt="Conexão Pet" />
        <h2>Entre ou crie sua conta</h2>
        <p>Garanta o bem estar do seu Pet</p>
        <form onSubmit={handleSubmit}>
          <Input
            type="email"
            label="E-mail"
            placeholder="Seu e-mail"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            required
          />
          <Input
            type="password"
            label="Senha"
            placeholder="Sua senha"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            required
          />
          <a href="/change-password" className={styles.forgotPassword}>
            Esqueci minha senha
          </a>
          <Button bgColor="--pink-500" color="--white" text="Entrar" type="submit" />
        </form>

        {/* {mutation.isLoading && <p>Logging in...</p>} */}
        {mutation.isError && (
          <p>
            Error:{" "}
            {mutation.error instanceof Error
              ? mutation.error.message
              : "Unknown error"}
          </p>
        )}
        {mutation.isSuccess && <p>Login successful!</p>}

        <Divider text="ou" />

        <Button
          width="100%"
          bgColor="--gray-200"
          color="--gray-700"
          text="Criar conta"
        />
      </div>
    </>
  );
};

export default Login;
