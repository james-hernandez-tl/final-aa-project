import { useDispatch } from "react-redux";
import useSession from "../../hooks/useSession";
import Scrollable from "../Scrollable";

export default function YourFolders() {
  const dispatch = useDispatch();
  const user = useSession();

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
