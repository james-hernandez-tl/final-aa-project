import { useState } from "react";
import { login } from "../../store/session";
import { useDispatch } from "react-redux";
import { useNavigate, useLocation } from "react-router-dom";
import "./SignUpPage.css";

export default function SignUpPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [passwordError, setPasswordError] = useState(null);
  const [usernameError, setUsernameError] = useState(null);
  const [required, setRequired] = useState(null);
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const { state } = useLocation();
  const LogInClicker = async () => {
    if (!username || !password) {
      setRequired("Required");
      return null;
    }
    const errors = await dispatch(login(username, password));
    if (errors?.password) {
      setPasswordError("passwordError");
    }
    if (errors?.username) {
      setUsernameError("usernameError");
    }
    if (!errors) navigate(state);
  };

  return (
    <div className="SignUpPage">
      <div className="SignUp-div">
        <div className="SignUpPage-header">Sign Up Page</div>
        <div className={`SignUpPage-input-wrapper ${usernameError}`}>
          <input
            type="text"
            value={username}
            onChange={(e) => {
              setUsername(e.target.value);
              setUsernameError(null);
            }}
            className={`SignUpPage-inputs ${required}`}
            placeholder={required ?? "Username"}
          />
        </div>
        <div className={`SignUpPage-input-wrapper ${usernameError}`}>
          <input
            type="text"
            value={username}
            onChange={(e) => {
              setUsername(e.target.value);
              setUsernameError(null);
            }}
            className={`SignUpPage-inputs ${required}`}
            placeholder={required ?? "Email"}
          />
        </div>
        <div className={`SignUpPage-input-wrapper ${usernameError}`}>
          <input
            type="text"
            value={username}
            onChange={(e) => {
              setUsername(e.target.value);
              setUsernameError(null);
            }}
            className={`SignUpPage-inputs ${required}`}
            placeholder={required ?? "Password"}
          />
        </div>
        <div className={`SignUpPage-input-wrapper ${passwordError}`}>
          <input
            type="text"
            value={password}
            onChange={(e) => {
              setPassword(e.target.value);
              setPasswordError(null);
            }}
            className={`SignUpPage-inputs ${required}`}
            placeholder={required ?? "Confirm Password"}
          />
        </div>
        <div>
          <button className="SignUpPage-button" onClick={LogInClicker}>
            Sign Up
          </button>
        </div>
      </div>
    </div>
  );
}
