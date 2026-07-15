package com.gzplatform.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.math.BigDecimal;
import java.time.LocalDateTime;

@Data
@TableName("major")
public class Major {

    @TableId(type = IdType.AUTO)
    private Long id;
    private Long universityId;
    private String name;
    private String code;
    private String category;
    private String firstCategory;
    private String degreeType;
    private Integer duration;
    private BigDecimal tuition;
    private Integer isNationalKey;
    private Integer isProvinceKey;
    private String employmentDesc;
    private Integer status;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
}
