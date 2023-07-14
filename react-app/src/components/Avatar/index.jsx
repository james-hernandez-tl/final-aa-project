import "./Avatar.css";

export default function Avatar({ src, size = "30px", btnRef, onClick }) {
  let newSrc =
    src ??
    "https://media.discordapp.net/attachments/934145502252003410/1129211702546796554/Screen_Shot_2023-07-13_at_8.43.39_PM.png?width=1192&height=1068";
  return (
    <img
      className="avatar"
      src={newSrc}
      style={{ width: size, height: size }}
      ref={btnRef}
      onClick={onClick}
    />
  );
}
