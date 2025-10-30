import React from "react";
import { Link } from "react-router-dom";

function Navbar() {
    const navStyle = {
        backgroundColor: "#065f46",
        padding: "15px",
        display: "flex",
        justifyContent: "center",
        gap: "30px",
    };

    const linkStyle = {
        color: "white",
        textDecoration: "none",
        fontWeight: "bold",
        fontSize: "16px",
    };

    return (
        <nav style={navStyle}>
            <Link to="/" style={linkStyle}>Home</Link>
            <Link to="/animals" style={linkStyle}>Animals</Link>
            <Link to="/keepers" style={linkStyle}>Keepers</Link>
            <Link to="/species" style={linkStyle}>Species</Link>
            <Link to="/diets" style={linkStyle}>Diets</Link>
            <Link to="/enclosures" style={linkStyle}>Enclosures</Link>
        </nav>
    );
}

export default Navbar;

