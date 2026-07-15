package com.gzplatform.controller;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.gzplatform.common.Result;
import com.gzplatform.entity.AdmissionScore;
import com.gzplatform.entity.ZhuanshengbenScore;
import com.gzplatform.mapper.AdmissionScoreMapper;
import com.gzplatform.mapper.ZhuanshengbenScoreMapper;
import com.gzplatform.service.UniversityService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.*;
import java.util.stream.Collectors;

@RestController
@RequestMapping("/api/stats")
public class StatisticsController {

    @Autowired
    private UniversityService universityService;

    @Autowired
    private AdmissionScoreMapper admissionScoreMapper;

    @Autowired
    private ZhuanshengbenScoreMapper zsbScoreMapper;

    @GetMapping("/overview")
    public Result<Map<String, Object>> overview() {
        return Result.success(universityService.getOverview());
    }

    @GetMapping("/ranking")
    public Result<List<Map<String, Object>>> ranking(@RequestParam(defaultValue = "city") String type) {
        List<Map<String, Object>> result;
        if ("city".equals(type)) {
            result = universityService.getMapData().stream()
                    .collect(Collectors.groupingBy(m -> m.get("city").toString()))
                    .entrySet().stream()
                    .map(e -> {
                        Map<String, Object> item = new HashMap<>();
                        item.put("city", e.getKey());
                        item.put("count", e.getValue().size());
                        return item;
                    })
                    .sorted((a, b) -> Integer.compare((int) b.get("count"), (int) a.get("count")))
                    .collect(Collectors.toList());
        } else {
            result = new ArrayList<>();
        }
        return Result.success(result);
    }

    @GetMapping("/score-distribution")
    public Result<Map<String, Object>> scoreDistribution(
            @RequestParam(required = false) Integer year,
            @RequestParam(defaultValue = "专升本") String type) {
        Map<String, Object> distribution = new HashMap<>();
        if ("专升本".equals(type)) {
            List<ZhuanshengbenScore> scores = zsbScoreMapper.selectList(
                    new LambdaQueryWrapper<ZhuanshengbenScore>()
                            .eq(year != null, ZhuanshengbenScore::getYear, year != null ? year : 2024));
            Map<String, Long> byRange = scores.stream()
                    .collect(Collectors.groupingBy(s -> {
                        int score = s.getTotalScore() != null ? s.getTotalScore() : 0;
                        if (score < 200) return "200分以下";
                        if (score < 250) return "200-250分";
                        if (score < 300) return "250-300分";
                        if (score < 350) return "300-350分";
                        return "350分以上";
                    }, Collectors.counting()));
            distribution.put("scores", byRange);
            distribution.put("total", scores.size());
        }
        return Result.success(distribution);
    }
}
