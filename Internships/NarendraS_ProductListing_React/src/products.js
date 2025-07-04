const products = [
    {
        "id": 1,
        "name": "Sony WH-1000XM4",
        "price": 29999,
        "category": "Electronics",
        "description": "Industry leading noise canceling headphones.",
        "image": "https://m.media-amazon.com/images/I/71o8Q5XJS5L._SL1500_.jpg",
        "rating": 4.8
    },
    {
        "id": 2,
        "name": "Apple iPhone 13",
        "price": 64999,
        "category": "Electronics",
        "description": "Apple's iPhone 13 with A15 Bionic chip.",
        "image": "https://m.media-amazon.com/images/I/71GLMJ7TQiL._SL1500_.jpg",
        "rating": 4.6
    },
    {
        "id": 3,
        "name": "Nike Air Max 270",
        "price": 11999,
        "category": "Footwear",
        "description": "Men's running shoes with responsive cushioning.",
        "image": "https://m.media-amazon.com/images/I/71ID+VZskdL._UL1500_.jpg",
        "rating": 4.5
    },
    {
        "id": 4,
        "name": "Samsung Galaxy Watch 5",
        "price": 28999,
        "category": "Electronics",
        "description": "Smartwatch with fitness tracking and AMOLED display.",
        "image": "https://m.media-amazon.com/images/I/61v2V+o8AQL._SL1500_.jpg",
        "rating": 4.4
    },
    {
        "id": 5,
        "name": "Adidas Running Shoes",
        "price": 4999,
        "category": "Footwear",
        "description": "Lightweight and breathable running shoes.",
        "image": "https://m.media-amazon.com/images/I/71QeG6-XIuL._UL1500_.jpg",
        "rating": 4.3
    },
    {
        "id": 6,
        "name": "Canon EOS 200D II",
        "price": 55999,
        "category": "Electronics",
        "description": "DSLR camera with 24.1MP CMOS sensor.",
        "image": "https://m.media-amazon.com/images/I/914hFeTU2-L._SL1500_.jpg",
        "rating": 4.7
    },
    {
        "id": 7,
        "name": "Amazon Echo Dot 4th Gen",
        "price": 3499,
        "category": "Electronics",
        "description": "Smart speaker with Alexa.",
        "image": "https://m.media-amazon.com/images/I/6182S7MYC2L._SL1000_.jpg",
        "rating": 4.5
    },
    {
        "id": 8,
        "name": "Puma Sports T-Shirt",
        "price": 1299,
        "category": "Clothing",
        "description": "Men's dry-fit activewear.",
        "image": "https://m.media-amazon.com/images/I/71vU0zBUXgL._UL1500_.jpg",
        "rating": 4.2
    },
    {
        "id": 9,
        "name": "Roadster Denim Jacket",
        "price": 2499,
        "category": "Clothing",
        "description": "Stylish and rugged denim jacket.",
        "image": "https://m.media-amazon.com/images/I/91aQW0WPO7L._UL1500_.jpg",
        "rating": 4.1
    },
    {
        "id": 10,
        "name": "Levi's Slim Fit Jeans",
        "price": 2299,
        "category": "Clothing",
        "description": "Men's slim fit stretchable jeans.",
        "image": "https://m.media-amazon.com/images/I/71mNyt0pKyL._UL1500_.jpg",
        "rating": 4.3
    },
    {
        "id": 11,
        "name": "Samsung 50 inch Smart TV",
        "price": 45999,
        "category": "Electronics",
        "description": "4K UHD LED Smart TV with HDR.",
        "image": "https://m.media-amazon.com/images/I/91TfiRzg-LL._SL1500_.jpg",
        "rating": 4.6
    },
    {
        "id": 12,
        "name": "Mi Band 6",
        "price": 3499,
        "category": "Electronics",
        "description": "Fitness tracker with AMOLED display.",
        "image": "https://m.media-amazon.com/images/I/61epn29QG0L._SL1500_.jpg",
        "rating": 4.2
    },
    {
        "id": 13,
        "name": "Fossil Analog Watch",
        "price": 7999,
        "category": "Accessories",
        "description": "Stylish analog watch with leather strap.",
        "image": "https://m.media-amazon.com/images/I/71wnWcvoL5L._UL1500_.jpg",
        "rating": 4.4
    },
    {
        "id": 14,
        "name": "Wildcraft Backpack",
        "price": 2199,
        "category": "Accessories",
        "description": "Water-resistant laptop backpack.",
        "image": "https://m.media-amazon.com/images/I/81ayXnWrVYL._UL1500_.jpg",
        "rating": 4.5
    },
    {
        "id": 15,
        "name": "Allen Solly Polo T-Shirt",
        "price": 1499,
        "category": "Clothing",
        "description": "Classic fit polo T-shirt for men.",
        "image": "https://m.media-amazon.com/images/I/71+4DZnylmL._UL1500_.jpg",
        "rating": 4.3
    },
    {
        "id": 16,
        "name": "Noise ColorFit Pulse",
        "price": 1999,
        "category": "Electronics",
        "description": "Smartwatch with heart rate monitor.",
        "image": "https://m.media-amazon.com/images/I/61epn29QG0L._SL1500_.jpg",
        "rating": 4.1
    },
    {
        "id": 17,
        "name": "HP Wireless Mouse",
        "price": 899,
        "category": "Electronics",
        "description": "Compact wireless mouse with USB receiver.",
        "image": "https://m.media-amazon.com/images/I/61l9ppRIiqL._SL1500_.jpg",
        "rating": 4.3
    },
    {
        "id": 18,
        "name": "Dell Inspiron Laptop",
        "price": 52999,
        "category": "Electronics",
        "description": "15.6 inch FHD laptop with 11th Gen i5 processor.",
        "image": "https://m.media-amazon.com/images/I/71D9ImsvEtL._SL1500_.jpg",
        "rating": 4.4
    },
    {
        "id": 19,
        "name": "Bata Formal Shoes",
        "price": 2499,
        "category": "Footwear",
        "description": "Men's leather formal shoes.",
        "image": "https://m.media-amazon.com/images/I/71j+1FvFo2L._UL1500_.jpg",
        "rating": 4.0
    },
    {
        "id": 20,
        "name": "Reebok Gym Bag",
        "price": 1799,
        "category": "Accessories",
        "description": "Durable gym bag with multiple compartments.",
        "image": "https://m.media-amazon.com/images/I/71xEDK-XMgL._UL1500_.jpg",
        "rating": 4.2
    }
];

export default products;