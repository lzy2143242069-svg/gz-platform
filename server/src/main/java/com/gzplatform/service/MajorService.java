package com.gzplatform.service;

import com.gzplatform.entity.Major;
import java.util.List;

public interface MajorService {
    List<Major> listByUniversityId(Long universityId);
}
