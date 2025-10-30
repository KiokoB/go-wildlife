import React, { useEffect, useState } from "react";
import axios from "axios";

function SpeciesList() {
    const [species, setSpecies] = useState([]);

    useEffect(() => {
        axios.get("http://127.0.0.1:4444/species")
            .then((res) => setSpecies(res.data))
            .catch((err) => console.error(err));
    }, []);

    return (
        <div>
            <h2>🐅 Species</h2>
            <table border="1" cellPadding="8" style={{ width: "100%", marginTop: "15px" }}>
                <thead style={{ backgroundColor: "#f8f1d0ff" }}>
                    <tr>
                        <th>ID</th>
                        <th>Type</th>
                        <th>Group</th>
                        <th>Lifestyle</th>
                        <th>Conservation Status</th>
                    </tr>
                </thead>
                <tbody>
                    {species.map((s) => (
                        <tr key={s.id}>
                            <td>{s.id}</td>
                            <td>{s.species_type}</td>
                            <td>{s.species_group}</td>
                            <td>{s.lifestyle}</td>
                            <td>{s.conservation_status}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default SpeciesList;
