import React from "react";
import { useSelector, useDispatch } from "react-redux";
import "./Navigation.css";
import Avatar from "../Avatar";
import { useMenu } from "../Menu";
import { Menu, MenuItem } from "../Menu";
import { useNavigate } from "react-router-dom";
import { logout } from "../../store/session";
import Profile from "./Profile";
import PlusIcon from "./PlusIcon";
import NavSearch from "./NavSearch";
import { useState } from "react";
import { useTheme } from "../../context/ColorProvider";

function Navigation({ isLoaded }) {
  const { theme, setTheme, toggleTheme } = useTheme();
  const sessionUser = useSelector((state) => state.session.user);
  const [userSearch, setUserSearch] = useState("");
  const navigate = useNavigate();
  const { btnRef, hideMenu, toggleMenu, show, menuRef } = useMenu();
  const dispatch = useDispatch();
  return (
    <div className="Nav">
      <div className="Nav-links">
        <Profile sessionUser={sessionUser} />
      </div>

      <div className="Nav-search-wrapper">
        <NavSearch
          placeholder="Search sets, solutions ..."
          cb={() => navigate(`/search?search=${userSearch}`)}
          setUserSearch={setUserSearch}
        />
        <PlusIcon />
        <div className="Nav-avatar-wrapper">
          <Avatar
            src={sessionUser?.image}
            size={"35px"}
            btnRef={btnRef}
            onClick={toggleMenu}
            inNav={true}
          />
          <Menu menuRef={menuRef} isOpen={show} right>
            {!sessionUser && (
              <MenuItem
                text="LogIn"
                onClick={() => {
                  navigate("/", { state: window.location.pathname });
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
                  navigate("/");
                }}
                icon={<i className="fa-solid fa-power-off"></i>}
              />
            )}
            <MenuItem
              text={theme === "light" ? "Dark mode" : "Light mode"}
              onClick={toggleTheme}
              icon={
                theme === "light" ? (
                  <i class="fa-solid fa-moon"></i>
                ) : (
                  <i className="fa-regular fa-sun"></i>
                )
              }
            />
          </Menu>
        </div>
      </div>
    </div>
  );
}

export default Navigation;
