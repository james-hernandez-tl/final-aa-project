import { useSelector } from "react-redux";

export default function useRecommened() {
  return useSelector((state) => state.sets.recommened);
}
