import "./FolderSingleView.css";
import { useModal } from "../../context/Modal";
import AddSet from "./AddSet";

export default function NoFolders() {
  const { setModalContent } = useModal();
  return (
    <div className="No-Folders">
      <h2 className="No-Folders-title">This folder has no sets yet</h2>
      <div>Organize all your study sets with folders.</div>
      <button
        className="No-Folders-btn"
        onClick={() => {
          setModalContent(<AddSet />);
        }}
      >
        Add a set
      </button>
    </div>
  );
}
