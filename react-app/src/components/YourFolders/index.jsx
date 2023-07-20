import { useDispatch } from "react-redux";
import useSession from "../../hooks/useSession";
import Scrollable from "../Scrollable";
import { authenticate } from "../../store/session";
import { useEffect } from "react";
import { useNavigate } from "react-router-dom";
import NavSearch from "../Navigation/NavSearch";
import "./YourFolder.css";

export default function YourFolders() {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const user = useSession();

  useEffect(() => {
    dispatch(authenticate());
  }, [dispatch]);

  useEffect(() => {
    if (!user) {
      navigate("/logIn", { state: window.location.pathname });
    }
  }, []);

  if (!user) return null;

  return (
    <div className="YourFolders">
      <div className="YourFolders-header">
        <div className="YourFolders-header-title">Your Folders</div>
        <NavSearch placeholder="Search your folders" />
      </div>
      {user.Folders.length ? (
        <Scrollable arr={user.Folders} isSet={false} />
      ) : (
        <div> You currently have no folders </div>
      )}
    </div>
  );
}
