// src/main/java/com/karthik/inventory/config/OpenApiConfig.java
package com.karthik.inventory.config;

import io.swagger.v3.oas.models.info.Info;
import io.swagger.v3.oas.models.OpenAPI;
import org.springframework.context.annotation.*;

@Configuration
public class OpenApiConfig {

    @Bean
    public OpenAPI apiInfo() {
        return new OpenAPI()
                .info(new Info()
                    .title("Product Inventory API")
                    .version("1.0")
                    .description("API documentation for Product Inventory App"));
    }
}
