import { useNavigate } from "react-router-dom";
import "./YourItemLayout.css";

export default function YourItemLayout({ item, isSet }) {
  const navigate = useNavigate();
  let itemClicker = () => {
    if (isSet) {
      navigate(`/sets/${item.id}`);
    } else {
      navigate(`/folders/${item.id}`);
    }
  };

  return (
    <div className="YourItemLayout" onClick={itemClicker}>
      <div className="YourItemLayout-name">{item.name}</div>
      <div>
        <div className="YourItemLayout-terms">
          {isSet ? item.NumCards + " terms" : item.NumSets + " sets"}
        </div>
        <div></div>
      </div>
    </div>
  );
}
