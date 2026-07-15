package com.gzplatform.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.math.BigDecimal;
import java.time.LocalDateTime;

@Data
@TableName("admission_score")
public class AdmissionScore {

    @TableId(type = IdType.AUTO)
    private Long id;
    private Long universityId;
    private Long majorId;
    private Integer year;
    private String province;
    private String batch;
    private String subjectType;
    private Integer minScore;
    private Integer maxScore;
    private BigDecimal avgScore;
    private Integer minRank;
    private Integer planCount;
    private Integer actualCount;
    private String dataSource;
    private Integer status;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
}
