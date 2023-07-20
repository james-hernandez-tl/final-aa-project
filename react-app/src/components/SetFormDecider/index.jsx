import { useDispatch, useSelector } from "react-redux";
import { useParams } from "react-router-dom";
import { useEffect } from "react";
import { getOneSetThunk } from "../../store/sets";
import useSession from "../../hooks/useSession";
import { useNavigate } from "react-router-dom";
import SetForm from "../SetForm";

export default function SetFormDecider() {
  const navigate = useNavigate();
  const set = useSelector((state) => state.sets.singleSet);
  const user = useSession();
  const { setId } = useParams();
  const dispatch = useDispatch();

  useEffect(() => {
    if (setId) {
      dispatch(getOneSetThunk(setId));
    }
  }, [dispatch, setId]);

  useEffect(() => {
    if (!user) {
      navigate("/logIn", { state: window.location.pathname });
    }
  }, []);

  if (!user) return null;

  return (
    <>
      {set && setId && <SetForm set={set} />}
      {!setId && <SetForm />}
    </>
  );
}
