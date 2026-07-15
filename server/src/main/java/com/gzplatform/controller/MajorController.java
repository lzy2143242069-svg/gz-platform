package com.gzplatform.controller;

import com.gzplatform.common.Result;
import com.gzplatform.entity.Major;
import com.gzplatform.service.MajorService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/major")
public class MajorController {

    @Autowired
    private MajorService majorService;

    @GetMapping("/list")
    public Result<List<Major>> list(@RequestParam Long universityId) {
        return Result.success(majorService.listByUniversityId(universityId));
    }
}
