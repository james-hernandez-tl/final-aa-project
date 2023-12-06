import React from "react";
import "./Landing.css";

export default function Landing() {
  return (
    <div>
      <div className="Landing-Nav">
        <div className="Landing-Nav-left">
          <div className="Landing-Nav-logo">KnowVerse</div>
        </div>
        <div className="Landing-Nav-right">
          <div className="Landing-Nav-signin">sign in</div>
          <div className="Landing-Nav-signup">sign up</div>
        </div>
      </div>
      <div className="Landing-Main">
        <div>
          <div className="Landing-Main-matters">It matters</div>
          <div className="Landing-Main-ask">how you ask</div>
        </div>
      </div>
    </div>
  );
}
