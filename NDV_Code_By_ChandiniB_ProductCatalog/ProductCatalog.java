<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
  <title>Product Catalog</title>
  <link rel="stylesheet" href="ProductCatalog.css" />
</head>
<body>
  <header>
    Product Catalog
  </header>

  <main class="catalog">
    <!-- Row 1 -->
    <div class="product-card">
      <img src="data:image/jpeg;base64,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" >
      <h3 class="product-name">Product 1</h3>
      <p class="product-price">$19.99</p>
    </div>
    <div class="product-card">
      <img src="data:image/jpeg;base64,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" >
      <h3 class="product-name">Product 2</h3>
      <p class="product-price">$24.99</p>
    </div>
    <div class="product-card">
      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQyPM9n6Cizmh_-x663DF4Y9LZxxZzW9BrS_A&s" >
      <h3 class="product-name">Product 3</h3>
      <p class="product-price">$29.99</p>
    </div>

    <!-- Row 2 -->
    <div class="product-card">
      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQkK_mzAUvHCl_e3jg0Gh821Q0_Sd9HC9ADdg&s" >
      <h3 class="product-name">Product 4</h3>
      <p class="product-price">$15.99</p>
    </div>
    <div class="product-card">
      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSS-Icz8AmCHm91ZjR0Wg2j3_ALbnXIbsAPEg&s" >
      <h3 class="product-name">Product 5</h3>
      <p class="product-price">$12.49</p>
    </div>
    <div class="product-card">
      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQdkxuPvvFFtRRRb4UnOL1EUnWjWw7s9mbxEA&s" >
      <h3 class="product-name">Product 6</h3>
      <p class="product-price">$39.99</p>
    </div>

    <!-- Row 3 -->
    <div class="product-card">
      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcT8s55mipBvliLb8okKfiP8catLsp05uIRY9w&s" >
      <h3 class="product-name">Product 7</h3>
      <p class="product-price">$22.00</p>
    </div>
    <div class="product-card">
      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQltkDf1u3xe0mLA3w88vTyhKcvINTccMGeDw&s" >
      <h3 class="product-name">Product 8</h3>
      <p class="product-price">$30.00</p>
    </div>
    <div class="product-card">
      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQ_emX1J2kH7lHfbs7Il1y3Vjl6J717gPfamw&s" alt="Product 9">
      <h3 class="product-name">Product 9</h3>
      <p class="product-price">$9.99</p>
    </div>

    <!-- Row 4 -->
    <div class="product-card">
      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTj3uo2K-0MFaz1IwxL-Y3cuOZrhiFQmEh9nA&s" alt="Product 10">
      <h3 class="product-name">Product 10</h3>
      <p class="product-price">$49.99</p>
    </div>
    <div class="product-card">
      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQpjyxsSQT2UydwiZYGWTnyxwpWBqUHVQA8Lw&s" alt="Product 11">
      <h3 class="product-name">Product 11</h3>
      <p class="product-price">$5.99</p>
    </div>
    <div class="product-card">
      <img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQyq9K0rZxQOi9J-l6491F_Pqx_JKEDLjH22g&s" alt="Product 12">
      <h3 class="product-name">Product 12</h3>
      <p class="product-price">$14.99</p>
    </div>

    
  </main>
</body>
</html>
