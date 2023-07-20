import { useState } from "react";
import { login } from "../../store/session";
import { useDispatch } from "react-redux";
import { useNavigate, useLocation } from "react-router-dom";
import "./LoginPage.css";

export default function LoginPage() {
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

  const signupClicker = () => {
    navigate("/signup", { state: state });
  };

  return (
    <div className="LoginPage">
      <div className="Login-div">
        <div className="LoginPage-header">Log In Page</div>
        <div className={`LoginPage-input-wrapper ${usernameError}`}>
          <input
            type="text"
            value={username}
            onChange={(e) => {
              setUsername(e.target.value);
              setUsernameError(null);
            }}
            className={`LoginPage-inputs ${required}`}
            placeholder={required ?? "username or email"}
          />
        </div>
        <div className={`LoginPage-input-wrapper ${passwordError}`}>
          <input
            type="text"
            value={password}
            onChange={(e) => {
              setPassword(e.target.value);
              setPasswordError(null);
            }}
            className={`LoginPage-inputs ${required}`}
            placeholder={required ?? "password"}
          />
        </div>
        <div>
          <button className="LoginPage-button" onClick={LogInClicker}>
            Log In
          </button>
        </div>
        <div className="LoginPage-signupbtn" onClick={signupClicker}>
          dont have an account? sign up instead
        </div>
      </div>
    </div>
  );
}
