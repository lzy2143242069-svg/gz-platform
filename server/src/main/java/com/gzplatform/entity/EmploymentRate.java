package com.gzplatform.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.math.BigDecimal;
import java.time.LocalDateTime;

@Data
@TableName("employment_rate")
public class EmploymentRate {

    @TableId(type = IdType.AUTO)
    private Long id;
    private Long universityId;
    private Long majorId;
    private Integer year;
    private BigDecimal rate;
    private BigDecimal avgSalary;
    private String topIndustry;
    private String dataSource;
    private Integer status;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
}
