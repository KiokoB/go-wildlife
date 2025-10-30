import React, { useEffect, useState } from "react";
import axios from "axios";

function DietList() {
    const [diets, setDiets] = useState([]);

    useEffect(() => {
        axios.get("http://127.0.0.1:4444/diets")
            .then((res) => setDiets(res.data))
            .catch((err) => console.error(err));
    }, []);

    return (
        <div>
            <h2>🥩 Diet Types</h2>
            <table border="1" cellPadding="8" style={{ width: "100%", marginTop: "15px" }}>
                <thead style={{ backgroundColor: "#fde68a" }}>
                    <tr>
                        <th>ID</th>
                        <th>Diet Type</th>
                        <th>Feeds per Day</th>
                    </tr>
                </thead>
                <tbody>
                    {diets.map((d) => (
                        <tr key={d.id}>
                            <td>{d.id}</td>
                            <td>{d.diet_type}</td>
                            <td>{d.feeds_per_day}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default DietList;
