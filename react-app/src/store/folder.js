import { qFetch } from "./utils";
import { removeUserFolder } from "./session";

//TYPES

const SET_FOLDER = "folders/getFolder";
const DELETE_FOLDER = "folders/deleteFolder";
const CREATE_FOLDER = "folders/createFolder";

//actions

const setFolder = (folder) => {
  return { type: SET_FOLDER, payload: folder };
};

const addFolder = (folder) => ({
  type: CREATE_FOLDER,
  payload: folder,
});

const removeFolder = (folderId) => {
  return {
    type: DELETE_FOLDER,
    payload: folderId,
  };
};

//thunks

export const getFolder = (id) => async (dispatch) => {
  const response = await qFetch(`/api/folders/${id}`);

  if (response.ok) {
    let data = await response.json();
    dispatch(setFolder(data));
  }
};

export const createFolder = (folder) => async (dispatch) => {
  const response = await qFetch("/api/folders/", {
    method: "POST",
    body: JSON.stringify(folder),
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(setFolder(data));
    return data;
  }
};

export const deleteFolder = (folderId) => async (dispatch) => {
  const response = await qFetch(`/api/folders/${folderId}`, {
    method: "DELETE",
  });
  if (response.ok) {
    dispatch(removeFolder(folderId));
    dispatch(removeUserFolder(folderId));
  }
};

export const editFolder = (folder) => async (dispatch) => {
  const response = await qFetch(`/api/folders/${folder.id}`, {
    method: "PUT",
    body: JSON.stringify(folder),
  });

  if (response.ok) {
    let data = await response.json();
    dispatch(setFolder(data));
  }
};

//reducer
let initialState = { singleFolder: null };

export default function reducer(state = initialState, action) {
  switch (action.type) {
    case SET_FOLDER:
      return { ...state, singleFolder: action.payload };
    case DELETE_FOLDER:
      return { singleFolder: null };
    default:
      return state;
  }
}
