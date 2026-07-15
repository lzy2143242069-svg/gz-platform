package com.gzplatform.entity;

import com.baomidou.mybatisplus.annotation.IdType;
import com.baomidou.mybatisplus.annotation.TableId;
import com.baomidou.mybatisplus.annotation.TableName;
import lombok.Data;

import java.time.LocalDateTime;

@Data
@TableName("province_control_line")
public class ProvinceControlLine {

    @TableId(type = IdType.AUTO)
    private Long id;
    private Integer year;
    private String examType;
    private String batch;
    private String subjectType;
    private Integer score;
    private String remark;
    private String dataSource;
    private LocalDateTime createdAt;
}
