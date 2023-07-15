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

function Navigation({ isLoaded }) {
  const sessionUser = useSelector((state) => state.session.user);

  return (
    <div className="Nav">
      <div className="Nav-links">
        <Profile sessionUser={sessionUser} />
      </div>

      <div className="Nav-search-wrapper">
        <div className="Nav-search">
          <i className="fa-solid fa-magnifying-glass search"></i>
          <input type="text" placeholder="Search sets" />
        </div>
        <PlusIcon />
      </div>
    </div>
  );
}

export default Navigation;
