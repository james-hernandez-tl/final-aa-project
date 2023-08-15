import { useState, useEffect } from "react";
import { login } from "../../store/session";
import { useDispatch } from "react-redux";
import { useNavigate, useLocation } from "react-router-dom";
import useSession from "../../hooks/useSession";
import "./LoginPage.css";

export default function LoginPage() {
  const user = useSession();
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

  useEffect(() => {
    if (user) {
      navigate(state);
    }
  }, []);

  return (
    <div className="LoginPage">
      <div className="Login-div">
        <div className="LoginPage-header">Log In Page</div>
        <div className={`LoginPage-input-wrapper ${usernameError}`}>
          <input
            type="text"
            value={usernameError ? "User doesn't exist" : username}
            onChange={(e) => {
              setUsername(e.target.value);
              setUsernameError(null);
            }}
            onClick={() => {
              setPasswordError(null);
              setUsernameError(null);
            }}
            className={`LoginPage-inputs ${required}`}
            placeholder={required ?? "username or email"}
          />
        </div>
        <div className={`LoginPage-input-wrapper ${passwordError}`}>
          <input
            type="text"
            value={passwordError ? "wrong password" : password}
            onChange={(e) => {
              setPassword(e.target.value);
              setPasswordError(null);
            }}
            onClick={() => setPasswordError(null)}
            className={`LoginPage-inputs ${required}`}
            placeholder={required ?? "password"}
          />
        </div>
        <div>
          <button className="LoginPage-button" onClick={LogInClicker}>
            Log In
          </button>
        </div>
        <div className="LoginPage-signupbtn">
          <div onClick={signupClicker}>
            {" "}
            dont have an account? sign up instead
          </div>
          <div
            onClick={async () => {
              await dispatch(login("Demo", "password"));
              navigate(state);
            }}
          >
            or try as a Demo user!
          </div>
        </div>
      </div>
    </div>
  );
}
