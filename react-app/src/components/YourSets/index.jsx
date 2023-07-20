import { useDispatch } from "react-redux";
import useSession from "../../hooks/useSession";
import { authenticate } from "../../store/session";
import { useEffect } from "react";
import Scrollable from "../Scrollable";
import { useNavigate } from "react-router-dom";
import NavSearch from "../Navigation/NavSearch";
import "./YourSets.css";

export default function YourSets() {
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const user = useSession();

  useEffect(() => {
    dispatch(authenticate());
  }, [dispatch]);

  useEffect(() => {
    if (!user) {
      navigate("/logIn", { state: window.location.pathname });
    }
  }, []);

  if (!user) return;

  return (
    <div className="YourSets">
      <div className="YourSets-header">
        <div className="YourSets-header-title">Your Sets</div>
        <NavSearch placeholder="Search your sets" />
      </div>
      {user.Sets.length ? (
        <Scrollable arr={user.Sets} isSet={true} />
      ) : (
        <div> You currently have no sets </div>
      )}
    </div>
  );
}
