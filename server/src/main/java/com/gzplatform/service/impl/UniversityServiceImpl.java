package com.gzplatform.service.impl;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.gzplatform.entity.University;
import com.gzplatform.mapper.UniversityMapper;
import com.gzplatform.service.UniversityService;
import org.springframework.stereotype.Service;
import org.springframework.util.StringUtils;

import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

@Service
public class UniversityServiceImpl extends ServiceImpl<UniversityMapper, University> implements UniversityService {

    @Override
    public IPage<University> listWithFilter(Page<University> page, String type, String city, String nature, Integer isZsbTarget) {
        LambdaQueryWrapper<University> wrapper = new LambdaQueryWrapper<>();
        wrapper.eq(StringUtils.hasText(type), University::getType, type)
               .eq(StringUtils.hasText(city), University::getCity, city)
               .eq(StringUtils.hasText(nature), University::getNature, nature)
               .eq(isZsbTarget != null, University::getIsZsbTarget, isZsbTarget)
               .orderByAsc(University::getRankSoft);
        return baseMapper.selectPage(page, wrapper);
    }

    @Override
    public University getDetailById(Long id) {
        return baseMapper.selectById(id);
    }

    @Override
    public List<University> search(String keyword) {
        LambdaQueryWrapper<University> wrapper = new LambdaQueryWrapper<>();
        wrapper.like(University::getName, keyword)
               .or()
               .like(University::getShortName, keyword)
               .last("LIMIT 20");
        return baseMapper.selectList(wrapper);
    }

    @Override
    public List<Map<String, Object>> getMapData() {
        List<University> all = baseMapper.selectList(
                new LambdaQueryWrapper<University>()
                        .isNotNull(University::getLongitude)
                        .isNotNull(University::getLatitude)
        );
        return all.stream().map(u -> {
            Map<String, Object> map = new HashMap<>();
            map.put("id", u.getId());
            map.put("name", u.getName());
            map.put("type", u.getType());
            map.put("city", u.getCity());
            map.put("lng", u.getLongitude());
            map.put("lat", u.getLatitude());
            map.put("isZsbTarget", u.getIsZsbTarget());
            return map;
        }).collect(Collectors.toList());
    }

    @Override
    public Map<String, Object> getOverview() {
        Map<String, Object> overview = new HashMap<>();
        long total = baseMapper.selectCount(null);
        long benke = baseMapper.selectCount(new LambdaQueryWrapper<University>().eq(University::getType, "本科"));
        long zhuanke = total - benke;
        long zsbTarget = baseMapper.selectCount(new LambdaQueryWrapper<University>().eq(University::getIsZsbTarget, 1));
        overview.put("totalUniversities", total);
        overview.put("benkeCount", benke);
        overview.put("zhuankeCount", zhuanke);
        overview.put("zsbUniversities", zsbTarget);
        overview.put("totalMajors", 0);
        return overview;
    }
}
