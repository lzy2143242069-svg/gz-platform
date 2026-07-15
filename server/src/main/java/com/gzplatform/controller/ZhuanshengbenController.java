package com.gzplatform.controller;

import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.gzplatform.common.Result;
import com.gzplatform.entity.ZhuanshengbenPlan;
import com.gzplatform.entity.ZhuanshengbenScore;
import com.gzplatform.service.ZhuanshengbenPlanService;
import com.gzplatform.service.ZhuanshengbenScoreService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/zsb")
public class ZhuanshengbenController {

    @Autowired
    private ZhuanshengbenScoreService zsbScoreService;

    @Autowired
    private ZhuanshengbenPlanService zsbPlanService;

    @GetMapping("/plans")
    public Result<IPage<ZhuanshengbenPlan>> queryPlans(
            @RequestParam(required = false) Integer year,
            @RequestParam(required = false) Long universityId,
            @RequestParam(required = false) String majorName,
            @RequestParam(defaultValue = "1") int page,
            @RequestParam(defaultValue = "20") int size) {
        IPage<ZhuanshengbenPlan> result = zsbPlanService.queryPlans(
                new Page<>(page, size), year, universityId, majorName);
        return Result.success(result);
    }

    @GetMapping("/scores")
    public Result<IPage<ZhuanshengbenScore>> queryScores(
            @RequestParam(required = false) Integer year,
            @RequestParam(required = false) Long universityId,
            @RequestParam(required = false) String majorName,
            @RequestParam(required = false) String category,
            @RequestParam(defaultValue = "1") int page,
            @RequestParam(defaultValue = "20") int size) {
        IPage<ZhuanshengbenScore> result = zsbScoreService.queryScores(
                new Page<>(page, size), year, universityId, majorName, category);
        return Result.success(result);
    }

    @GetMapping("/score-trend")
    public Result<List<Map<String, Object>>> scoreTrend(
            @RequestParam Long universityId,
            @RequestParam(required = false) String majorName) {
        return Result.success(zsbScoreService.scoreTrend(universityId, majorName));
    }

    @GetMapping("/compare")
    public Result<List<Map<String, Object>>> compare(
            @RequestParam List<Long> ids,
            @RequestParam(required = false) Integer year) {
        return Result.success(zsbScoreService.compare(ids, year));
    }

    @GetMapping("/guide")
    public Result<Map<String, Object>> guide() {
        Map<String, Object> guide = new java.util.LinkedHashMap<>();
        guide.put("title", "贵州专升本报考指南");
        guide.put("timeline", List.of(
                Map.of("step", 1, "name", "发布招生简章", "time", "每年1-2月", "desc", "各招生院校陆续发布当年专升本招生简章"),
                Map.of("step", 2, "name", "网上报名", "time", "3月上旬", "desc", "登录贵州省招生考试院官网进行网上报名"),
                Map.of("step", 3, "name", "资格审核", "time", "3月中旬", "desc", "所在专科院校审核报名资格"),
                Map.of("step", 4, "name", "缴费确认", "time", "3月下旬", "desc", "网上缴纳报名考试费"),
                Map.of("step", 5, "name", "打印准考证", "time", "考前一周", "desc", "登录报名系统打印准考证"),
                Map.of("step", 6, "name", "统一考试", "time", "4月中旬", "desc", "文化课考试 + 专业课考试"),
                Map.of("step", 7, "name", "成绩公布", "time", "5月中旬", "desc", "省招生考试院公布成绩和最低控制线"),
                Map.of("step", 8, "name", "志愿填报", "time", "5月下旬", "desc", "根据成绩填报志愿"),
                Map.of("step", 9, "name", "录取公示", "time", "6月", "desc", "各校公布录取名单")
        ));
        guide.put("tips", List.of(
                "关注贵州省招生考试院官网 (eaagz.org.cn) 获取最新政策",
                "专升本只能报考本省院校，不能跨省",
                "部分专业有对口限制，需查看专业对照表",
                "退役士兵有免试政策，需提前准备材料",
                "建议同时准备文化课和专业课，不要偏科"
        ));
        return Result.success(guide);
    }
}
