import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { useEffect } from "react";
import { getOneSetThunk } from "../../store/sets";
import SetForm from "../SetForm";

export default function SetFormDecider() {
  const set = useSelector((state) => state.sets.singleSet);
  const { setId } = useParams();
  const dispatch = useDispatch();

  console.log(setId);

  useEffect(() => {
    if (setId) {
      dispatch(getOneSetThunk(setId));
    }
  }, [dispatch, setId]);

  return (
    <>
      {set && setId && <SetForm set={set} />}
      {!setId && <SetForm />}
    </>
  );
}
