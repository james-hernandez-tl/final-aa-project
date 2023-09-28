import ReactCardFlip from "react-card-flip";
import "./SetSingleView.css";

export default function MainCardView({
  cards,
  isFlipped,
  setIsFlipped,
  index,
  containerClassName,
}) {
  const card = cards[index];

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
        <div className="SetSingleView-card-content">{card.question}</div>
      </div>
      <div className="SetSingleView-card" onClick={() => setIsFlipped(false)}>
        <div className="SetSingleView-card-header"></div>
        <div className="SetSingleView-card-content">{card.answer}</div>
      </div>
    </ReactCardFlip>
  );
}
