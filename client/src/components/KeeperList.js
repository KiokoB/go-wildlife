import React, { useEffect, useState } from "react";
import axios from "axios";

function KeeperList() {
    const [keepers, setKeepers] = useState([]);

    useEffect(() => {
        axios.get("http://127.0.0.1:4444/keepers")
            .then((res) => setKeepers(res.data))
            .catch((err) => console.error(err));
    }, []);

    return (
        <div>
            <h2>🧍‍♂️ Keepers</h2>
            <table border="1" cellPadding="8" style={{ width: "100%", marginTop: "15px" }}>
                <thead style={{ backgroundColor: "#fef9c3" }}>
                    <tr>
                        <th>ID</th>
                        <th>Name</th>
                        <th>Date of Birth</th>
                        <th>Rank</th>
                    </tr>
                </thead>
                <tbody>
                    {keepers.map((k) => (
                        <tr key={k.id}>
                            <td>{k.id}</td>
                            <td>{k.name}</td>
                            <td>{k.date_of_birth}</td>
                            <td>{k.rank}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default KeeperList;
