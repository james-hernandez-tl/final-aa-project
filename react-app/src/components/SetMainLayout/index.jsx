import "./SetMainLayout.css";
import Avatar from "../Avatar";
import { useNavigate } from "react-router-dom";

export default function SetMainLayout({ set, inSearch, setPreviewSet }) {
  const navigate = useNavigate();
  const setClicker = () => {
    navigate(`/sets/${set.id}`);
  };
  return (
    <div className="SetMainLayout" onClick={setClicker}>
      {inSearch && (
        <div>
          <button className="SetMainLayout-studiers">
            10 studiers recently
          </button>
        </div>
      )}
      <div className="SetMainLayout-name">{set.name}</div>
      <div className="SetMainLayout-addons">
        <div>
          <span className="SetMainLayout-addons-numCards">
            {Object.values(set.Cards).length} cards
          </span>
        </div>
        <div className="SetMainLayout-star-wrapper">
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
          <div className="SetMainLayout-preview-wrapper">
            <button
              className="SetMainLayout-preview"
              onClick={(e) => {
                e.preventDefault();
                e.stopPropagation();
                setPreviewSet(set);
              }}
            >
              Preview
            </button>
          </div>
        )}
      </div>
    </div>
  );
}
