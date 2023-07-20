import { useState } from "react";
import "./CardForm.css";

export default function CardForm({
  card,
  index,
  setCards,
  setDeletedCards,
  error,
}) {
  const [answer, setAnswer] = useState(card.answer);
  const [question, setQuestion] = useState(card.question);

  const cardChanger = (psudeoId, answer, question) => {
    setCards((state) =>
      state.map((card) => {
        if (card.psudeoId === psudeoId) {
          card.answer = answer;
          card.question = question;
          if (card.id) card.edited = true;
        }
        return card;
      })
    );
  };

  const questionChanger = (e) => {
    setQuestion(e.target.value);
    cardChanger(card.psudeoId, answer, e.target.value);
  };

  const answerChanger = (e) => {
    setAnswer(e.target.value);
    cardChanger(card.psudeoId, e.target.value, question);
  };

  const deleteCard = (psudeoId) => {
    setCards((state) => {
      if (state.length > 2) {
        if (card.id) {
          setDeletedCards((state) => [...state, card.id]);
        }
        return state.filter((card) => card.psudeoId !== psudeoId);
      }
      return state;
    });
  };

  return (
    <div className="CardForm">
      <div className="CardForm-header">
        <div>{index + 1}</div>
        <div onClick={() => deleteCard(card.psudeoId)}>
          <i className="fa-regular fa-trash-can"></i>
        </div>
      </div>
      <div className="CardForm-divider"></div>
      <div className="CardForm-Input-wrappers">
        <div>
          <input
            type="text"
            placeholder={error ?? "Enter Term"}
            value={question}
            onChange={questionChanger}
            className={`CardForm-inputs ${error}`}
          />
          <div className="CardForm-inputs-labels">TERM</div>
        </div>
        <div>
          <input
            type="text"
            placeholder={error ?? "Enter Definition"}
            value={answer}
            onChange={answerChanger}
            className={`CardForm-inputs ${error}`}
          />
          <div className="CardForm-inputs-labels">DEFINITION</div>
        </div>
      </div>
    </div>
  );
}
