import "./Navigation.css";

export default function NavSearch({ placeholder }) {
  return (
    <div className="Nav-search">
      <i className="fa-solid fa-magnifying-glass search"></i>
      <input type="text" placeholder={placeholder} />
    </div>
  );
}
