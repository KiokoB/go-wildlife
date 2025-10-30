// import React, { useEffect, useState } from "react";
// import { Switch, Route } from "react-router-dom";

// function App() {
//   return <h1>Project Client</h1>;
// }

// export default App;
import React from "react";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Navbar from "./components/Navbar";
import AnimalList from "./components/AnimalList";
import KeeperList from "./components/KeeperList";
import SpeciesList from "./components/SpeciesList";
import DietList from "./components/DietList";
import EnclosureList from "./components/EnclosureList";

function App() {
  return (
    <Router>
      <Navbar />
      <div className="container" style={{ padding: "20px" }}>
        <Routes>
          <Route path="/" element={<AnimalList />} />
          <Route path="/keepers" element={<KeeperList />} />
          <Route path="/species" element={<SpeciesList />} />
          <Route path="/diets" element={<DietList />} />
          <Route path="/enclosures" element={<EnclosureList />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;

