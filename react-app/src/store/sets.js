import { qFetch } from "./utils";
//TYPES
const ALL_SETS = "sets/allSets";
const ONE_SET = "sets/oneSet";
const CREATE_SET = "sets/createSet";
const EDIT_SET = "sets/editSet";
const DELETE_SET = "sets/deleteSet";

//ACTION

const allSetsAction = (allSets) => {
  return {
    type: ALL_SETS,
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

export const createSetThunk = (set, cards) => async (dispatch) => {
  const response = await qFetch("/api/sets/", {
    method: "POST",
    body: JSON.stringify(set),
  });

  if (response.ok) {
    let set = await response.json();
    console.log("set created", set);
    let updatedSet = await qFetch("/api/cards/", {
      method: "POST",
      body: JSON.stringify({
        cards: cards.map((card) => ({ ...card, setId: set.id })),
      }),
    });

    if (updatedSet.ok) {
      updatedSet = await updatedSet.json();
      console.log("updatedSet", updatedSet);
      dispatch(createSetAction(updatedSet));
    }
  }
};

//reducer
const initialState = { allSets: null, recommened: null };

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
      };
    default:
      return state;
  }
}
