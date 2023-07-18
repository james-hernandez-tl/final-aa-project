import { useDispatch } from "react-redux";
import useSession from "../../hooks/useSession";
import { authenticate } from "../../store/session";
import { useEffect } from "react";
import Scrollable from "../Scrollable";
import "./YourSets.css";

export default function YourSets() {
  const dispatch = useDispatch();
  const user = useSession();

  useEffect(() => {
    dispatch(authenticate());
  }, [dispatch]);

  if (!user) return;

  return (
    <div className="YourSets">
      <div className="YourSets-header">
        <div className="YourSets-header-title">Your Sets</div>
        <div>
          <input type="text" />
        </div>
      </div>
      <Scrollable arr={user.Sets} isSet={true} />
    </div>
  );
}
