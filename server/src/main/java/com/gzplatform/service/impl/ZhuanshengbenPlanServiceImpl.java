package com.gzplatform.service.impl;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.baomidou.mybatisplus.extension.service.impl.ServiceImpl;
import com.gzplatform.entity.ZhuanshengbenPlan;
import com.gzplatform.mapper.ZhuanshengbenPlanMapper;
import com.gzplatform.service.ZhuanshengbenPlanService;
import org.springframework.stereotype.Service;
import org.springframework.util.StringUtils;

@Service
public class ZhuanshengbenPlanServiceImpl extends ServiceImpl<ZhuanshengbenPlanMapper, ZhuanshengbenPlan> implements ZhuanshengbenPlanService {

    @Override
    public IPage<ZhuanshengbenPlan> queryPlans(Page<ZhuanshengbenPlan> page, Integer year, Long universityId, String majorName) {
        LambdaQueryWrapper<ZhuanshengbenPlan> wrapper = new LambdaQueryWrapper<>();
        wrapper.eq(year != null, ZhuanshengbenPlan::getYear, year)
               .eq(universityId != null, ZhuanshengbenPlan::getUniversityId, universityId)
               .like(StringUtils.hasText(majorName), ZhuanshengbenPlan::getMajorName, majorName)
               .orderByDesc(ZhuanshengbenPlan::getYear)
               .orderByAsc(ZhuanshengbenPlan::getMajorName);
        return baseMapper.selectPage(page, wrapper);
    }
}
