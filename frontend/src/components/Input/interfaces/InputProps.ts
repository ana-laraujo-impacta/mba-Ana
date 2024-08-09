export interface InputProps {
  bgColor?: string;
  width?: string;
  color?: string;
  label?: string;
  placeholder: string;
  type: string;
  value?: string;
  onChange?: (e: React.ChangeEvent<HTMLInputElement>) => void;
  required?: boolean;
}
