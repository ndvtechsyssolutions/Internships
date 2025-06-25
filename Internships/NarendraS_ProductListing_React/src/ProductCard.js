import React from 'react'

const ProductCard = ({product}) => {
    return(
        <div className="product-card">
            <img src={product.image} alt={product.name} />
            <h2>{product.name}</h2>
            <p>{product.description}</p>
            <div>
                <span className='price'>₹ {product.price}</span><br/><br/>
                <span className='rating'>⭐ {product.rating}</span>
            </div>
        </div>
    )
}

export default ProductCard;