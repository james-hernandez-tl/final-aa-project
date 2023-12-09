import ClipLoader from "react-spinners/ClipLoader";
import { useTheme } from "../../context/ColorProvider";
import React from "react";
import "./LoadingScreen.css";

export default function LoadingScreen() {
  const { theme } = useTheme();
  return (
    <div className="LoadingScreen">
      <ClipLoader color={theme === "light" ? "black" : "white"} size={100} />
    </div>
  );
}
