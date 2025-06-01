
import '../App.css';

const ProductCard = ({ product }) => {
  return (
    <div className="product-card">
      <img src={product.image} alt={product.title} />
      <div className="details">
        <div className="title">{product.title}</div>
        <div className="category">{product.category}</div>
        <div className="price">${product.price}</div>
      </div>
    </div>
  );
};

export default ProductCard;
