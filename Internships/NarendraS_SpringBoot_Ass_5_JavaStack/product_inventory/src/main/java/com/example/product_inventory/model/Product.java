package com.example.product_inventory.model;

import jakarta.persistence.*;
import jakarta.validation.constraints.*;

@Entity
public class Product {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private Long id;
	
	@NotBlank(message = "Product name is required")
	private String name;
	
	@NotBlank(message = "Category is required")
	private String category;
	
	@Min(0)
	private int quantity;
	
	@DecimalMin(value = "0.0", inclusive = false)
	private double price;
	
	//Getters and Setters
	public Long getId() {return id;}
	public void setId(Long id) {this.id = id;}
	public String getName() {return name;}
	public void setName(String name) {this.name = name;}
	public String getCategory() {return category;}
	public void setCategory(String category) {this.category = category;}
	public int getQuantity() {return quantity;}
	public void setQuantity(int quantity) {this.quantity = quantity;}
	public double getPrice() {return price;}
	public void setPrice(double price) {this.price = price;}
}
