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

//reducer
const initialState = { allSets: null, recommened: null };

let normalizer = (arr) => {
  let obj = {};
  for (let i = 0; i < arr.length; i++) {
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
    default:
      return state;
  }
}
