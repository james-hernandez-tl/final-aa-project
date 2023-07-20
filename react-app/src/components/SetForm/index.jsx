import CardForm from "../CardForm";
import { useState } from "react";
import { v4 as uuidv4 } from "uuid";
import { useDispatch } from "react-redux";
import {
  createSetThunk,
  editSetThunk,
  editCardsThunk,
  addCardsThunk,
  deleteCardsThunk,
} from "../../store/sets";
import useSession from "../../hooks/useSession";
import { useNavigate } from "react-router-dom";
import "./SetForm.css";

export default function SetForm({ set }) {
  const navigate = useNavigate();
  const dispatch = useDispatch();
  const currentUser = useSession();
  const [error, setError] = useState(null);
  const [deletedCards, setDeletedCards] = useState([]);
  const [name, setName] = useState(set ? set.name : "");
  const [description, setDescription] = useState(set ? set.description : "");
  const [cards, setCards] = useState(
    set
      ? Object.values(set.Cards).map((card) => ({
          ...card,
          psudeoId: uuidv4(),
        }))
      : []
  );

  let addCardClicker = () => {
    setCards((state) => [
      ...state,
      { psudeoId: uuidv4(), answer: "", question: "" },
    ]);
  };

  if (cards.length < 2) {
    addCardClicker();
    return null;
  }
  console.log("cards", cards);

  const createClicker = async (isDraft) => {
    console.log(deletedCards);
    const cardError = cards.find((ele, index) => {
      let questionBlank = !ele.question && ele.answer;
      let answerBlank = ele.question && !ele.answer;
      if (index < 2 && (!ele.question || !ele.answer)) {
        return true;
      }
      if (ele.id && (!ele.question || !ele.answer)) {
        return true;
      }
      if (index >= 2 && (questionBlank || answerBlank)) {
        return true;
      }

      return false;
    });

    console.log("found", cardError);

    if (!name || !description || cardError) {
      setError("Required");
      return;
    }

    if (!set) {
      dispatch(
        createSetThunk(
          {
            name,
            description,
            draft: isDraft,
            userId: currentUser.id,
          },
          cards
        )
      );
    } else {
      let editedCards = cards.filter((card) => card.edited);
      let addedCards = cards.filter(
        (card) => !card.id && card.answer && card.question
      );
      if (editedCards.length) await dispatch(editCardsThunk(editedCards));
      if (addedCards.length) await dispatch(addCardsThunk(set.id, addedCards));
      if (deletedCards.length) await dispatch(deleteCardsThunk(deletedCards));
      dispatch(
        editSetThunk({
          name,
          description,
          draft: isDraft,
          userId: currentUser.id,
          id: set.id,
          edited: true,
        })
      );
    }

    navigate("/sets");
  };
  return (
    <div className="SetForm">
      <div className="SetForm-header">Create New Set</div>
      <div className="SetForm-input-wrapper">
        <input
          type="text"
          placeholder={error ?? `Example: 'History Section 10 '`}
          value={name}
          onChange={(e) => setName(e.target.value)}
          className={`SetForm-inputs ${error}`}
        />
        <div className="SetForm-input-lables">TITLE</div>
      </div>
      <div className="SetForm-input-wrapper">
        <input
          type="text"
          placeholder={error ?? "Description"}
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          className={`SetForm-inputs ${error}`}
        />
        <div className="SetForm-input-lables">DESCRIPTION</div>
      </div>
      {cards.map((card, index) => (
        <CardForm
          key={card.psudeoId}
          index={index}
          setCards={setCards}
          card={card}
          setDeletedCards={setDeletedCards}
          error={error}
        />
      ))}
      <div className="SetForm-addCard" onClick={addCardClicker}>
        <div>+</div> ADD CARD
      </div>
      <div className="SetForm-button-wrapper">
        <button
          className="SetForm-CreateCard"
          onClick={() => createClicker(false)}
        >
          Create
        </button>
        <button
          className="SetForm-EditCard"
          onClick={() => createClicker(true)}
        >
          Draft
        </button>
      </div>
    </div>
  );
}
