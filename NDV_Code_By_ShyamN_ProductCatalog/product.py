<!DOCTYPE html>
<html lang="en">

<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Electronics Showcase</title>
  <style>
    * {
      box-sizing: border-box;
      margin: 0;
      padding: 0;
      font-family: 'Segoe UI', sans-serif;
    }

    body {
      background-color: #f0f0f0;
      padding: 20px;
    }

    header {
      text-align: center;
      margin-bottom: 30px;
    }

    header h1 {
      font-size: 2rem;
      color: #333;
    }

    .product-container {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
      gap: 20px;
    }

    .product-card {
      background: #fff;
      border-radius: 10px;
      padding: 16px;
      box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
      text-align: center;
    }

    .product-card img {
      width: 100%;
      height: 200px;
      object-fit: cover;
      border-radius: 8px;
    }

    .product-name {
      font-size: 1.1rem;
      margin: 10px 0;
      color: #444;
    }

    .product-price {
      color: #007acc;
      font-weight: bold;
      margin-bottom: 10px;
    }

    .add-button {
      background-color: #007acc;
      color: white;
      padding: 10px 16px;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }
  </style>
</head>

<body>

  <header>
    <h1>Electronics Showcase</h1>
  </header>

  <div class="product-container" id="productContainer"></div>

  <script>
    const products = [
      {
        name: "Wireless Headphones",
        price: "$59.99",
        imageUrl: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRnj4_GMgY6Lhv71LDZ1RsZqcNvKfHfPpTGeQ&s"
      },
      {
        name: "Smart Watch",
        price: "$129.99",
        imageUrl: "https://www.boat-lifestyle.com/cdn/shop/files/WaveSigma3_FIs_BlackMetal01_1200x1200_crop_center.png?v=1715601060"
      },
      {
        name: "Bluetooth Speaker",
        price: "$39.99",
        imageUrl: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTs3fXVy33V0nhWou3KhTEWyu66aEAW6BecQg&s"
      },
      {
        name: "DSLR Camera",
        price: "$599.99",
        imageUrl: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPxuQ4r6cvgCVgpK-lDXc1sfIX7Zbavssfeg&s"
      },
      {
        name: "Gaming Mouse",
        price: "$29.99",
        imageUrl: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRPk-XCJF5zLFTBj1J0a-qrrmYNoltMeN5qsQ&s"
      },
      {
        name: "Laptop",
        price: "$900.00",
        imageUrl: "https://m.media-amazon.com/images/I/61owpYGKjhL.jpg"
      },
      {
        name: "Smart TV",
        price: "$1200",
        imageUrl: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSAo3xHIrDeGnL00To3MJujIQ8KN7wzEi3ubA&s"
      },
      {
        name: "Air Conditioner",
        price: "$2000",
        imageUrl: "https://havells.com/media/catalog/product/cache/844a913d283fe95e56e39582c5f2767b/g/l/gls18v5fogvv_3__1.jpg"
      },
      {
        name: "Room Cooler",
        price: "$599.99",
        imageUrl: "https://havells.com/media/catalog/product/cache/844a913d283fe95e56e39582c5f2767b/g/h/ghracbke090_3_.jpg"
      },
      {
        name: "Tablet",
        price: "$1600",
        imageUrl: "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRS96jJnj4Nt3kN_j_oh0KPLdyubbPFKegh-g&s"
      }
    ];

    const container = document.getElementById("productContainer");

    products.forEach(item => {
      const card = document.createElement("div");
      card.className = "product-card";
      card.innerHTML = `
        <img src="${item.imageUrl}" alt="${item.name}">
        <h2 class="product-name">${item.name}</h2>
        <p class="product-price">${item.price}</p>
        <button class="add-button">Add to Cart</button>
      `;
      container.appendChild(card);
    });
  </script>

</body>

</html>
