import { getFolder } from "../../store/folder";
import { useDispatch, useSelector } from "react-redux";
import { useNavigate } from "react-router-dom";
import { useParams } from "react-router-dom";
import { useEffect } from "react";
import YourItemLayout from "../YourItemLayout";
import CreateFolder from "../CreateFolder.jsx";
import { useModal } from "../../context/Modal";
import { deleteFolder } from "../../store/folder";
import "./FolderSingleView.css";
import { Menu, MenuItem, useMenu } from "../Menu";
import NoFolders from "./NoFolders";
import AddSet from "./AddSet";
import ClipLoader from "react-spinners/ClipLoader";

export default function FolderSingleView() {
  let folder = useSelector((state) => state.folders.singleFolder);
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const { setModalContent } = useModal();
  const { folderId } = useParams();
  const { btnRef, hideMenu, toggleMenu, show, menuRef } = useMenu();

  useEffect(() => {
    dispatch(getFolder(folderId));
  }, [dispatch, folderId]);

  if (!folder || folder.id != folderId)
    return (
      <div className="Home-loadingScreen">
        <ClipLoader color="white" size={100} />
      </div>
    );
  return (
    <div className="FolderSingleView">
      <div className="FolderSingleView-header">
        <h2 className="FolderSingleView-header-title">
          <span className="FolderSingleView-header-title-icon">
            <i className="fa-regular fa-folder"></i>
          </span>
          {folder.name}
        </h2>
        <div className="FolderSingleView-option-wrapper">
          <div
            onClick={() => {
              setModalContent(<AddSet />);
            }}
          >
            <i className="fa-solid fa-plus fa-circle-folder-singleView"></i>
          </div>
          <div className="FolderSingleView-createFolder-wrapper">
            <i
              ref={btnRef}
              onClick={toggleMenu}
              className="fa-solid fa-ellipsis fa-ellipsis-folder-singleView"
            ></i>
            <Menu menuRef={menuRef} isOpen={show} top right>
              <MenuItem
                text="edit"
                onClick={() => {
                  hideMenu();
                  setModalContent(<CreateFolder folder={folder} />);
                }}
                icon={<i className="fa-solid fa-pen"></i>}
              />
              <MenuItem
                text="delete"
                onClick={() => {
                  dispatch(deleteFolder(folder.id));
                  navigate("/folders");
                }}
                icon={<i className="fa-solid fa-trash"></i>}
              />
            </Menu>
          </div>
        </div>
      </div>
      <div>
        {folder.Sets.length ? (
          folder.Sets.map((item) => (
            <YourItemLayout isSet={true} item={item} key={item.id} />
          ))
        ) : (
          <NoFolders />
        )}
      </div>
    </div>
  );
}
