package com.gzplatform.service.impl;

import com.baomidou.mybatisplus.core.conditions.query.LambdaQueryWrapper;
import com.gzplatform.entity.Major;
import com.gzplatform.mapper.MajorMapper;
import com.gzplatform.service.MajorService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class MajorServiceImpl implements MajorService {

    @Autowired
    private MajorMapper majorMapper;

    @Override
    public List<Major> listByUniversityId(Long universityId) {
        LambdaQueryWrapper<Major> wrapper = new LambdaQueryWrapper<>();
        wrapper.eq(Major::getUniversityId, universityId)
               .eq(Major::getStatus, 1)
               .orderByAsc(Major::getName);
        return majorMapper.selectList(wrapper);
    }
}
