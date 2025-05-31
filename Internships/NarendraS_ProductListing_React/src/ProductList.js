import React, {useState, useEffect } from 'react';
import ProductCard from './ProductCard';
import './App.css';

const ProductList = () => {
    const [products, setProducts] = useState([]);
    const [filtered, setFiltered] = useState([]);
    const [search, setSearch] = useState('');
    const [category, setCategory] = useState('');
    const [sort, setSort] = useState('');

    useEffect(() => {
        fetch('/products.json')
        .then(res => res.json())
        .then(data => {
            setProducts(data);
            setFiltered(data);
        });
    }, []);

    useEffect(() => {
        let temp = [...products];

        if(search){
            temp = temp.filter(p => p.name.toLowerCase().includes(search.toLowerCase()));
        }

        if(category){
            temp = temp.filter(p => p.category === category);
        }

        if(sort === 'price'){
            temp.sort((a,b) => a.price - b.price);
        }else if(sort === 'name'){
            temp.sort((a,b) => a.name.localeCompare(b.name));
        }

        setFiltered(temp);
    },[search,category,sort,products]);

    return(
        <div>
            <div className='controls'>
                <input type='text' placeholder='Search by name' onChange={(e)=> setSearch(e.target.value)}/>
                <select onChange={(e)=>setCategory(e.target.value)}>
                    <option value="">All Categories</option>
                    <option value="Electronics">Electronics</option>
                    <option value="Footwear">Footwear</option>
                    <option value="Clothing">Clothing</option>
                    <option value="Accessories">Accessories</option>
                </select>
                <select onChange={(e)=>setSort(e.target.value)}>
                    <option value="">Sort By</option>
                    <option value="price">Price</option>
                    <option value="name">Name</option>
                </select>
            </div>
            <div className='product-grid'>
                {filtered.map(product => (
                    <ProductCard key={product.id} product={product} />
                ))}
            </div>
        </div>
    );
};

export default ProductList;