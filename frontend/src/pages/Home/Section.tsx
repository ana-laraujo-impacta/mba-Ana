import { infoData } from "./servicesData";
import GirlCat from "../../assets/notes-girl-holding-a-cat 1.svg";
import styles from "./styles.module.css";

const Section = () => {
  return (
    <section className={styles.infoSection}>
      <img src={GirlCat} alt="Figura de uma menina e um gato" />
      <h2>Facilitando Cuidados para o seu Pet</h2>
      <div className={styles.infoCards}>
        {infoData.map((info) => (
          <div key={info.title} className={styles.infoCard}>
            <img src={info.icon} alt="" />
            <h3>{info.title}</h3>
            <p>{info.description}</p>
          </div>
        ))}
      </div>
    </section>
  );
};

export default Section;
