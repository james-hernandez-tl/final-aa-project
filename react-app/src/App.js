import React, { useState, useEffect } from "react";
import { useDispatch, useSelector } from "react-redux";
import { Route, Routes } from "react-router-dom";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";
import Home from "./components/Home";
import LoginPage from "./components/LoginPage";
import SetForm from "./components/SetForm";
import SetSingleView from "./components/SetSingleView";
import SetFormDecider from "./components/SetFormDecider";
import YourSets from "./components/YourSets";
import YourFolders from "./components/YourFolders";
import FolderSingleView from "./components/FolderSingleView";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  const set = useSelector((state) => state.sets.singleSet);

  return (
    <>
      <Navigation isLoaded={isLoaded} />

      <Routes>
        <Route path="/" exact={"True"} element={<Home />} />
        <Route path="/logIn" element={<LoginPage />} />
        <Route path="/sets/new" exact={"True"} element={<SetFormDecider />} />
        <Route
          path="/sets/:setId/edit"
          exact={"True"}
          element={<SetFormDecider />}
        />
        <Route path="/sets/:setId" exact={"True"} element={<SetSingleView />} />
        <Route path="/sets" exact={"True"} element={<YourSets />} />
        <Route path="/folders" exact={"True"} element={<YourFolders />} />
        <Route
          path="/folders/:folderId"
          exact={"True"}
          element={<FolderSingleView />}
        />
      </Routes>
    </>
  );
}

export default App;
