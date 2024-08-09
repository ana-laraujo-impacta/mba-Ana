import Logo from "../../assets/logo.svg";
import styles from "./Footer.module.css";

interface footerDataProps {
  title: string;
  firstText: string;
  secondText: string;
  link: string;
}

export const footerData: footerDataProps[] = [
  {
    title: "Conexão Pet",
    firstText: "Como funciona",
    secondText: "Quem somos",
    link: "#how-it-works",
  },
  {
    title: "Central de ajuda",
    firstText: "Ajuda",
    secondText: "Termos de uso",
    // Política de privacidade
    link: "#pet-sitter",
  },
  {
    title: "Serviços",
    firstText: "Pet Sitting",
    secondText: "Pet Supply",
    // Pet Vet Free
    link: "#pet-sitter",
  },
];

const Footer = () => {
  return (
    <footer>
      <div className={styles.logoFooter}>
        <img src={Logo} alt="" />
        <div className={styles.copyright}>
          <p>© 2024 - Conexão Pet</p>
        </div>
      </div>

      <div className={styles.footerLinks}>
        {footerData.map((item) => (
          <div key={item.title}>
            <h3>{item.title}</h3>
            <ul>
              <li>
                <a href={item.link}>{item.firstText}</a>
              </li>
              <li>
                <a href={item.link}>{item.secondText}</a>
              </li>
            </ul>
          </div>
        ))}
      </div>
    </footer>
  );
};

export default Footer;
