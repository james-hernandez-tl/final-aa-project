import { NavLink, Link } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import "./Navigation.css";
import Avatar from "../Avatar";
import { useMenu } from "../Menu";
import { Menu, MenuItem } from "../Menu";
import { useNavigate } from "react-router-dom";
import { logout } from "../../store/session";
export default function Profile({ sessionUser }) {
  const navigation = useNavigate();
  const dispatch = useDispatch();
  const { btnRef, hideMenu, toggleMenu, show, menuRef } = useMenu();
  return (
    <>
      <Avatar
        src={sessionUser?.image}
        size={"35px"}
        btnRef={btnRef}
        onClick={toggleMenu}
      />
      <Menu menuRef={menuRef} isOpen={show}>
        {!sessionUser && (
          <MenuItem
            text="LogIn"
            onClick={() => {
              navigation("/logIn", { state: window.location.pathname });
              hideMenu();
            }}
          />
        )}
        {sessionUser && (
          <MenuItem text="Logout" onClick={() => dispatch(logout())} />
        )}
      </Menu>

      <NavLink to={"/"}>KnowVerse</NavLink>
      <NavLink to={"/sets"}>Sets</NavLink>
      <NavLink to={"/folders"}>Folders</NavLink>
      <NavLink to={"/groups"}>Groups</NavLink>
    </>
  );
}
