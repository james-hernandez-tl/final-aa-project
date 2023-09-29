import ReactCardFlip from "react-card-flip";
import { useSpeechSynthesis } from "react-speech-kit";
import "./SetSingleView.css";

export default function MainCardView({
  cards,
  isFlipped,
  setIsFlipped,
  index,
  containerClassName,
}) {
  const card = cards[index];
  const { speak, voices, cancel } = useSpeechSynthesis();
  console.log(voices);

  return (
    <ReactCardFlip
      containerClassName={containerClassName}
      isFlipped={isFlipped}
      flipDirection="vertical"
      containerStyle={{ position: "relative" }}
    >
      <div className={`SetSingleView-card`} onClick={() => setIsFlipped(true)}>
        <div className="SetSingleView-card-header">
          <div className="SetSingleView-card-hint">
            <div>
              Get a hint <i className="fa-regular fa-lightbulb"></i>{" "}
            </div>
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
