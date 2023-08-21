import "./Navigation.css";
import { useIsSearching } from "../../context/Search";

export default function NavSearch({ placeholder, cb, setUserSearch }) {
  const { isSearching, setIsSearching } = useIsSearching();
  return (
    <div className="Nav-search">
      <i className="fa-solid fa-magnifying-glass search"></i>
      <input
        type="text"
        placeholder={placeholder}
        onChange={(e) => setUserSearch(e.target.value)}
        onKeyPress={(e) => {
          if (e.key === "Enter" && cb) {
            cb();
            setIsSearching(true);
          }
        }}
      />
    </div>
  );
}
