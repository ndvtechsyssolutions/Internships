import React from 'react';

const ProductCard = ({ product, onAddToCart }) => (
  <div className="product-card">
    <img className="product-image" src={product.image || product.imageUrl} alt={product.title || product.name} style={{ width: '100%', height: 120, objectFit: 'cover' }} />
    <h3>{product.title || product.name}</h3>
    {/* <p>Category: {product.category}</p> */}
    <p className='product-price'>Price: ${product.price}</p>
    <button className="add-to-cart-btn" onClick={() => onAddToCart(product)}>
      Add to Cart
    </button>
  </div>
);

export default ProductCard;
