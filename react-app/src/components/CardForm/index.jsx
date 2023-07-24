import { useState, useEffect } from "react";
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
  const [answerTooLong, setAnwerTooLong] = useState(null);
  const [questionTooLong, setQuestionTooLong] = useState(null);

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

  useEffect(() => {
    if (answer.length > 225) setAnwerTooLong(true);
    else setAnwerTooLong(null);

    if (question.length > 225) setQuestionTooLong(true);
    else setQuestionTooLong(null);
  }, [answer, question]);

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
          <div
            className={`CardForm-inputs-labels ${
              questionTooLong ? "SetForm-length-error" : ""
            }`}
          >
            {questionTooLong
              ? "Question too long, must be less than 225 characters"
              : "TERM"}
          </div>
        </div>
        <div>
          <input
            type="text"
            placeholder={error ?? "Enter Definition"}
            value={answer}
            onChange={answerChanger}
            className={`CardForm-inputs ${error}`}
          />
          <div
            className={`CardForm-inputs-labels ${
              answerTooLong ? "SetForm-length-error" : ""
            }`}
          >
            {answerTooLong
              ? "Answer too long, must be less than 225 character"
              : "DEFINITION"}
          </div>
        </div>
      </div>
    </div>
  );
}
