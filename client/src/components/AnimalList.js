import React, { useEffect, useState } from "react";
import axios from "axios";

function AnimalList() {
    const [animals, setAnimals] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [newAnimal, setNewAnimal] = useState({
        name: "",
        gender: "",
        year_of_arrival: "",
        species_id: "",
        diet_id: "",
        keeper_id: "",
        enclosure_id: ""
    });

    // ✅ Fetch all animals
    useEffect(() => {
        fetchAnimals();
    }, []);

    const fetchAnimals = () => {
        axios.get("http://127.0.0.1:4444/animals")
            .then((res) => setAnimals(res.data))
            .catch((err) => setError(err.message))
            .finally(() => setLoading(false));
    };

    // ✅ Handle delete
    const handleDelete = (id) => {
        axios.delete(`http://127.0.0.1:4444/animals/${id}`)
            .then(() => {
                setAnimals(animals.filter(a => a.id !== id));
            })
            .catch((err) => alert("Failed to delete: " + err.message));
    };

    // ✅ Handle input changes for new animal
    const handleChange = (e) => {
        setNewAnimal({ ...newAnimal, [e.target.name]: e.target.value });
    };

    // ✅ Handle adding new animal
    const handleAddAnimal = (e) => {
        e.preventDefault();
        axios.post("http://127.0.0.1:4444/animals", newAnimal)
            .then((res) => {
                setAnimals([...animals, res.data]);
                setNewAnimal({
                    name: "",
                    gender: "",
                    year_of_arrival: "",
                    species: "",
                    diet: "",
                    keeper: "",
                    enclosure: ""
                });
            })
            .catch((err) => alert("Failed to add: " + err.message));
    };

    if (loading) return <p>Loading animals...</p>;
    if (error) return <p style={{ color: "red" }}>Error: {error}</p>;

    return (
        <div style={{ padding: "20px" }}>
            <h2>🐾 Animals in the Park</h2>

            {/* 🐣 Add Animal Form */}
            <form onSubmit={handleAddAnimal} style={{ marginBottom: "20px" }}>
                <h3>Add New Animal</h3>
                <div style={{ display: "grid", gridTemplateColumns: "repeat(4, 1fr)", gap: "10px" }}>
                    <input name="name" value={newAnimal.name} onChange={handleChange} placeholder="Name" required />
                    <input name="gender" value={newAnimal.gender} onChange={handleChange} placeholder="Gender" />
                    <input name="year_of_arrival" value={newAnimal.year_of_arrival} onChange={handleChange} placeholder="Year of Arrival" />
                    <input name="species_id" value={newAnimal.species_id} onChange={handleChange} placeholder="Species ID" />
                    <input name="diet_id" value={newAnimal.diet_id} onChange={handleChange} placeholder="Diet" />
                    <input name="keeper_id" value={newAnimal.keeper_id} onChange={handleChange} placeholder="Keeper" />
                    <input name="enclosure_id" value={newAnimal.enclosure_id} onChange={handleChange} placeholder="Enclosure" />
                    <button type="submit" style={{ gridColumn: "span 4", backgroundColor: "#86efac", border: "none", padding: "8px", cursor: "pointer" }}>
                        ➕ Add Animal
                    </button>
                </div>
            </form>

            {/* 🐾 Animal Table */}
            <table border="1" cellPadding="8" style={{ width: "100%", marginTop: "15px", borderCollapse: "collapse" }}>
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
                        <th>Actions</th>
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
                            <td>
                                <button
                                    onClick={() => handleDelete(a.id)}
                                    style={{ backgroundColor: "#f87171", color: "white", border: "none", padding: "5px", cursor: "pointer" }}
                                >
                                    🗑 Delete
                                </button>
                            </td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
}

export default AnimalList;
