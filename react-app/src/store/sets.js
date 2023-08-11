import { qFetch } from "./utils";
import { addUserSet } from "./session";
import { removeUserSet } from "./session";
import { editUserSet } from "./session";
//TYPES
const ALL_SETS = "sets/allSets";
const ONE_SET = "sets/oneSet";
const CREATE_SET = "sets/createSet";
const EDIT_SET = "sets/editSet";
const DELETE_SET = "sets/deleteSet";
const SEARCH_SETS = "sets/searchSets";

//ACTION

const allSetsAction = (allSets) => {
  return {
    type: ALL_SETS,
    payload: allSets,
  };
};

const searchSetsAction = (allSets) => {
  return {
    type: SEARCH_SETS,
    payload: allSets,
  };
};

const oneSetAction = (set) => {
  return {
    type: ONE_SET,
    payload: set,
  };
};

const createSetAction = (set) => {
  return {
    type: CREATE_SET,
    payload: set,
  };
};

const editSetAction = (set) => {
  return {
    type: EDIT_SET,
    payload: set,
  };
};

const deleteSetAction = (setId) => {
  return {
    type: DELETE_SET,
    payload: setId,
  };
};

//thunks

export const allSetThunk = () => async (dispatch) => {
  const response = await qFetch("/api/sets/");
  if (response.ok) {
    const data = await response.json();
    dispatch(allSetsAction(data));
  }
};

export const searchSets = (query) => async (dispatch) => {
  const response = await qFetch(`/api/sets/search${query}`);

  if (response.ok) {
    const data = await response.json();
    dispatch(searchSetsAction(data));
  }
};

export const createSetThunk = (set, cards) => async (dispatch) => {
  const response = await qFetch("/api/sets/", {
    method: "POST",
    body: JSON.stringify(set),
  });

  if (response.ok) {
    let set = await response.json();
    let updatedSet = await qFetch("/api/cards/", {
      method: "POST",
      body: JSON.stringify({
        cards: cards.map((card) => ({ ...card, setId: set.id })),
      }),
    });

    if (updatedSet.ok) {
      updatedSet = await updatedSet.json();
      await dispatch(createSetAction(updatedSet));
      await dispatch(
        addUserSet({ ...updatedSet, NumCards: updatedSet.Cards.length })
      );
    }
  }
};

export const deleteSetThunk = (setId) => async (dispatch) => {
  const response = await qFetch(`/api/sets/${setId}`, {
    method: "DELETE",
  });

  if (response.ok) {
    await dispatch(deleteSetAction(setId));
    await dispatch(removeUserSet(Number(setId)));
  }
};

export const editSetThunk = (set) => async (dispatch) => {
  const response = await qFetch(`/api/sets/${set.id}`, {
    method: "PUT",
    body: JSON.stringify(set),
  });

  if (response.ok) {
    let data = await response.json();
    dispatch(editSetAction(data));
    dispatch(editUserSet({ ...data, NumCards: data.Cards.length }));
  }
};

export const editCardsThunk = (cards) => async (dispatch) => {
  const response = await qFetch("/api/cards/", {
    method: "PUT",
    body: JSON.stringify({ cards }),
  });

  if (response.ok) {
    let data = await response.json();
    dispatch(editSetAction(data));
  }
};

export const addCardsThunk = (setId, cards) => async (dispatch) => {
  let updatedSet = await qFetch("/api/cards/", {
    method: "POST",
    body: JSON.stringify({
      cards: cards.map((card) => ({ ...card, setId })),
    }),
  });

  if (updatedSet.ok) {
    let data = await updatedSet.json();
    dispatch(editSetAction(data));
  }
};

export const getOneSetThunk = (setId) => async (dispatch) => {
  let set = await qFetch(`/api/sets/${setId}`);

  if (set.ok) {
    let data = await set.json();
    dispatch(oneSetAction(data));
  }
};

export const deleteCardsThunk = (cards) => async (dispatch) => {
  let deleted = await qFetch("/api/cards/", {
    method: "DELETE",
    body: JSON.stringify({ cards }),
  });

  if (deleted.ok) {
    let data = await deleted.json();
    dispatch(editSetAction(data));
    dispatch(editUserSet({ ...data, NumCards: data.Cards.length }));
  }
};

export const createRating = (rating) => async (dispatch) => {
  let newRating = await qFetch("/api/ratings/", {
    method: "POST",
    body: JSON.stringify(rating),
  });

  if (newRating.ok) {
    let data = await newRating.json();
    dispatch(editSetAction(data));
  }
};

export const editRating = (rating) => async (dispatch) => {
  let newRating = await qFetch("/api/ratings/", {
    method: "PUT",
    body: JSON.stringify(rating),
  });

  if (newRating.ok) {
    let data = await newRating.json();
    dispatch(editSetAction(data));
  }
};

//reducer
const initialState = { allSets: null, recommened: null, singleSet: null };

let normalizer = (arr) => {
  let obj = {};
  for (let i = 0; i < arr.length; i++) {
    if (arr[i].Cards) {
      arr[i].Cards = normalizer(arr[i].Cards);
    }
    obj[arr[i].id] = arr[i];
  }
  return obj;
};

export default function reducer(state = initialState, action) {
  switch (action.type) {
    case ALL_SETS:
      return {
        allSets: normalizer(action.payload.allSets),
        recommened: normalizer(action.payload.recommended),
      };
    case SEARCH_SETS:
      return {
        ...state,
        allSets: normalizer(action.payload.allSets),
      };
    case CREATE_SET:
      return {
        ...state,
        allSets: {
          ...state.allSets,
          [action.payload.id]: {
            ...action.payload,
            Cards: normalizer(action.payload.Cards),
          },
        },
        singleSet: action.payload,
      };
    case DELETE_SET:
      delete state.allSets[action.payload.setId];
      return { ...state, allSets: { ...state.allSets } };
    case EDIT_SET:
      return {
        ...state,
        allSets: {
          ...state.allSets,
          [action.payload.id]: { ...state.allSets[action.payload.id] },
        },
        singleSet: action.payload,
      };
    case ONE_SET:
      return {
        ...state,
        singleSet: action.payload,
        allSets: { ...state.allSets, [action.payload.id]: action.payload },
      };
    default:
      return state;
  }
}
