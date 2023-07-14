import React from "react";
import { NavLink, Link } from "react-router-dom";
import { useSelector } from "react-redux";
import ProfileButton from "./ProfileButton";
import "./Navigation.css";
import Avatar from "../Avatar";
import { useMenu } from "../Menu";
import { Menu, MenuItem } from "../Menu";

function Navigation({ isLoaded }) {
  const sessionUser = useSelector((state) => state.session.user);
  const { btnRef, hideMenu, toggleMenu, show, menuRef } = useMenu();

  return (
    <div className="Nav">
      <div className="Nav-links">
        <Avatar
          src={sessionUser?.image}
          size={"35px"}
          btnRef={btnRef}
          onClick={toggleMenu}
        />
        <Menu menuRef={menuRef} isOpen={show}>
          <MenuItem text="LogIn" />
          <MenuItem text="idk" />
        </Menu>

        <NavLink to={"/"}>KnowVerse</NavLink>
        <NavLink to={"/sets"}>Sets</NavLink>
        <NavLink to={"/folders"}>Folders</NavLink>
        <NavLink to={"/groups"}>Groups</NavLink>
      </div>

      <div className="Nav-search-wrapper">
        <div className="Nav-search">
          <i className="fa-solid fa-magnifying-glass search"></i>
          <input type="text" placeholder="Search sets" />
        </div>
        <i className="fa-solid fa-circle-plus nav-plus"></i>
      </div>
    </div>
  );
}

export default Navigation;
