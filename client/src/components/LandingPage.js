import React from "react";
import { Link } from "react-router-dom";

function LandingPage() {
    const pageStyle = {
        textAlign: "center",
        backgroundColor: "#f0fdf4",
        minHeight: "100vh",
        display: "flex",
        flexDirection: "column",
        justifyContent: "center",
        alignItems: "center",
        color: "#065f46",
        fontFamily: "Segoe UI, sans-serif",
    };

    const buttonStyle = {
        backgroundColor: "#16a34a",
        color: "white",
        border: "none",
        padding: "10px 20px",
        fontSize: "18px",
        borderRadius: "10px",
        cursor: "pointer",
        textDecoration: "none",
    };

    const imageStyle = {
        width: "80%",
        maxWidth: "900px",
        borderRadius: "20px",
        marginTop: "20px",
        boxShadow: "0 4px 20px rgba(0,0,0,0.3)",
    };

    return (
        <div style={pageStyle}>
            <h1>🌿 Welcome to Go Wild Wildlife Park!</h1>
            <p style={{ fontSize: "18px", margin: "10px 0" }}>
                Explore the animals, their habitats, and the amazing team that cares for them.
            </p>
            <img
                src="https://images.unsplash.com/photo-1508672019048-805c876b67e2?auto=format&fit=crop&w=1350&q=80"
                alt="Wildlife"
                style={imageStyle}
            />
            <div style={{ marginTop: "30px" }}>
                <Link to="/animals" style={buttonStyle}>
                    🦓 Explore Animals
                </Link>
            </div>
        </div>
    );
}

export default LandingPage;
