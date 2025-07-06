package com.karthik.inventory.service;

import com.karthik.inventory.model.Product;
import com.karthik.inventory.repository.ProductRepository;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.data.domain.*;
import org.springframework.stereotype.Service;

import java.util.*;

@Service
public class ProductService {

    @Autowired
    private ProductRepository repo;

    public Product save(Product p) {
        return repo.save(p);
    }

    public List<Product> getAll(Pageable pageable) {
        return repo.findAll(pageable).getContent();
    }

    public Optional<Product> getById(Long id) {
        return repo.findById(id);
    }

    public void deleteById(Long id) {
        repo.deleteById(id);
    }

    public List<Product> findByCategory(String category) {
        return repo.findByCategory(category);
    }

    public List<Product> findByPriceRange(double min, double max) {
        return repo.findByPriceBetween(min, max);
    }
}
