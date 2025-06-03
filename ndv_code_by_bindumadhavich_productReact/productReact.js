
import React, { useState } from "react";
import products from "./products";

function App() {
  const [searchText, setSearchText] = useState("");
  const [category, setCategory] = useState("All");
  const [sortOrder, setSortOrder] = useState("asc");

  const categories = ["All", ...new Set(products.map((p) => p.category))];

  const filtered = products
    .filter(
      (product) =>
        (category === "All" || product.category === category) &&
        product.title.toLowerCase().includes(searchText.toLowerCase())
    )
    .sort((a, b) =>
      sortOrder === "asc" ? a.price - b.price : b.price - a.price
    );

  return (
    <div style={{ padding: "20px", fontFamily: "Arial", textAlign: "center" }}>
      <h1>Product Listing</h1>
      <div style={{ marginBottom: "20px" }}>
        <input
          type="text"
          placeholder="Search products..."
          value={searchText}
          onChange={(e) => setSearchText(e.target.value)}
          style={{ padding: "8px", width: "250px", marginRight: "10px" }}
        />
        <select value={category} onChange={(e) => setCategory(e.target.value)}>
          {categories.map((cat) => (
            <option key={cat}>{cat}</option>
          ))}
        </select>
        <select
          value={sortOrder}
          onChange={(e) => setSortOrder(e.target.value)}
          style={{ marginLeft: "10px" }}
        >
          <option value="asc">Price: Low to High</option>
          <option value="desc">Price: High to Low</option>
        </select>
      </div>
      <div style={{ display: "flex", flexWrap: "wrap", justifyContent: "center", gap: "20px" }}>
        {filtered.map((product) => (
          <div
            key={product.id}
            style={{
              border: "1px solid #ccc",
              borderRadius: "8px",
              padding: "10px",
              width: "200px",
              textAlign: "left",
            }}
          >
            <img
              src={product.image}
              alt={product.title}
              style={{ width: "100%", height: "150px", objectFit: "cover", borderRadius: "4px" }}
            />
            <h4>{product.title}</h4>
            <p style={{ fontSize: "14px", color: "#777" }}>{product.category}</p>
            <p style={{ fontWeight: "bold" }}>${product.price.toFixed(2)}</p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default App;
