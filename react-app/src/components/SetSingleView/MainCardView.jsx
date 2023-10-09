import ReactCardFlip from "react-card-flip";
import { useSpeechSynthesis } from "react-speech-kit";
import "./SetSingleView.css";
import { useState } from "react";

export default function MainCardView({
  cards,
  isFlipped,
  setIsFlipped,
  index,
  containerClassName,
  showHint,
  setShowHint,
}) {
  const card = cards[index];
  const { speak, voices, cancel } = useSpeechSynthesis();

  return (
    <ReactCardFlip
      containerClassName={containerClassName}
      isFlipped={isFlipped}
      flipDirection="vertical"
      containerStyle={{ position: "relative" }}
    >
      <div className={`SetSingleView-card`} onClick={() => setIsFlipped(true)}>
        <div className="SetSingleView-card-header">
          <div
            className={`SetSingleView-card-hint ${
              showHint ? "SetSingleView-card-header-hint" : ""
            }`}
            onClick={(e) => {
              e.stopPropagation();
              setShowHint((state) => !state);
            }}
          >
            {showHint ? (
              <div>
                {(() => {
                  const length = card.answer.length;
                  let value;
                  if (length < 3) value = card.answer[0];
                  else if (length < 30)
                    value = card.answer.slice(0, Math.floor(length / 3));
                  else value = card.answer.slice(0, 10);
                  for (let i = value.length; i <= 10; i++) {
                    value += "_";
                  }
                  return value;
                })()}
              </div>
            ) : (
              <div>
                Get a hint <i className="fa-regular fa-lightbulb"></i>{" "}
              </div>
            )}
          </div>
        </div>
        <div
          className="text-to-speech"
          onClick={(e) => {
            cancel();
            e.stopPropagation();
            speak({
              text: card.question,
              voice: voices[51],
            });
          }}
        >
          <i className="fa-solid fa-volume-high"></i>
        </div>
        <div className="SetSingleView-card-content">{card.question}</div>
      </div>
      <div className="SetSingleView-card" onClick={() => setIsFlipped(false)}>
        <div
          className="text-to-speech"
          onClick={(e) => {
            e.stopPropagation();
            speak({
              text: card.answer,
              voice: voices[51],
            });
          }}
        >
          <i className="fa-solid fa-volume-high"></i>
        </div>
        <div className="SetSingleView-card-content">{card.answer}</div>
      </div>
    </ReactCardFlip>
  );
}
