import React, { useEffect, useState } from "react";

function App() {
  const [products, setProducts] = useState([]);
  const [searchText, setSearchText] = useState("");
  const [category, setCategory] = useState("All");
  const [sortOrder, setSortOrder] = useState("asc");

  // Custom home appliances products to add
  const customHomeAppliances = [
    {
      id: 1001,
      title: "Air Conditioner",
      price: 499.99,
      category: "home appliances",
      image:
        "https://cdn-icons-png.flaticon.com/512/684/684908.png",
    },
    {
      id: 1002,
      title: "Microwave Oven",
      price: 149.99,
      category: "home appliances",
      image:
        "https://cdn-icons-png.flaticon.com/512/2972/2972185.png",
    },
    {
      id: 1003,
      title: "Vacuum Cleaner",
      price: 199.99,
      category: "home appliances",
      image:
        "https://cdn-icons-png.flaticon.com/512/2965/2965567.png",
    },
  ];

  useEffect(() => {
    fetch("https://fakestoreapi.com/products")
      .then((res) => res.json())
      .then((data) => {
        // Combine API data + custom home appliances
        setProducts([...data, ...customHomeAppliances]);
      });
  }, []);

  // Get unique categories + "All"
  const categories = ["All", ...new Set(products.map((p) => p.category))];

  // Filter and sort products
  const filteredProducts = products
    .filter(
      (product) =>
        (category === "All" || product.category === category) &&
        product.title.toLowerCase().includes(searchText.toLowerCase())
    )
    .sort((a, b) =>
      sortOrder === "asc" ? a.price - b.price : b.price - a.price
    );

  return (
    <div
      style={{
        maxWidth: "1200px",
        margin: "0 auto",
        padding: "20px",
        fontFamily: "Arial, sans-serif",
        textAlign: "center",
      }}
    >
      <h1>Welcome to Product Listing of ShopGo</h1>

      {/* Controls */}
      <div
        style={{
          marginBottom: "30px",
          display: "flex",
          justifyContent: "center",
          gap: "15px",
          flexWrap: "wrap",
        }}
      >
        <input
          type="text"
          placeholder="Search products..."
          value={searchText}
          onChange={(e) => setSearchText(e.target.value)}
          style={{
            padding: "10px",
            width: "250px",
            fontSize: "16px",
            borderRadius: "5px",
            border: "1px solid #ccc",
          }}
        />

        <select
          value={category}
          onChange={(e) => setCategory(e.target.value)}
          style={{
            padding: "10px",
            fontSize: "16px",
            borderRadius: "5px",
            border: "1px solid #ccc",
          }}
        >
          {categories.map((cat) => (
            <option key={cat} value={cat}>
              {cat.charAt(0).toUpperCase() + cat.slice(1)}
            </option>
          ))}
        </select>

        <select
          value={sortOrder}
          onChange={(e) => setSortOrder(e.target.value)}
          style={{
            padding: "10px",
            fontSize: "16px",
            borderRadius: "5px",
            border: "1px solid #ccc",
          }}
        >
          <option value="asc">Price: Low to High</option>
          <option value="desc">Price: High to Low</option>
        </select>
      </div>

      {/* Products grid */}
      <div
        style={{
          display: "grid",
          gridTemplateColumns: "repeat(auto-fill,minmax(220px,1fr))",
          gap: "25px",
          justifyItems: "center",
        }}
      >
        {filteredProducts.length === 0 ? (
          <p>No products found.</p>
        ) : (
          filteredProducts.map((product) => (
            <div
              key={product.id}
              style={{
                border: "1px solid #ddd",
                borderRadius: "10px",
                padding: "15px",
                maxWidth: "220px",
                textAlign: "center",
                boxShadow: "0 2px 5px rgba(0,0,0,0.1)",
                backgroundColor: "#fff",
              }}
            >
              <img
                src={product.image}
                alt={product.title}
                style={{ height: "150px", objectFit: "contain", marginBottom: "10px" }}
              />
              <h4
                style={{
                  fontSize: "16px",
                  height: "48px",
                  overflow: "hidden",
                  marginBottom: "8px",
                }}
                title={product.title}
              >
                {product.title}
              </h4>
              <p style={{ color: "#666", marginBottom: "6px", fontStyle: "italic" }}>
                {product.category.charAt(0).toUpperCase() + product.category.slice(1)}
              </p>
              <p style={{ fontWeight: "bold", fontSize: "18px", color: "#2a9d8f" }}>
                ${product.price.toFixed(2)}
              </p>
            </div>
          ))
        )}
      </div>
    </div>
  );
}

export default App;
