import useSession from "../../hooks/useSession";
import { addSetToFolder, removeSetFromFolder } from "../../store/folder";
import { useDispatch } from "react-redux";
import "./AddSetToFolder.css";

export default function AddSetToFolder({ setId }) {
  const dispatch = useDispatch();
  const user = useSession();
  const folderClicker = (folder) => {
    if (folder.Sets.filter((set) => set.id == setId).length) {
      dispatch(removeSetFromFolder(folder.id, setId));
    } else {
      dispatch(addSetToFolder(folder.id, setId));
    }
  };

  return (
    <div className="AddSetToFolder">
      <div className="AddSetToFolder-header">Add to folder</div>
      <div className="AddSetToFolder-divider"></div>
      {user.Folders.map((folder) => (
        <div
          key={folder.id}
          className={`AddSetToFolder-folder
            ${
              folder.Sets.filter((set) => set.id == setId).length
                ? "AddSetToFolder-folder-red"
                : "AddSetToFolder-folder-green"
            }`}
          onClick={() => folderClicker(folder)}
        >
          <div>{folder.name}</div>
          <div>
            {folder.Sets.filter((set) => set.id == setId).length ? "-" : "+"}
          </div>
        </div>
      ))}
    </div>
  );
}
