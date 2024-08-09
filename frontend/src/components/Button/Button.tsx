import React from "react";
import { ButtonProps } from "./interfaces/ButtonProps";
import styles from "./Button.module.css";

const Button = ({
  bgColor,
  width,
  color,
  text,
  children,
  onClick,
  type,
}: ButtonProps) => {
  const dynamicStyles = {
    backgroundColor: `var(${bgColor})`,
    minWidth: width || "auto",
    color: `var(${color})`,
  } as React.CSSProperties;

  return (
    <button
      className={styles.button}
      style={dynamicStyles}
      type={type}
      onClick={onClick}
    >
      {text}
      {children}
    </button>
  );
};

export default Button;
