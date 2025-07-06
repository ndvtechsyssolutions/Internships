// App.js
import React, { useState } from 'react';
import productsData from './products';
import ProductCard from './components/ProductCard';
import './App.css';

function App() {
  const [search, setSearch] = useState('');
  const [filterCategory, setFilterCategory] = useState('All');

  const filteredProducts = productsData.filter(product => {
    return (
      (filterCategory === 'All' || product.category === filterCategory) &&
      product.name.toLowerCase().includes(search.toLowerCase())
    );
  });

  return (
    <div className="App">
      <h1>Product Listing Page</h1>

      <input
        type="text"
        placeholder="Search by name"
        value={search}
        onChange={e => setSearch(e.target.value)}
      />

      <select onChange={e => setFilterCategory(e.target.value)} value={filterCategory}>
        <option value="All">All</option>
        <option value="Electronics">Electronics</option>
        <option value="Mobiles">Mobiles</option>
        <option value="Fashion">Fashion</option>
      </select>

      <div className="product-grid">
        {filteredProducts.map(product => (
          <ProductCard key={product.id} product={product} />
        ))}
      </div>
    </div>
  );
}

export default App;
