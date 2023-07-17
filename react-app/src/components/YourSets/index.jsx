import { useDispatch } from "react-redux";
import useSession from "../../hooks/useSession";
import { authenticate } from "../../store/session";
import { useEffect } from "react";
import Scrollable from "../Scrollable";

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
        <div>Your Sets</div>
        <div>
          <input type="text" />
        </div>
      </div>
      <Scrollable arr={user.Sets} isSet={true} />
    </div>
  );
}
