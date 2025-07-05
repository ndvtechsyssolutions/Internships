package com.example.product_inventory.controller;

import com.example.product_inventory.model.Product;
import com.example.product_inventory.service.ProductService;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.*;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.Optional;

@RestController
@RequestMapping("/api/products")
public class ProductController {

	@Autowired
	private ProductService productService;

	@PostMapping
	public ResponseEntity<Product> createProduct(@Valid @RequestBody Product product){
		return ResponseEntity.ok(productService.saveProduct(product));
	}

	@GetMapping
	public ResponseEntity<Page<Product>> getAllProducts(
			@RequestParam(defaultValue = "0") int page,
			@RequestParam(defaultValue = "5") int size,
			@RequestParam(defaultValue = "id") String sortBy
			){
		Pageable pageable = PageRequest.of(page, size, Sort.by(sortBy));
		return ResponseEntity.ok(productService.getAllProducts(pageable));
	}

	@GetMapping("/{id}")
	public ResponseEntity<?> getProductById(@PathVariable Long id){
		Optional<Product> product = productService.getProductById(id);
		return product.map(ResponseEntity::ok).orElseGet(() -> ResponseEntity.notFound().build());
	}

	@PutMapping("/{id}")
	public ResponseEntity<?> updateProduct(@PathVariable Long id, @Valid @RequestBody Product newProduct){
		return productService.getProductById(id).map(existing -> {
			newProduct.setId(existing.getId());
			return ResponseEntity.ok(productService.saveProduct(newProduct));
		}).orElseGet(() -> ResponseEntity.notFound().build());
	}

	@DeleteMapping("/{id}")
	public ResponseEntity<?> deleteProduct(@PathVariable Long id){
		productService.deleteProduct(id);
		return ResponseEntity.ok("Product deleted");
	}

	@GetMapping("/filter/category")
	public ResponseEntity<Page<Product>> filterByCategory(@RequestParam String category, @RequestParam(defaultValue = "0") int page, @RequestParam(defaultValue = "5") int size){
		Pageable pageable = PageRequest.of(page, size);
		return ResponseEntity.ok(productService.filterByCategory(category, pageable));
	}

	@GetMapping("/filter/price")
	public ResponseEntity<Page<Product>> filterByPrice(@RequestParam double min, @RequestParam double max, @RequestParam(defaultValue = "0") int page, @RequestParam(defaultValue = "5") int size){
		Pageable pageable = PageRequest.of(page, size);
		return ResponseEntity.ok(productService.filterByPriceRange(min, max, pageable));
	}
}




























