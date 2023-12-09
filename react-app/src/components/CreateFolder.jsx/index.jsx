import { useModal } from "../../context/Modal";
import { useDispatch } from "react-redux";
import { createFolder } from "../../store/folder";
import { useState, useEffect } from "react";
import useSession from "../../hooks/useSession";
import { useNavigate } from "react-router-dom";
import { editFolder } from "../../store/folder";
import "./CreateFolder.css";

export default function CreateFolder({ folder }) {
  const dispatch = useDispatch();
  const navigate = useNavigate();
  const user = useSession();
  const [error, setError] = useState(null);
  const [name, setName] = useState(folder ? folder.name : "");
  const [description, setDescription] = useState(
    folder ? folder.description : ""
  );
  const [nameTooLong, setNameTooLong] = useState(null);
  const [desTooLong, setDesTooLong] = useState(null);

  const { closeModal } = useModal();

  const createFolderClicker = async () => {
    if (!name || !description) {
      setError("Required");
      return;
    }

    if (name.length > 20) {
      setNameTooLong("Name must be less than 20 characters");
    }

    if (description.length > 100) {
      setDesTooLong("Description must be less than 100 character");
    }

    if (name.length > 20 || description.length > 100) return;

    closeModal();
    if (!folder) {
      const newFolder = await dispatch(
        createFolder({ name, description, userId: user.id })
      );
      navigate(`/folders/${newFolder.id}`);
    } else {
      dispatch(
        editFolder({
          name,
          description,
          userId: user.id,
          edited: true,
          id: folder.id,
        })
      );
    }
  };

  useEffect(() => {
    if (!user) {
      navigate("/", { state: window.location.pathname });
    }
  }, []);

  if (!user) {
    closeModal();
    return null;
  }

  return (
    <div className="CreateFolder">
      <div className="CreateFolder-header">
        {!folder ? "Create A New Folder" : "Edit Folder"}
      </div>
      <div>
        <input
          type="text"
          placeholder={error ?? "Enter a tilte"}
          value={nameTooLong ?? name}
          onChange={(e) => setName(e.target.value)}
          className={`CreateFolder-input-title ${error} ${
            nameTooLong ? "CreateFolder-toolong" : ""
          }`}
          onClick={() => setNameTooLong(null)}
        />
      </div>
      <div>
        <input
          type="text"
          placeholder={error ?? "Enter a description"}
          value={desTooLong ?? description}
          onChange={(e) => setDescription(e.target.value)}
          className={`CreateFolder-input-description ${error} ${
            desTooLong ? "CreateFolder-toolong" : ""
          }`}
          onClick={() => setDesTooLong(null)}
        />
      </div>
      <div className="CreateFolder-button-wrapper">
        <button onClick={createFolderClicker}>
          {folder ? "Edit" : "Create"} folder
        </button>
      </div>
    </div>
  );
}
