import Footer from "../../components/Footer/Footer";
import Header from "../../components/Header/Header";
import SearchBar from "../../components/SearchBar/SearchBar";
import ServiceCard from "../../components/ServiceCard/ServiceCard";
import HowItWorks from "./HowItWorks";
import Section from "./Section";
import { servicesData } from "./servicesData";
import styles from "./styles.module.css";

const Home = () => {
  return (
    <div className="App">
      <Header showArrow={false} showLinksAndButtons={true} showLogo={true} />
      <main>
        <section className={styles.hero}>
          <div className={styles.topTexts}>
            <h1>
              Cuidamos do seu pet<br></br>quando você não pode.
            </h1>
            <p>
              Encontre e conecte-se com voluntários de confiança na sua região,
              <br></br>
              garantindo bem-estar e cuidado com seu Pet.
            </p>
          </div>
          <SearchBar />
        </section>
        <section className={styles.services}>
          {servicesData.map((service) => (
            <ServiceCard
              key={service.title}
              title={service.title}
              description={service.description}
              linkText={service.linkText}
              image={service.image}
              link={service.link}
            />
          ))}
        </section>
        <Section />
        <HowItWorks />
      </main>
      <Footer />
    </div>
  );
};

export default Home;
