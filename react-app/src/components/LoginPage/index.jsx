import { useState } from "react";
import { login } from "../../store/session";
import { useDispatch } from "react-redux";
import { useNavigate, useLocation } from "react-router-dom";

export default function LoginPage() {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const { state } = useLocation();
  const LogInClicker = () => {
    dispatch(login(username, password));
    navigate(state);
  };

  return (
    <div>
      <input
        type="text"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
      />
      <input
        type="text"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
      />
      <button onClick={LogInClicker}>LogIn</button>
    </div>
  );
}
