package com.karthik.inventory.controller;

import com.karthik.inventory.model.Product;
import com.karthik.inventory.service.ProductService;
import com.karthik.inventory.exception.ProductNotFoundException;
import jakarta.validation.Valid;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;
import org.springframework.http.*;
import org.springframework.data.domain.*;

import java.util.List;

@RestController
@RequestMapping("/api/products")
public class ProductController {

    @Autowired
    private ProductService service;

    @PostMapping
    public ResponseEntity<Product> create(@Valid @RequestBody Product p) {
        return new ResponseEntity<>(service.save(p), HttpStatus.CREATED);
    }

    @GetMapping
    public ResponseEntity<List<Product>> getAll(@RequestParam(defaultValue = "0") int page,
                                                @RequestParam(defaultValue = "10") int size,
                                                @RequestParam(defaultValue = "id") String sortBy) {
        return ResponseEntity.ok(service.getAll(PageRequest.of(page, size, Sort.by(sortBy))));
    }

    @GetMapping("/{id}")
    public Product getById(@PathVariable Long id) {
        return service.getById(id).orElseThrow(() -> new ProductNotFoundException(id));
    }

    @PutMapping("/{id}")
    public Product update(@PathVariable Long id, @Valid @RequestBody Product p) {
        Product existing = service.getById(id).orElseThrow(() -> new ProductNotFoundException(id));
        existing.setName(p.getName());
        existing.setCategory(p.getCategory());
        existing.setPrice(p.getPrice());
        existing.setQuantity(p.getQuantity());
        return service.save(existing);
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(@PathVariable Long id) {
        service.deleteById(id);
        return ResponseEntity.noContent().build();
    }

    @GetMapping("/filter")
    public ResponseEntity<List<Product>> filter(@RequestParam(required = false) String category,
                                                @RequestParam(required = false) Double minPrice,
                                                @RequestParam(required = false) Double maxPrice) {
        if (category != null) return ResponseEntity.ok(service.findByCategory(category));
        if (minPrice != null && maxPrice != null)
            return ResponseEntity.ok(service.findByPriceRange(minPrice, maxPrice));
        return ResponseEntity.badRequest().build();
    }
}
