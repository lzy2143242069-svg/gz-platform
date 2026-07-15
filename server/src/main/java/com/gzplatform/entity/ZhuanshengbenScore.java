package com.gzplatform.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.math.BigDecimal;
import java.time.LocalDateTime;

@Data
@TableName("zhuanshengben_score")
public class ZhuanshengbenScore {

    @TableId(type = IdType.AUTO)
    private Long id;
    private Long universityId;
    private Integer year;
    private String majorName;
    private String category;
    private Integer totalScore;
    private Integer lineScore;
    private Integer maxScore;
    private BigDecimal avgScore;
    private Integer passCount;
    private Integer enrollCount;
    private BigDecimal competitionRatio;
    private String dataSource;
    private Integer status;
    private LocalDateTime createdAt;
    private LocalDateTime updatedAt;
}
