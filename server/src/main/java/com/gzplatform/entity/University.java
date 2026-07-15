package com.gzplatform.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.math.BigDecimal;
import java.time.LocalDateTime;

@Data
@TableName("university")
public class University {

    @TableId(type = IdType.AUTO)
    private Long id;
    private String name;
    private String shortName;
    private String code;
    private String type;
    private String nature;
    private String level;
    private String city;
    private String district;
    private String address;
    private BigDecimal longitude;
    private BigDecimal latitude;
    private String website;
    private String logoUrl;
    private String description;
    private Integer foundedYear;
    private BigDecimal areaMu;
    private Integer studentCount;
    private Integer facultyCount;
    private Integer isZsbTarget;
    private Integer rankSoft;
    private Integer rankQs;
    private Integer status;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
}
