import React, { useState, useEffect } from 'react';
import ProductsDisplay from './ProductsDisplay';

const Api = "https://fakestoreapi.com/products";

const Products = () => {
  const [productsDetails, setProductDetails] = useState([]);

  const productHandler = async () => {
    try {
      const response = await fetch(Api);
      if (!response.ok) throw new Error('Failed to fetch products');
      const newData = await response.json();
      setProductDetails(newData);
    } catch (error) {
      console.error('Error fetching products:', error);
    }
  };

  useEffect(() => {
    productHandler();
  }, []);

  return (
    <div>
      <h1>Products</h1>
      <div className="products-container">
        {productsDetails.map((item) => (
          <ProductsDisplay
            key={item.id}
            image={item.image}
            title={item.title}
            description={item.description}
            category={item.category}
            price={item.price}
            rating={item.rating.rate}
            count={item.rating.count}
          />
        ))}
      </div>
    </div>
  );
};

export default Products;