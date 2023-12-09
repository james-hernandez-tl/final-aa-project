import React from "react";
import { useTheme } from "../../context/ColorProvider";

export default function ChangeTheme() {
  const { theme, setTheme, toggleTheme } = useTheme();

  return <div onClick={toggleTheme}>toggleTheme</div>;
}
