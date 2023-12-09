import useSession from "../../hooks/useSession";
import { useEffect, useState } from "react";
import Scrollable from "../Scrollable";
import { useNavigate } from "react-router-dom";
import NavSearch from "../Navigation/NavSearch";
import "./YourSets.css";

export default function YourSets() {
  const navigate = useNavigate();
  const user = useSession();
  const [searchSets, setSearchSets] = useState("");

  useEffect(() => {
    if (!user) {
      navigate("/", { state: window.location.pathname });
    }
  }, [navigate, user]);

  const filterSets = (arr) => {
    if (!searchSets) return arr;
    return arr
      .filter(
        (set) =>
          set.name.toLowerCase().includes(searchSets.toLowerCase()) ||
          set.description.toLowerCase().includes(searchSets.toLowerCase())
      )
      .sort((a, b) => {
        if (
          a.name.toLowerCase().includes(searchSets.toLowerCase()) &&
          !b.name.toLowerCase().includes(searchSets.toLowerCase())
        )
          return -1;
        if (
          b.name.toLowerCase().includes(searchSets.toLowerCase()) &&
          !a.name.toLowerCase().includes(searchSets.toLowerCase())
        )
          return 1;
        else return 1;
      });
  };

  if (!user) return;

  return (
    <div className="YourSets">
      <div className="YourSets-header">
        <div className="YourSets-header-title">Your Sets</div>
        <NavSearch
          placeholder="Search your sets"
          setUserSearch={setSearchSets}
        />
      </div>
      {user.Sets.length ? (
        <Scrollable
          arr={filterSets(user.Sets)}
          isSet={true}
          searchTerm={searchSets}
        />
      ) : (
        <div> You currently have no sets </div>
      )}
    </div>
  );
}
