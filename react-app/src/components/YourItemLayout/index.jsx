import { useNavigate } from "react-router-dom";

export default function YourItemLayout({ item, isSet }) {
  const navigate = useNavigate();
  let itemClicker = () => {
    if (isSet) {
      navigate(`/sets/${item.id}`);
    } else {
      navigate(`/folders/${item.id}`);
    }
  };

  return <div onClick={itemClicker}>{item.name}</div>;
}
