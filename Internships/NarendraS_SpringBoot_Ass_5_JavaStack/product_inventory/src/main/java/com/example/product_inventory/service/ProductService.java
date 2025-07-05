package com.example.product_inventory.service;

import com.example.product_inventory.model.Product;
import com.example.product_inventory.repository.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.*;
import org.springframework.stereotype.Service;

import java.util.Optional;

@Service
public class ProductService {
	
	@Autowired
	private ProductRepository productRepository;
	
	public Product saveProduct(Product product) {
		return productRepository.save(product);
	}
	
	public Page<Product> getAllProducts(Pageable pageable){
		return productRepository.findAll(pageable);
	}
	
	public Optional<Product> getProductById(Long id){
		return productRepository.findById(id);
	}
	
	public void deleteProduct(Long id) {
		productRepository.deleteById(id);
	}
	
	public Page<Product> filterByCategory(String category, Pageable pageable){
		return productRepository.findByCategory(category, pageable);
	}
	
	public Page<Product> filterByPriceRange(double min, double max, Pageable pageable){
		return productRepository.findByPriceBetween(min, max, pageable);
	}
}
