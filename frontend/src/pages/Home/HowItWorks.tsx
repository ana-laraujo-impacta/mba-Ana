import GirlDog from "../../assets/notes-young-woman-training-her-dog 1.svg";
import { howItWorksData } from "./servicesData";
import styles from "./styles.module.css";

const HowItWorks = () => {
  return (
    <section id="how-it-works" className={styles.howItWorks}>
      <div className={styles.firstColumn}>
        <img src={GirlDog} alt="" />
      </div>
      <div className={styles.secondColumn}>
        <h2>Como funciona</h2>

        {howItWorksData.map((item) => (
          <div key={item.title}>
            <div className={styles.firstRow}>
              <img src={item.icon} alt="" />
              <h3>{item.title}</h3>
            </div>
            <p>{item.description}</p>
          </div>
        ))}
      </div>
    </section>
  );
};

export default HowItWorks;
