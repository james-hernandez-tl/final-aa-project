import { qFetch } from "./utils";

//TYPES

const SET_FOLDER = "folders/getFolder";
const DELETE_FOLDER = "folders/deleteFolder";

//actions

const setFolder = (folder) => {
  return { type: SET_FOLDER, payload: folder };
};

//thunks

export const getFolder = (id) => async (dispatch) => {
  const response = await qFetch(`/api/folders/${id}`);

  if (response.ok) {
    let data = await response.json();
    dispatch(setFolder(data));
  }
};
let initialState = { singleFolder: null };

export default function reducer(state = initialState, action) {
  switch (action.type) {
    case SET_FOLDER:
      return { ...state, singleFolder: action.payload };
    default:
      return state;
  }
}
