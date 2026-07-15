package com.gzplatform.service;

import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.baomidou.mybatisplus.extension.service.IService;
import com.gzplatform.entity.ZhuanshengbenScore;

import java.util.List;
import java.util.Map;

public interface ZhuanshengbenScoreService extends IService<ZhuanshengbenScore> {

    IPage<ZhuanshengbenScore> queryScores(Page<ZhuanshengbenScore> page, Integer year, Long universityId, String majorName, String category);

    List<Map<String, Object>> scoreTrend(Long universityId, String majorName);

    List<Map<String, Object>> compare(List<Long> ids, Integer year);
}
