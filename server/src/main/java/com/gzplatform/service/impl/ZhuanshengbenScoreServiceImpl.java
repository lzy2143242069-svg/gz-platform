package com.gzplatform.service.impl;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.gzplatform.entity.University;
import com.gzplatform.entity.ZhuanshengbenScore;
import com.gzplatform.mapper.UniversityMapper;
import com.gzplatform.mapper.ZhuanshengbenScoreMapper;
import com.gzplatform.service.ZhuanshengbenScoreService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.util.StringUtils;

import java.util.*;
import java.util.stream.Collectors;

@Service
public class ZhuanshengbenScoreServiceImpl extends ServiceImpl<ZhuanshengbenScoreMapper, ZhuanshengbenScore> implements ZhuanshengbenScoreService {

    @Autowired
    private UniversityMapper universityMapper;

    @Override
    public IPage<ZhuanshengbenScore> queryScores(Page<ZhuanshengbenScore> page, Integer year, Long universityId, String majorName, String category) {
        LambdaQueryWrapper<ZhuanshengbenScore> wrapper = new LambdaQueryWrapper<>();
        wrapper.eq(year != null, ZhuanshengbenScore::getYear, year)
               .eq(universityId != null, ZhuanshengbenScore::getUniversityId, universityId)
               .like(StringUtils.hasText(majorName), ZhuanshengbenScore::getMajorName, majorName)
               .eq(StringUtils.hasText(category), ZhuanshengbenScore::getCategory, category)
               .orderByDesc(ZhuanshengbenScore::getYear)
               .orderByAsc(ZhuanshengbenScore::getMajorName);
        return baseMapper.selectPage(page, wrapper);
    }

    @Override
    public List<Map<String, Object>> scoreTrend(Long universityId, String majorName) {
        LambdaQueryWrapper<ZhuanshengbenScore> wrapper = new LambdaQueryWrapper<>();
        wrapper.eq(ZhuanshengbenScore::getUniversityId, universityId)
               .eq(StringUtils.hasText(majorName), ZhuanshengbenScore::getMajorName, majorName)
               .orderByAsc(ZhuanshengbenScore::getYear);
        List<ZhuanshengbenScore> scores = baseMapper.selectList(wrapper);

        return scores.stream().map(s -> {
            Map<String, Object> map = new HashMap<>();
            map.put("year", s.getYear());
            map.put("majorName", s.getMajorName());
            map.put("totalScore", s.getTotalScore());
            map.put("lineScore", s.getLineScore());
            map.put("maxScore", s.getMaxScore());
            map.put("avgScore", s.getAvgScore());
            map.put("enrollCount", s.getEnrollCount());
            map.put("competitionRatio", s.getCompetitionRatio());
            return map;
        }).collect(Collectors.toList());
    }

    @Override
    public List<Map<String, Object>> compare(List<Long> ids, Integer year) {
        List<Map<String, Object>> result = new ArrayList<>();
        for (Long id : ids) {
            University uni = universityMapper.selectById(id);
            if (uni == null) continue;

            LambdaQueryWrapper<ZhuanshengbenScore> wrapper = new LambdaQueryWrapper<>();
            wrapper.eq(ZhuanshengbenScore::getUniversityId, id)
                   .eq(year != null, ZhuanshengbenScore::getYear, year);
            List<ZhuanshengbenScore> scores = baseMapper.selectList(wrapper);

            Map<String, Object> item = new HashMap<>();
            item.put("universityId", id);
            item.put("universityName", uni.getName());
            item.put("city", uni.getCity());
            item.put("nature", uni.getNature());
            item.put("scores", scores);
            result.add(item);
        }
        return result;
    }
}
