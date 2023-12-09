import "./Avatar.css";
import { useTheme } from "../../context/ColorProvider";

export default function Avatar({ src, size = "30px", btnRef, onClick, inNav }) {
  // let newSrc =
  //   src ??
  //   "https://media.discordapp.net/attachments/934145502252003410/1129211702546796554/Screen_Shot_2023-07-13_at_8.43.39_PM.png?width=1192&height=1068";
  const { theme } = useTheme();

  if (!src) {
    let pfpColor = "rgba(175, 175, 175, 0.5)";
    if (inNav) {
      if (theme === "light") pfpColor = "#5271ff";
      else pfpColor = "#ffffff";
    } else {
      if (theme === "light") pfpColor = "rgba(175, 175, 175, 0.5)";
      else pfpColor = "#ffffff";
    }
    return (
      <i
        className="fa-solid fa-user avatar"
        style={{
          backgroundColor: pfpColor,
          width: size,
          height: size,
          color: theme === "light" ? "#ffffff" : "#25284a",
        }}
        ref={btnRef}
        onClick={onClick}
      ></i>
    );
  }
  return (
    <img
      className="avatar"
      src={src}
      style={{ width: size, height: size }}
      ref={btnRef}
      onClick={onClick}
    />
  );
}
