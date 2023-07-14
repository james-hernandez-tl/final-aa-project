import "./Home.css";
import { allSetThunk } from "../../store/sets";
import { useDispatch } from "react-redux";
import useAllSets from "../../hooks/useAllSets";
import { useEffect } from "react";
import SetWrapper from "../SetWrapper";

export default function Home() {
  const dispatch = useDispatch();
  let allSets = useAllSets();

  useEffect(() => {
    dispatch(allSetThunk());
  }, [dispatch]);

  if (!allSets) return null;
  allSets = Object.values(allSets);
  return (
    <div className="Home">
      <div className="Home-achievements">Achievements</div>
      <SetWrapper allSets={allSets.slice(0, 5)} />
    </div>
  );
}
