import styles from "./Divider.module.css";
import { DividerProps } from "./interfaces/DividerProps";

const Divider = ({ text }: DividerProps) => {
  return (
    <div className={styles.divider}>
      <span className={styles.line}></span>
      {text && <span className={styles.text}>{text}</span>}
      <span className={styles.line}></span>
    </div>
  );
};

export default Divider;
