import { InputProps } from "./interfaces/InputProps";
import styles from "./Input.module.css";

const Input = ({
  bgColor,
  width,
  color,
  label,
  placeholder,
  type,
  value,
  onChange,
  required,
}: InputProps) => {
  const dynamicStyles = {
    backgroundColor: `var(${bgColor})`,
    width: width || "100%",
    color: `var(${color})`,
  } as React.CSSProperties;

  return (
    <div className={styles.inputContainer}>
      <label className={styles.label} style={{ color: dynamicStyles.color }}>
        {label}
      </label>
      <input
        type={type}
        className={styles.input}
        style={dynamicStyles}
        placeholder={placeholder}
        value={value}
        onChange={onChange}
        required={required}
      />
    </div>
  );
};

export default Input;
