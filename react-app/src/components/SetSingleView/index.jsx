import { getOneSetThunk } from "../../store/sets";
import { useDispatch, useSelector } from "react-redux";
import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import useSession from "../../hooks/useSession";

export default function SetSingleView() {
  const navigate = useNavigate();
  const { setId } = useParams();
  const dispatch = useDispatch();

  const set = useSelector((state) => state.sets.singleSet);
  const user = useSession();

  useEffect(() => {
    dispatch(getOneSetThunk(setId));
  }, [dispatch, setId]);

  const editSetClicker = () => {
    navigate(`/sets/${setId}/edit`);
  };

  if (!set) return <div>There is no set with this id</div>;

  return (
    <div className="SetSingleView">
      <div>{set.name}</div>
      <div className="SetSingleView-card">
        <div>edit</div>
        <div>{set.Cards[0].question}</div>
      </div>
      {set.userId === user?.id && <div onClick={editSetClicker}>EDIT</div>}
    </div>
  );
}
