import React from "react";
import { Link } from "react-router-dom";

function Navbar() {
    const navStyle = {
        padding: "15px",
        backgroundColor: "#2f855a",
        color: "white",
        display: "flex",
        justifyContent: "space-around",
    };

    return (
        <nav style={navStyle}>
            <Link to="/" style={{ color: "white" }}>Animals</Link>
            <Link to="/keepers" style={{ color: "white" }}>Keepers</Link>
            <Link to="/species" style={{ color: "white" }}>Species</Link>
            <Link to="/diets" style={{ color: "white" }}>Diets</Link>
            <Link to="/enclosures" style={{ color: "white" }}>Enclosures</Link>
        </nav>
    );
}

export default Navbar;
