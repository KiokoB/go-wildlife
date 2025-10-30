import React, { useEffect, useState } from "react";
import axios from "axios";

function AnimalList() {
    const [animals, setAnimals] = useState([]);

    useEffect(() => {
        axios.get("http://127.0.0.1:4444/animals")
            .then((res) => setAnimals(res.data))
            .catch((err) => console.error(err));
    }, []);

    return (
        <div>
            <h2>🐾 Animals in the Park</h2>
            <table border="1" cellPadding="8" style={{ width: "100%", marginTop: "15px" }}>
                <thead style={{ backgroundColor: "#d9f99d" }}>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Gender</th>
                        <th>Year of Arrival</th>
                        <th>Species</th>
                        <th>Diet</th>
                        <th>Keeper</th>
                        <th>Enclosure</th>
                    </tr>
                </thead>
                <tbody>
                    {animals.map((a) => (
                        <tr key={a.id}>
                            <td>{a.id}</td>
                            <td>{a.name}</td>
                            <td>{a.gender}</td>
                            <td>{a.year_of_arrival}</td>
                            <td>{a.species}</td>
                            <td>{a.diet}</td>
                            <td>{a.keeper}</td>
                            <td>{a.enclosure}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default AnimalList;
