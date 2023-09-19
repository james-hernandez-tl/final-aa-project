import useSession from "../../hooks/useSession";
import "./FolderSingleView.css";
import { useModal } from "../../context/Modal";
import { removeSetFromFolder, addSetToFolder } from "../../store/folder";
import { useSelector, useDispatch } from "react-redux";
import { useNavigate } from "react-router-dom";

export default function AddSet() {
  const user = useSession();
  const { closeModal } = useModal();
  const folder = useSelector((state) => state.folders.singleFolder);
  const dispatch = useDispatch();
  const navigate = useNavigate();

  const addSetClicker = (setId) => {
    if (folder.Sets.filter((set) => set.id == setId).length) {
      dispatch(removeSetFromFolder(folder.id, setId));
    } else {
      dispatch(addSetToFolder(folder.id, setId));
    }
  };
  return (
    <div className="AddSet">
      <div className="AddSet-Header">
        <h2 className="AddSet-Header-title">Add a set</h2>
        <div className="AddSet-Header-exit" onClick={closeModal}>
          <i className="fa-solid fa-xmark"></i>
        </div>
      </div>
      <div>
        <div
          className="AddSet-createSet-wrapper"
          onClick={() => {
            closeModal();
            navigate("/sets/new");
          }}
        >
          <div className="AddSet-createSet">
            <span className="fa-plus-AddSet ">
              <i className="fa-solid fa-plus"></i>
            </span>
            CREATE A NEW SET
          </div>
          <div className="AddSet-createSet-bar"></div>
        </div>
        <div className="AddSet-dropdown-wrapper">
          <select className="AddSet-dropdown">
            <option value="your-sets">Your sets</option>
          </select>
        </div>
        {user.Sets.map((set) => {
          let inFolder = folder.Sets.filter(
            (set2) => set2.id === set.id
          ).length;
          return (
            <div className="AddSet-set" key={set.id}>
              <h3>{set.name}</h3>
              <div
                className={`AddSet-set-plus-wrapper ${
                  inFolder ? "AddSet-set-plus-wrapper-inFolder" : ""
                }`}
                onClick={() => {
                  addSetClicker(set.id);
                }}
              >
                {inFolder ? (
                  <i className="fa-solid fa-minus fa-minus-AddSet-set"></i>
                ) : (
                  <i className="fa-solid fa-plus fa-plus-AddSet-set"></i>
                )}
              </div>
            </div>
          );
        })}
      </div>
    </div>
  );
}
