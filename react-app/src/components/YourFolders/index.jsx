import { useDispatch } from "react-redux";
import useSession from "../../hooks/useSession";
import Scrollable from "../Scrollable";
import { authenticate } from "../../store/session";
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import NavSearch from "../Navigation/NavSearch";
import "./YourFolder.css";

export default function YourFolders() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const user = useSession();
  const [searchFolders, setSearchFolders] = useState();

  useEffect(() => {
    dispatch(authenticate());
  }, [dispatch]);

  useEffect(() => {
    if (!user) {
      navigate("/", { state: window.location.pathname });
    }
  }, [navigate, user]);

  const filterFolders = (arr) => {
    if (!searchFolders) return arr;
    return arr
      .filter(
        (folder) =>
          folder.name.toLowerCase().includes(searchFolders.toLowerCase()) ||
          folder.description.toLowerCase().includes(searchFolders.toLowerCase())
      )
      .sort((a, b) => {
        if (
          a.name.toLowerCase().includes(searchFolders.toLowerCase()) &&
          !b.name.toLowerCase().includes(searchFolders.toLowerCase())
        )
          return -1;
        if (
          b.name.toLowerCase().includes(searchFolders.toLowerCase()) &&
          !a.name.toLowerCase().includes(searchFolders.toLowerCase())
        )
          return 1;
        else return 1;
      });
  };

  if (!user) return null;

  return (
    <div className="YourFolders">
      <div className="YourFolders-header">
        <div className="YourFolders-header-title">Your Folders</div>
        <NavSearch
          placeholder="Search your folders"
          setUserSearch={setSearchFolders}
        />
      </div>
      {user.Folders.length ? (
        <Scrollable
          arr={filterFolders(user.Folders)}
          isSet={false}
          searchTerm={searchFolders}
        />
      ) : (
        <div> You currently have no folders </div>
      )}
    </div>
  );
}
