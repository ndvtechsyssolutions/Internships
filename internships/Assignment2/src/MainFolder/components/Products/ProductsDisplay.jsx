import React from 'react';
import ShoppingCartIcon from '@mui/icons-material/ShoppingCart';
import FavoriteIcon from '@mui/icons-material/Favorite';
import { Box, Button } from '@mui/material';
import Buttons from './Buttons';
import WishlistButton from './wishlistButton';

const ProductsDisplay = ({ image, title, description, category, price, rating, count }) => {
  return (
    <div className="product-card">
      <div>
        <img src={image} alt={title} />
      </div>
      <h3>{title}</h3>
      <p className="category">{category}</p>
      <p className="description">{description.slice(0, 100)}...</p>
      <p className="price">${price}</p>
      <p>Rating: {rating} ({count} reviews)</p>
      <Box>
        <Buttons />
      </Box>
    </div>
  );
};

export default ProductsDisplay;