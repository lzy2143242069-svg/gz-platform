package com.gzplatform.controller;

import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.gzplatform.common.Result;
import com.gzplatform.entity.University;
import com.gzplatform.service.UniversityService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/university")
public class UniversityController {

    @Autowired
    private UniversityService universityService;

    @GetMapping("/list")
    public Result<IPage<University>> list(
            @RequestParam(defaultValue = "1") int page,
            @RequestParam(defaultValue = "20") int size,
            @RequestParam(required = false) String type,
            @RequestParam(required = false) String city,
            @RequestParam(required = false) String nature,
            @RequestParam(required = false) Integer isZsbTarget) {
        IPage<University> result = universityService.listWithFilter(
                new Page<>(page, size), type, city, nature, isZsbTarget);
        return Result.success(result);
    }

    @GetMapping("/{id}")
    public Result<University> detail(@PathVariable Long id) {
        University university = universityService.getDetailById(id);
        if (university == null) {
            return Result.error(404, "高校不存在");
        }
        return Result.success(university);
    }

    @GetMapping("/search")
    public Result<List<University>> search(@RequestParam String keyword) {
        return Result.success(universityService.search(keyword));
    }

    @GetMapping("/map-data")
    public Result<List<Map<String, Object>>> mapData() {
        return Result.success(universityService.getMapData());
    }
}
