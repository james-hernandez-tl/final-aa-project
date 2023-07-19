import { useDispatch } from "react-redux";
import "./Navigation.css";
import { useMenu } from "../Menu";
import { Menu, MenuItem } from "../Menu";
import { useNavigate } from "react-router-dom";
import { useModal } from "../../context/Modal";
import CreateFolder from "../CreateFolder.jsx";

export default function PlusIcon() {
  const navigation = useNavigate();
  const { btnRef, hideMenu, toggleMenu, show, menuRef } = useMenu();
  const { setModalContent } = useModal();
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
          icon={<i className="fa-regular fa-note-sticky"></i>}
        />
        <MenuItem
          text="New Folder"
          onClick={() => {
            hideMenu();
            setModalContent(<CreateFolder />);
          }}
          icon={<i className="fa-regular fa-folder"></i>}
        />
      </Menu>
    </>
  );
}
