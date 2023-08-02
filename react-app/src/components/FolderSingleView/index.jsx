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

export default function FolderSingleView() {
  let folder = useSelector((state) => state.folders.singleFolder);
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const { setModalContent } = useModal();
  const { folderId } = useParams();

  useEffect(() => {
    dispatch(getFolder(folderId));
  }, [dispatch, folderId]);

  if (!folder) return <div>Folder does not exist</div>;
  return (
    <div className="FolderSingleView">
      <div className="FolderSingleView-header">
        <div className="FolderSingleView-header-title">{folder.name}</div>
        <div
          onClick={() => {
            setModalContent(<CreateFolder folder={folder} />);
          }}
        >
          Edit
        </div>
        <div
          onClick={() => {
            dispatch(deleteFolder(folder.id));
            navigate("/folders");
          }}
        >
          delete
        </div>
      </div>
      <div>
        {folder.Sets.length
          ? folder.Sets.map((item) => (
              <YourItemLayout isSet={true} item={item} key={item.id} />
            ))
          : "You dont have any sets in this folder"}
      </div>
    </div>
  );
}
