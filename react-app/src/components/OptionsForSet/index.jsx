import { useNavigate } from "react-router-dom";
import "./OptionsForSet.css";

export default function OptionsForSet({ setId }) {
  const navigate = useNavigate();
  return (
    <div className="OptionsForSet">
      <div
        className="OptionsForSet-option"
        onClick={() => navigate(`/chat/${setId}`)}
      >
        <div className="OptionsForSet-option-icon">
          <i className="fa-solid fa-wand-magic-sparkles"></i>
        </div>
        <div className="OptionsForSet-option-text">Q-Chat</div>
      </div>
      <div className="OptionsForSet-option"></div>
      <div className="OptionsForSet-option"></div>
    </div>
  );
}
