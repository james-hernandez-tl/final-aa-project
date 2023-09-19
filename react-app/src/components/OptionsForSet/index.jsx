import { useNavigate } from "react-router-dom";
import "./OptionsForSet.css";

export default function OptionsForSet({ setId }) {
  const navigate = useNavigate();
  return (
    <div className="OptionsForSet">
      <div
        className="OptionsForSet-option"
        onClick={() => navigate(`/chat/${setId}`)}
        onMouseEnter={() => {
          document
            .getElementById("OptionsForSet-option-hover")
            .classList.add("OptionsForSet-option-hover");
        }}
        onMouseLeave={() => {
          document
            .getElementById("OptionsForSet-option-hover")
            .classList.remove("OptionsForSet-option-hover");
        }}
      >
        <div className="OptionsForSet-option-icon">
          <i className="fa-solid fa-wand-magic-sparkles"></i>
        </div>
        <div className="OptionsForSet-option-text">Q-Chat</div>
        <div id="OptionsForSet-option-hover"></div>
      </div>
      <div className="OptionsForSet-option"></div>
      <div className="OptionsForSet-option"></div>
    </div>
  );
}
