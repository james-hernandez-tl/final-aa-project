import { getFolder } from "../../store/folder";
import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { useEffect } from "react";
import YourItemLayout from "../YourItemLayout";

export default function FolderSingleView() {
  let folder = useSelector((state) => state.folders.singleFolder);
  const dispatch = useDispatch();
  const { folderId } = useParams();

  useEffect(() => {
    dispatch(getFolder(folderId));
  }, [dispatch, folderId]);

  if (!folder) return null;
  console.log(folder);
  return (
    <div>
      {folder.Sets.length
        ? folder.Sets.map((item) => (
            <YourItemLayout set={true} item={item} key={item.id} />
          ))
        : "you dont hvae any Sets in this folder"}
    </div>
  );
}
