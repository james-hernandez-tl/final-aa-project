import { useState } from "react";
import { signUp } from "../../store/session";
import { useDispatch } from "react-redux";
import { useNavigate, useLocation } from "react-router-dom";
import "./SignUpPage.css";

export default function SignUpPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [confirmPassword, setConfirmPassword] = useState("");
  const [passwordError, setPasswordError] = useState(null);
  const [usernameError, setUsernameError] = useState(null);
  const [emailError, setEmailError] = useState(null);
  const [confirmPasswordError, setConfirmPasswordError] = useState(null);

  const [required, setRequired] = useState(null);
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const { state } = useLocation();
  const SignUpClicker = async () => {
    if (!username || !password || !email || !confirmPassword) {
      setRequired("Required");
      return null;
    }
    if (password !== confirmPassword) {
      setConfirmPasswordError("formError");
      return null;
    }
    const errors = await dispatch(signUp(username, email, password));
    if (errors) {
      setUsernameError(errors?.username);
      setPasswordError(errors?.password);
      setEmailError(errors?.email);
    }
    if (!errors) navigate(state);
  };

  const usernameClicker = () => {
    if (usernameError) {
      setUsernameError(null);
    }
  };

  const emailClicker = () => {
    if (emailError) {
      setEmailError(null);
    }
  };

  const passwordClicker = () => {
    if (passwordError) {
      setPasswordError(null);
    }
  };

  const loginClicker = () => {
    navigate("/login", { state: state });
  };

  return (
    <div className="SignUpPage">
      <div className="SignUp-div">
        <div className="SignUpPage-header">Sign Up Page</div>
        <div
          className={`SignUpPage-input-wrapper ${
            usernameError ? "formError" : ""
          }`}
          onClick={usernameClicker}
        >
          <input
            type="text"
            value={usernameError ?? username}
            onChange={(e) => {
              setUsername(e.target.value);
              setUsernameError(null);
            }}
            className={`SignUpPage-inputs ${required}`}
            placeholder={required ?? "username"}
          />
        </div>
        <div
          className={`SignUpPage-input-wrapper ${
            emailError ? "formError" : ""
          }`}
          onClick={emailClicker}
        >
          <input
            type="text"
            value={emailError ?? email}
            onChange={(e) => {
              setEmail(e.target.value);
              setEmailError(null);
            }}
            className={`SignUpPage-inputs ${required}`}
            placeholder={required ?? "example@email.com"}
          />
        </div>
        <div
          className={`SignUpPage-input-wrapper ${
            passwordError ? "formError" : ""
          }`}
          onClick={passwordClicker}
        >
          <input
            type="text"
            value={passwordError ?? password}
            onChange={(e) => {
              setPassword(e.target.value);
              setPasswordError(null);
            }}
            className={`SignUpPage-inputs ${required}`}
            placeholder={required ?? "password123"}
          />
        </div>
        <div className={`SignUpPage-input-wrapper ${confirmPasswordError}`}>
          <input
            type="text"
            value={
              confirmPasswordError ? "doesn't match password" : confirmPassword
            }
            onChange={(e) => {
              setConfirmPassword(e.target.value);
              if (confirmPasswordError) setConfirmPasswordError(null);
            }}
            onClick={() => {
              if (confirmPasswordError) setConfirmPasswordError(null);
            }}
            className={`SignUpPage-inputs ${required}`}
            placeholder={required ?? "confirm password"}
          />
        </div>
        <div>
          <button className="SignUpPage-button" onClick={SignUpClicker}>
            sign up
          </button>
        </div>
        <div className="SignUpPage-login-btn" onClick={loginClicker}>
          already have an account? log in
        </div>
      </div>
    </div>
  );
}
