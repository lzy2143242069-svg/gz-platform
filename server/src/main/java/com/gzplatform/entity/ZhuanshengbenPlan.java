package com.gzplatform.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.math.BigDecimal;
import java.time.LocalDateTime;

@Data
@TableName("zhuanshengben_plan")
public class ZhuanshengbenPlan {

    @TableId(type = IdType.AUTO)
    private Long id;
    private Long universityId;
    private Long majorId;
    private Integer year;
    private String majorName;
    private Integer planCount;
    private Integer actualEnroll;
    private String category;
    private BigDecimal tuition;
    private String duration;
    private String campus;
    private String requirement;
    private String examSubjects;
    private String textbookInfo;
    private String dataSource;
    private Integer status;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
}
