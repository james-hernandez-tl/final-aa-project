import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Routes } from "react-router-dom";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";
import Home from "./components/Home";
import LoginPage from "./components/LoginPage";
import SetSingleView from "./components/SetSingleView";
import SetFormDecider from "./components/SetFormDecider";
import YourSets from "./components/YourSets";
import YourFolders from "./components/YourFolders";
import FolderSingleView from "./components/FolderSingleView";
import SignUpPage from "./components/SignUpPage";
import Search from "./components/Search";
import Footer from "./components/Footer";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);
  return (
    <>
      <Navigation isLoaded={isLoaded} />

      {isLoaded && (
        <Routes>
          <Route path="/" exact element={<Home />} />
          <Route path="/logIn" element={<LoginPage />} />
          <Route path="/sets/new" exact element={<SetFormDecider />} />
          <Route path="/sets/:setId/edit" exact element={<SetFormDecider />} />
          <Route path="/sets/:setId" exact element={<SetSingleView />} />
          <Route path="/sets" exact element={<YourSets />} />
          <Route path="/folders" exact element={<YourFolders />} />
          <Route
            path="/folders/:folderId"
            exact
            element={<FolderSingleView />}
          />
          <Route path="/SignUp" exact element={<SignUpPage />} />
          <Route path="/Search" exact element={<Search />} />
        </Routes>
      )}
      {isLoaded && <Footer />}
    </>
  );
}

export default App;
