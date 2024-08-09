import { useState } from "react";
import { useMutation, UseMutationResult } from "@tanstack/react-query";
import { useNavigate } from "react-router-dom";
import { changePassword, ChangePasswordParams } from "../../services/auth";
import Button from "../../components/Button/Button";
import Header from "../../components/Header/Header";
import Input from "../../components/Input/Input";
import Divider from "../../components/Divider/Divider";
import Logo from "../../assets/logo.svg";
import styles from "./ChangePassword.module.css";

const ChangePassword = () => {
  const [email, setEmail] = useState("");
  const [currentPassword, setCurrentPassword] = useState("");
  const [newPassword, setNewPassword] = useState("");

  const navigate = useNavigate();

  const mutation: UseMutationResult<any, any, ChangePasswordParams, unknown> =
    useMutation({
      mutationFn: changePassword,
      onSuccess: (data) => {
        alert("Senha alterada com sucesso!");
        console.log("Password change successful:", data);
        navigate("/login"); // Redireciona para a tela de login após a alteração da senha
      },
      onError: (error: any) => {
        console.error("Erro ao alterar a senha:", error);
      },
    });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    mutation.mutate({ email, password: currentPassword, newPassword: newPassword });
  };

  return (
    <>
      <Header showArrow={true} />

      <div className={styles.container}>
        <img className={styles.logo} src={Logo} alt="Conexão Pet" />
        <h2>Esqueci minha senha</h2>
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
            label="Senha Atual"
            placeholder="Sua senha atual"
            value={currentPassword}
            onChange={(e) => setCurrentPassword(e.target.value)}
            required
          />
          <Input
            type="password"
            label="Nova Senha"
            placeholder="Sua nova senha"
            value={newPassword}
            onChange={(e) => setNewPassword(e.target.value)}
            required
          />
          <Button
            bgColor="--pink-500"
            color="--white"
            text="Alterar minha senha"
          />
        </form>

        {mutation.isError && (
          <p>
            Error:{" "}
            {mutation.error instanceof Error
              ? mutation.error.message
              : "Unknown error"}
          </p>
        )}
        {mutation.isSuccess && <p>Senha alterada com sucesso!</p>}

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

export default ChangePassword;
