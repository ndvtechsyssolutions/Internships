package com.example.product_inventory.repository;

import com.example.product_inventory.model.Product;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;

public interface ProductRepository extends JpaRepository<Product, Long> {
	Page<Product> findByCategory(String category, Pageable pageable);
	Page<Product> findByPriceBetween(double min, double max, Pageable pageable);
}

