package com.gzplatform.service;

import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.baomidou.mybatisplus.extension.service.IService;
import com.gzplatform.entity.ZhuanshengbenPlan;

public interface ZhuanshengbenPlanService extends IService<ZhuanshengbenPlan> {

    IPage<ZhuanshengbenPlan> queryPlans(Page<ZhuanshengbenPlan> page, Integer year, Long universityId, String majorName);
}
