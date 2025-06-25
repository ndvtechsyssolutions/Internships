import React from 'react';

const FilterOptions = ({ categories, selected, setSelected }) => (
  <select
    value={selected}
    onChange={e => setSelected(e.target.value)}
    className="filter"
  >
    <option value="">All Categories</option>
    {categories.map(cat => (
      <option key={cat} value={cat}>{cat}</option>
    ))}
  </select>
);

export default FilterOptions;
