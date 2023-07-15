import { useSelector } from "react-redux";

export default function useSession() {
  return useSelector((state) => state.session.user);
}
