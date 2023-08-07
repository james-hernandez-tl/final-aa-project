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
    const remainder =
      containerRef.current.scrollWidth -
      containerRef.current.scrollLeft -
      containerRef.current.clientWidth;

    if (remainder < 1) {
      console.log("idk");
    }
  };

  const handlePreviousClick = () => {
    const scrollDistance = containerRef.current.offsetWidth;
    containerRef.current.scrollBy({
      left: -scrollDistance,
      behavior: "smooth",
    });
    console.log(containerRef.current);
  };
  return (
    <div className="SetWrapper" style={{ background: color }}>
      <div className="slider-controls-prev">
        <i className="fa-solid fa-arrow-left" onClick={handlePreviousClick}></i>
      </div>
      <div className="slider" ref={containerRef}>
        {allSets.map((set) => (
          <SetMainLayout set={set} key={set.id} />
        ))}
      </div>
      <div className="slider-controls-next">
        <i onClick={handleNextClick} className="fa-solid fa-arrow-right"></i>
      </div>
    </div>
  );
}
