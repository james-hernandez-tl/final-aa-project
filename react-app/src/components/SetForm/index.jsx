import CardForm from "../CardForm";
import { useState } from "react";
import { v4 as uuidv4 } from "uuid";
import { useDispatch } from "react-redux";
import { createSetThunk } from "../../store/sets";
import useSession from "../../hooks/useSession";

export default function SetForm({ set }) {
  const dispatch = useDispatch();
  const currentUser = useSession();
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

  const createClicker = (isDraft) => {
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
  };

  return (
    <div>
      <div>Create New Set</div>
      <div>
        <input
          type="text"
          placeholder="Example :history"
          value={name}
          onChange={(e) => setName(e.target.value)}
        />
        <div>title</div>
      </div>
      <div>
        <input
          type="text"
          placeholder="Description"
          value={description}
          onChange={(e) => setDescription(e.target.value)}
        />
        <div>Description</div>
      </div>
      {cards.map((card, index) => (
        <CardForm
          key={card.psudeoId}
          index={index}
          setCards={setCards}
          card={card}
        />
      ))}
      <div onClick={addCardClicker}>Add Card</div>
      <div onClick={() => createClicker(false)}>Create</div>
      <div onClick={() => createClicker(true)}>Draft</div>
    </div>
  );
}
