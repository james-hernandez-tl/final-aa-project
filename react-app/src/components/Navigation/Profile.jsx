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
            icon={<i className="fa-solid fa-power-off"></i>}
          />
        )}
        {sessionUser && (
          <MenuItem
            text="Logout"
            onClick={() => {
              dispatch(logout());
              navigation("/");
            }}
            icon={<i className="fa-solid fa-power-off"></i>}
          />
        )}
      </Menu>

      <NavLink
        exact={"true"}
        to={"/"}
        className="Navlink-unactive"
        activeclassname="active"
      >
        KnowVerse
      </NavLink>
      <NavLink
        to={"/sets"}
        className="Navlink-unactive"
        activeclassname="active"
      >
        Sets
      </NavLink>
      <NavLink
        to={"/folders"}
        className="Navlink-unactive"
        activeclassname="active"
      >
        Folders
      </NavLink>
      <NavLink
        to={"/groups"}
        className="Navlink-unactive"
        activeclassname="active"
      >
        Groups
      </NavLink>
    </>
  );
}
