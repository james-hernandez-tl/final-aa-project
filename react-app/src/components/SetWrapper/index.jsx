import SetMainLayout from "../SetMainLayout";
import { useState } from "react";
import { useRef } from "react";
import "./SetWrapper.css";

export default function SetWrapper({ allSets, color = "#586380" }) {
  const containerRef = useRef(null);

  const handleNextClick = () => {
    const scrollDistance = containerRef.current.offsetWidth;
    containerRef.current.scrollBy({
      left: scrollDistance,
      behavior: "smooth",
    });
  };

  const handlePreviousClick = () => {
    const scrollDistance = containerRef.current.offsetWidth;
    containerRef.current.scrollBy({
      left: -scrollDistance,
      behavior: "smooth",
    });
  };
  return (
    <div className="SetWrapper" style={{ background: color }}>
      <div className="slider" ref={containerRef}>
        {allSets.map((set) => (
          <SetMainLayout set={set} key={set.id} />
        ))}
      </div>
      <div className="slider-controls">
        <button onClick={handlePreviousClick}>Previous</button>
        <button onClick={handleNextClick}>Next</button>
      </div>
    </div>
  );
}
