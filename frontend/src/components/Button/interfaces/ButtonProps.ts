import { MouseEventHandler, ReactNode } from "react";

export interface ButtonProps {
  bgColor?: string;
  width?: string;
  color?: string;
  text?: string;
  children?: ReactNode;
  onClick?: MouseEventHandler<HTMLButtonElement>;
  type?: "reset" | "submit" | "button" | undefined;
}
