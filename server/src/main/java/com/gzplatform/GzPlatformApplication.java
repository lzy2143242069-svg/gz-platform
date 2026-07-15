package com.gzplatform;

import org.mybatis.spring.annotation.MapperScan;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
@MapperScan("com.gzplatform.mapper")
public class GzPlatformApplication {

    public static void main(String[] args) {
        SpringApplication.run(GzPlatformApplication.class, args);
    }
}
