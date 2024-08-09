import { HeaderProps } from "./interfaces/HeaderProps";
import styles from "./Header.module.css";
import iconArrowBack from "../../assets/arrow_back.svg";
import Button from "../Button/Button";
import logo from "../../assets/logo.svg";
import { useLogin } from "../../utils/goToLogin";
import { useBack } from "../../utils/handleBack";

const Header = ({
  showArrow = false,
  showLinksAndButtons = false,
  showLogo = false,
}: HeaderProps) => {
  const { goToLogin } = useLogin();
  const { handleBack } = useBack();

  return (
    <header className={styles.header}>
      <div className={styles.logoContainer}>
        {showArrow && (
          <button onClick={handleBack}>
            <img src={iconArrowBack} alt="Voltar" className={styles.icon} />
          </button>
        )}

        {showLogo && (
          <img src={logo} alt="Conexão Pet" className={styles.logo} />
        )}
      </div>
      {showLinksAndButtons && (
        <nav className={styles.nav}>
          <div className={styles.links}>
            <a href="#how-it-works" className={styles.link}>
              Como funciona
            </a>
            <a href="#ajuda" className={styles.link}>
              Ajuda
            </a>
          </div>
          <div className={styles.buttons}>
            <Button
              bgColor="--gray-200"
              color="--gray-700"
              width="124px"
              text="Entrar"
              onClick={goToLogin}
            />
            <Button
              bgColor="--pink-500"
              color="--white"
              width="124px"
              text="Criar conta"
            />
          </div>
        </nav>
      )}
    </header>
  );
};

export default Header;
