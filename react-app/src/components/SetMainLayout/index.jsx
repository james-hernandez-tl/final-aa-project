import "./SetMainLayout.css";
import Avatar from "../Avatar";
import { useNavigate } from "react-router-dom";

export default function SetMainLayout({ set, inSearch }) {
  const navigate = useNavigate();
  const setClicker = () => {
    navigate(`/sets/${set.id}`);
  };
  return (
    <div className="SetMainLayout" onClick={setClicker}>
      <div className="SetMainLayout-name">{set.name}</div>
      <div className="SetMainLayout-addons">
        <div>{set.Cards.length} Terms</div>
        <div>
          <i className="fa-regular fa-star"></i>
          {`${set.Rating} (${set.NumRatings})`}
        </div>
      </div>
      <div className="SetMainLayout-footer">
        <div className="SetMainLayout-footer-pfp">
          <Avatar src={set.User.image} />
        </div>
        <div className="SetMainLayout-footer-username">{set.User.username}</div>
        {inSearch && (
          <div>
            <button>preview</button>
          </div>
        )}
      </div>
    </div>
  );
}
