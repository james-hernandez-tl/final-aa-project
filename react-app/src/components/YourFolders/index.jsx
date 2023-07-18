import { useDispatch } from "react-redux";
import useSession from "../../hooks/useSession";
import Scrollable from "../Scrollable";
import { authenticate } from "../../store/session";
import { useEffect } from "react";
import "./YourFolder.css";

export default function YourFolders() {
  const dispatch = useDispatch();
  const user = useSession();

  useEffect(() => {
    dispatch(authenticate());
  }, [dispatch]);

  if (!user) return;

  return (
    <div className="YourFolders">
      <div className="YourFolders-header">
        <div className="YourFolders-header-title">Your Folders</div>
        <div>
          <input type="text" />
        </div>
      </div>
      <Scrollable arr={user.Folders} isSet={false} />
    </div>
  );
}
