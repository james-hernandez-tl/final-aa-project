import { NavLink, Link } from "react-router-dom";
import { useSelector, useDispatch } from "react-redux";
import "./Navigation.css";
import Avatar from "../Avatar";
import { useMenu } from "../Menu";
import { Menu, MenuItem } from "../Menu";
import { useNavigate } from "react-router-dom";
import { logout } from "../../store/session";
export default function PlusIcon() {
  const navigation = useNavigate();
  const dispatch = useDispatch();
  const { btnRef, hideMenu, toggleMenu, show, menuRef } = useMenu();
  return (
    <>
      <i
        className="fa-solid fa-circle-plus nav-plus"
        ref={btnRef}
        onClick={toggleMenu}
      ></i>
      <Menu menuRef={menuRef} isOpen={show} right>
        <MenuItem
          text="New Set"
          onClick={() => {
            navigation("/sets/new");
            hideMenu();
          }}
        />
        <MenuItem text="New Folder" />
      </Menu>
    </>
  );
}
