import styles from "./ServiceCard.module.css";
import { ServiceCardProps } from "./interfaces/ServiceCardProps";

const ServiceCard = ({
  title,
  description,
  linkText,
  image,
  link,
}: ServiceCardProps) => (
  <div className={styles.serviceCard}>
    <img src={image} alt={title} className={styles.image} />
    <h2 className={styles.title}>{title}</h2>
    <p className={styles.description}>{description}</p>
    <a href={link} className={styles.link}>
      {linkText}
    </a>
  </div>
);

export default ServiceCard;
