// constants
const SET_USER = "session/SET_USER";
const REMOVE_USER = "session/REMOVE_USER";
const ADD_USER_SET = "session/ADD_USER_SET";
const EDIT_USER_SET = "session/EDIT_USER_SET";
const REMOVE_USER_FOLDER = "session/REMOVE_USER_FOLDER";
const REMOVE_USER_SET = "session/REMOVE_USER_SET";

const setUser = (user) => ({
  type: SET_USER,
  payload: user,
});

const removeUser = () => ({
  type: REMOVE_USER,
});

export const addUserSet = (set) => ({
  type: ADD_USER_SET,
  payload: set,
});

export const removeUserFolder = (folderId) => ({
  type: REMOVE_USER_FOLDER,
  payload: folderId,
});

export const removeUserSet = (setId) => {
  return {
    type: REMOVE_USER_SET,
    payload: setId,
  };
};

export const editUserSet = (set) => {
  return {
    type: EDIT_USER_SET,
    payload: set,
  };
};

const initialState = { user: null };

export const authenticate = () => async (dispatch) => {
  const response = await fetch("/api/auth/", {
    headers: {
      "Content-Type": "application/json",
    },
  });
  if (response.ok) {
    const data = await response.json();
    if (data.errors) {
      return;
    }

    dispatch(setUser(data));
  }
};

export const login = (username, password) => async (dispatch) => {
  const response = await fetch("/api/auth/login", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      username,
      password,
    }),
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(setUser(data));
    return null;
  } else if (response.status < 500) {
    const data = await response.json();
    if (data.errors) {
      return data.errors;
    }
  } else {
    return ["An error occurred. Please try again."];
  }
};

export const logout = () => async (dispatch) => {
  const response = await fetch("/api/auth/logout", {
    headers: {
      "Content-Type": "application/json",
    },
  });

  if (response.ok) {
    dispatch(removeUser());
  }
};

export const signUp = (username, email, password) => async (dispatch) => {
  const response = await fetch("/api/auth/signup", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      username,
      email,
      password,
    }),
  });

  if (response.ok) {
    const data = await response.json();
    dispatch(setUser(data));
    return null;
  } else if (response.status < 500) {
    const data = await response.json();
    if (data.errors) {
      return data.errors;
    }
  } else {
    return ["An error occurred. Please try again."];
  }
};

export default function reducer(state = initialState, action) {
  switch (action.type) {
    case SET_USER:
      return { user: action.payload };
    case REMOVE_USER:
      return { user: null };
    case ADD_USER_SET:
      return {
        user: {
          ...state.user,
          Sets: [...state.user.Sets, action.payload],
        },
      };
    case EDIT_USER_SET:
      return {
        user: {
          ...state.user,
          Sets: state.user.Sets.map((set) => {
            if (set.id === action.payload.id) {
              return action.payload;
            }
            return set;
          }),
        },
      };
    case REMOVE_USER_FOLDER:
      return {
        user: {
          ...state.user,
          Folders: state.user.Folders.filter(
            (folder) => folder.id !== action.payload
          ),
        },
      };
    case REMOVE_USER_SET:
      return {
        user: {
          ...state.user,
          Sets: state.user.Sets.filter((set) => set.id !== action.payload),
        },
      };
    default:
      return state;
  }
}
