import { getOneSetThunk } from "../../store/sets";
import { useDispatch, useSelector } from "react-redux";
import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import useSession from "../../hooks/useSession";
import { deleteSetThunk } from "../../store/sets";

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

  const deleteSetClicker = () => {
    dispatch(deleteSetThunk(setId));
    navigate("/sets");
  };

  if (!set) return <div>There is no set with this id</div>;

  return (
    <div className="SetSingleView">
      <div>{set.name}</div>
      <div className="SetSingleView-card">
        <div>edit card</div>
        <div>{set.Cards[0].question}</div>
      </div>
      {set.userId === user?.id && <div onClick={editSetClicker}>EDIT SET</div>}
      {set.userId === user?.id && (
        <div onClick={deleteSetClicker}>DELETE SET</div>
      )}
    </div>
  );
}
