import { qFetch } from "./utils";
import { removeUserFolder } from "./session";
import { editUserFolder } from "./session";

//TYPES

const SET_FOLDER = "folders/getFolder";
const DELETE_FOLDER = "folders/deleteFolder";

//actions

const setFolder = (folder) => {
  return { type: SET_FOLDER, payload: folder };
};

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

export const addSetToFolder = (folderId, setId) => async (dispatch) => {
  const response = await qFetch(`/api/folders/${folderId}/sets/${setId}`, {
    method: "POST",
  });
  if (response.ok) {
    const data = await response.json();
    dispatch(setFolder(data));
    dispatch(editUserFolder({ ...data, NumSets: data.Sets.length }));
  }
};

export const removeSetFromFolder = (folderId, setId) => async (dispatch) => {
  const response = await qFetch(`/api/folders/${folderId}/sets/${setId}`, {
    method: "DELETE",
  });
  if (response.ok) {
    const data = await response.json();
    dispatch(setFolder(data));
    dispatch(editUserFolder({ ...data, NumSets: data.Sets.length }));
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
