import "./SetMainLayout.css";
import Avatar from "../Avatar";

export default function SetMainLayout({ set, inSearch }) {
  return (
    <div className="SetMainLayout">
      <div className="SetMainLayout-name">{set.name}</div>
      <div className="SetMainLayout-addons">
        <div>{set.Cards.length} Terms</div>
        <div>
          <i className="fa-solid fa-star"></i>
          {set.Rating}({set.NumRatings})
        </div>
      </div>
      <div className="SetMainLayout-footer">
        <div>
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
