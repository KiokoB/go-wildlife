// import React, { useEffect, useState } from "react";
// import { Switch, Route } from "react-router-dom";

// function App() {
//   return <h1>Project Client</h1>;
// }

// export default App;
import React from "react";
import { BrowserRouter as Router, Switch, Route } from "react-router-dom"; // v5 syntax
import Navbar from './Navbar';
import LandingPage from "./LandingPage";
import AnimalList from "./AnimalList";
import KeeperList from "./KeeperList";
import SpeciesList from "./SpeciesList";
import DietList from "./DietList";
import EnclosureList from "./EnclosureList";


function App() {
  return (
    <Router>
      <Navbar />
      <Switch>
        <Route exact path="/" component={LandingPage} />
        <Route path="/animals" component={AnimalList} />
        <Route path="/keepers" component={KeeperList} />
        <Route path="/species" component={SpeciesList} />
        <Route path="/diets" component={DietList} />
        <Route path="/enclosures" component={EnclosureList} />
      </Switch>
    </Router>
  );
}


export default App;

