import React, { useEffect, useState } from "react";

function ProductListingPage() {
  const [products, setProducts] = useState([]);
  const [searchText, setSearchText] = useState("");
  const [category, setCategory] = useState("All");
  const [sortOrder, setSortOrder] = useState("asc");

  useEffect(() => {
    fetch("https://fakestoreapi.com/products")
      .then((res) => res.json())
      .then((data) => setProducts(data));
  }, []);

  const categories = ["All", ...new Set(products.map((p) => p.category))];

  const filtered = products
    .filter((product) =>
      (category === "All" || product.category === category) &&
      product.title.toLowerCase().includes(searchText.toLowerCase())
    )
    .sort((a, b) =>
      sortOrder === "asc" ? a.price - b.price : b.price - a.price
    );

  return (
    <div style={{ padding: "20px", fontFamily: "Arial" }}>
      <h1>Products</h1>

      {/* Controls */}
      <div style={{ marginBottom: "20px" }}>
        <input
          type="text"
          placeholder="Search products..."
          value={searchText}
          onChange={(e) => setSearchText(e.target.value)}
          style={{ marginRight: "10px" }}
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
          <option value="asc">Low to High</option>
          <option value="desc">High to Low</option>
        </select>
      </div>

      {/* Product Cards */}
      <div style={{ display: "flex", flexWrap: "wrap", gap: "20px" }}>
        {filtered.map((product) => (
          <div
            key={product.id}
            style={{
              border: "1px solid #ccc",
              padding: "10px",
              width: "200px",
            }}
          >
            <img
              src={product.image}
              alt={product.title}
              style={{ width: "100%", height: "150px", objectFit: "contain" }}
            />
            <h4>{product.title}</h4>
            <p>{product.category}</p>
            <p><strong>${product.price.toFixed(2)}</strong></p>
          </div>
        ))}
      </div>
    </div>
  );
}

export default ProductListingPage;

  

