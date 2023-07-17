import { useDispatch } from "react-redux";
import useSession from "../../hooks/useSession";
import Scrollable from "../Scrollable";
import { authenticate } from "../../store/session";
import { useEffect } from "react";

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
        <div>Your Folders</div>
        <div>
          <input type="text" />
        </div>
      </div>
      <Scrollable arr={user.Folders.slice(0, 4)} isSet={false} />
    </div>
  );
}
