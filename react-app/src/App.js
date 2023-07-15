import React, { useState, useEffect } from "react";
import { useDispatch } from "react-redux";
import { Route, Routes } from "react-router-dom";
import { authenticate } from "./store/session";
import Navigation from "./components/Navigation";
import Home from "./components/Home";
import LoginPage from "./components/LoginPage";
import SetForm from "./components/SetForm";

function App() {
  const dispatch = useDispatch();
  const [isLoaded, setIsLoaded] = useState(false);
  useEffect(() => {
    dispatch(authenticate()).then(() => setIsLoaded(true));
  }, [dispatch]);

  return (
    <>
      <Navigation isLoaded={isLoaded} />

      <Routes>
        <Route path="/" exact={"True"} element={<Home />} />
        <Route path="/logIn" element={<LoginPage />} />
        <Route path="/sets/new" exact={"True"} element={<SetForm />} />
      </Routes>
    </>
  );
}

export default App;
