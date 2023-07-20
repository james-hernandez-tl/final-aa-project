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

function Navigation({ isLoaded }) {
  const sessionUser = useSelector((state) => state.session.user);

  return (
    <div className="Nav">
      <div className="Nav-links">
        <Profile sessionUser={sessionUser} />
      </div>

      <div className="Nav-search-wrapper">
        <NavSearch placeholder="Search sets, solutions ..." />
        <PlusIcon />
      </div>
    </div>
  );
}

export default Navigation;
