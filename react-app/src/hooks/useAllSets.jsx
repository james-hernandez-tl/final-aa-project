import { useSelector } from "react-redux";

export default function useAllSets() {
  return useSelector((state) => state.sets.allSets);
}
