import React from "react";
import "./Landing.css";
import { useModal } from "../../context/Modal";
import LoginPage from "../LoginPage";
import SignUpPage from "../SignUpPage";
import { useTheme } from "../../context/ColorProvider";

export default function Landing() {
  const { setModalContent } = useModal();
  const { theme } = useTheme();
  return (
    <div>
      <div className="Landing-Nav">
        <div className="Landing-Nav-left">
          <div className="Landing-Nav-logo">KnowVerse</div>
        </div>
        <div className="Landing-Nav-right">
          <div
            className="Landing-Nav-signin"
            onClick={() => {
              setModalContent(<LoginPage />);
            }}
          >
            sign in
          </div>
          <div
            className="Landing-Nav-signup"
            onClick={() => {
              setModalContent(<SignUpPage />);
            }}
          >
            sign up
          </div>
        </div>
      </div>
      <div className="Landing-Main">
        {/* <div className="Landing-Main-header">
          <div className="Landing-Main-matters">It matters</div>
          <div className="Landing-Main-ask"> &nbsp;how you ask</div>
        </div> */}
        <div className="Landing-Headers">Weclome to KnowVerse</div>
        <video
          autoPlay
          muted
          loop
          src={`/useKnowVerse-${theme}.mov`}
          style={{ width: "1000px" }}
        />
        <div className="Landing-Headers">
          Create sets and use them to study!
        </div>
        <video
          autoPlay
          muted
          loop
          src={`/createASet-${theme}.mov`}
          style={{ width: "1000px" }}
        />
        <div className="Landing-Headers">Create Folders</div>
        <video
          autoPlay
          muted
          loop
          src={`/createAFolder-${theme}.mov`}
          style={{ width: "1000px" }}
        />
        {/* <video src="./media/Home-page.mov"></video> */}
      </div>
    </div>
  );
}
