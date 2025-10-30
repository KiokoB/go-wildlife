import React, { useEffect, useState } from "react";
import axios from "axios";

function EnclosureList() {
    const [enclosures, setEnclosures] = useState([]);

    useEffect(() => {
        axios.get("http://127.0.0.1:4444/enclosures")
            .then((res) => setEnclosures(res.data))
            .catch((err) => console.error(err));
    }, []);

    return (
        <div>
            <h2>🏠 Enclosures</h2>
            <table border="1" cellPadding="8" style={{ width: "100%", marginTop: "15px" }}>
                <thead style={{ backgroundColor: "#b6e0c7ff" }}>
                    <tr>
                        <th>ID</th>
                        <th>Type</th>
                        <th>Location</th>
                    </tr>
                </thead>
                <tbody>
                    {enclosures.map((e) => (
                        <tr key={e.id}>
                            <td>{e.id}</td>
                            <td>{e.enclosure_type}</td>
                            <td>{e.location}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default EnclosureList;
