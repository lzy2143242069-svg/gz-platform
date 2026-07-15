package com.gzplatform.service;

import com.baomidou.mybatisplus.core.metadata.IPage;
import com.baomidou.mybatisplus.extension.plugins.pagination.Page;
import com.baomidou.mybatisplus.extension.service.IService;
import com.gzplatform.entity.University;

import java.util.List;
import java.util.Map;

public interface UniversityService extends IService<University> {

    IPage<University> listWithFilter(Page<University> page, String type, String city, String nature, Integer isZsbTarget);

    University getDetailById(Long id);

    List<University> search(String keyword);

    List<Map<String, Object>> getMapData();

    Map<String, Object> getOverview();
}
