import { qFetch } from "./utils";

//TYPES

const QUIZME = "aiChat/quizMe";
const CHAT = "aiChat/chat";

//ACTIONS

export const setMessages = (messages) => {
  return {
    type: QUIZME,
    payload: messages,
  };
};

//THUNKS

export const quizMe = (setId) => async (dispatch) => {
  const response = await qFetch(`/api/openai/quiz/${setId}`, {
    method: "POST",
  });

  if (response.ok) {
    let data = await response.json();
    console.log(data);
    dispatch(setMessages(data));
  }
};

export const teachMe = (setId) => async (dispatch) => {
  const response = await qFetch(`/api/openai/quiz/${setId}/teach`, {
    method: "POST",
  });

  if (response.ok) {
    let data = await response.json();
    console.log(data);
    dispatch(setMessages(data));
  }
};

export const chat = (messages) => async (dispatch) => {
  const response = await qFetch(`/api/openai/chat`, {
    method: "POST",
    body: JSON.stringify({ pastMessages: messages }),
  });

  if (response.ok) {
    let data = await response.json();
    console.log(data);
    dispatch(setMessages(data));
  }
};

//reducer

let initialState = [];

export default function reducer(state = initialState, action) {
  switch (action.type) {
    case QUIZME:
      return action.payload;
    default:
      return state;
  }
}
