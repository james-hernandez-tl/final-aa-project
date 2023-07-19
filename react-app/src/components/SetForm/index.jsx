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
    console.log("list of delted cards", deletedCards);
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
      let addedCards = cards.filter((card) => !card.id);
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
  console.log("cards", cards);
  return (
    <div className="SetForm">
      <div className="SetForm-header">Create New Set</div>
      <div>
        <input
          type="text"
          placeholder="Example :history"
          value={name}
          onChange={(e) => setName(e.target.value)}
          className="SetForm-inputs"
        />
        <div>title</div>
      </div>
      <div>
        <input
          type="text"
          placeholder="Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          className="SetForm-inputs"
        />
        <div>Description</div>
      </div>
      {cards.map((card, index) => (
        <CardForm
          key={card.psudeoId}
          index={index}
          setCards={setCards}
          card={card}
          setDeletedCards={setDeletedCards}
        />
      ))}
      <div onClick={addCardClicker}>Add Card</div>
      <div onClick={() => createClicker(false)}>Create</div>
      <div onClick={() => createClicker(true)}>Draft</div>
    </div>
  );
}
