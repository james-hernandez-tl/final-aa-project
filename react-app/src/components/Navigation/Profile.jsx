import { NavLink } from "react-router-dom";
import { useNavigate } from "react-router-dom";
import "./Navigation.css";
export default function Profile({ sessionUser }) {
  let navigate = useNavigate();
  return (
    <>
      <h2
        className="Navigation-logo"
        onClick={() => {
          navigate("/");
        }}
      >
        KnowVerse
      </h2>
      <NavLink
        exact={"true"}
        to={"/"}
        className="Navlink-unactive"
        activeclassname="active"
      >
        Home
        <div className="Navlink-active-bar"></div>
      </NavLink>
      <NavLink
        to={"/sets"}
        className="Navlink-unactive"
        activeclassname="active"
      >
        Sets
        <div className="Navlink-active-bar"></div>
      </NavLink>
      <NavLink
        to={"/folders"}
        className="Navlink-unactive"
        activeclassname="active"
      >
        Folders
        <div className="Navlink-active-bar"></div>
      </NavLink>
      {/* <NavLink
        to={"/groups"}
        className="Navlink-unactive"
        activeclassname="active"
      >
        Groups
      </NavLink> */}
    </>
  );
}
