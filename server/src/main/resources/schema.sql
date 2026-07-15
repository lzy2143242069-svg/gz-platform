-- =============================================
-- 贵州高校数据平台 - 建表脚本 (H2/MySQL 兼容)
-- =============================================

-- 表 1: university - 高校基本信息
CREATE TABLE IF NOT EXISTS university (
    id              BIGINT PRIMARY KEY AUTO_INCREMENT,
    name            VARCHAR(100) NOT NULL,
    short_name      VARCHAR(50),
    code            VARCHAR(20),
    type            VARCHAR(20) NOT NULL,
    nature          VARCHAR(20) NOT NULL,
    level           VARCHAR(30),
    city            VARCHAR(30) NOT NULL,
    district        VARCHAR(50),
    address         VARCHAR(200),
    longitude       DECIMAL(10,6),
    latitude        DECIMAL(10,6),
    website         VARCHAR(200),
    logo_url        VARCHAR(300),
    description     TEXT,
    founded_year    INT,
    area_mu         DECIMAL(10,2),
    student_count   INT,
    faculty_count   INT,
    is_zsb_target   TINYINT DEFAULT 0,
    rank_soft       INT,
    rank_qs         INT,
    status          TINYINT DEFAULT 1,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 表 2: major - 专业信息
CREATE TABLE IF NOT EXISTS major (
    id              BIGINT PRIMARY KEY AUTO_INCREMENT,
    university_id   BIGINT NOT NULL,
    name            VARCHAR(100) NOT NULL,
    code            VARCHAR(20),
    category        VARCHAR(50),
    first_category  VARCHAR(50),
    degree_type     VARCHAR(20),
    duration        INT,
    tuition         DECIMAL(10,2),
    is_national_key TINYINT DEFAULT 0,
    is_province_key TINYINT DEFAULT 0,
    employment_desc TEXT,
    status          TINYINT DEFAULT 1,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 表 3: admission_score - 高考录取分数线
CREATE TABLE IF NOT EXISTS admission_score (
    id              BIGINT PRIMARY KEY AUTO_INCREMENT,
    university_id   BIGINT NOT NULL,
    major_id        BIGINT,
    year            INT NOT NULL,
    province        VARCHAR(20) DEFAULT '贵州',
    batch           VARCHAR(30) NOT NULL,
    subject_type    VARCHAR(20) NOT NULL,
    min_score       INT,
    max_score       INT,
    avg_score       DECIMAL(6,1),
    min_rank        INT,
    plan_count      INT,
    actual_count    INT,
    data_source     VARCHAR(100),
    status          TINYINT DEFAULT 1,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 表 4: zhuanshengben_plan - 专升本招生计划
CREATE TABLE IF NOT EXISTS zhuanshengben_plan (
    id                  BIGINT PRIMARY KEY AUTO_INCREMENT,
    university_id       BIGINT NOT NULL,
    major_id            BIGINT,
    year                INT NOT NULL,
    major_name          VARCHAR(100) NOT NULL,
    plan_count          INT,
    actual_enroll       INT,
    category            VARCHAR(30),
    tuition             DECIMAL(10,2),
    duration            VARCHAR(20),
    campus              VARCHAR(100),
    requirement         TEXT,
    exam_subjects       VARCHAR(200),
    textbook_info       TEXT,
    data_source         VARCHAR(100),
    status              TINYINT DEFAULT 1,
    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 表 5: zhuanshengben_score - 专升本分数线
CREATE TABLE IF NOT EXISTS zhuanshengben_score (
    id                  BIGINT PRIMARY KEY AUTO_INCREMENT,
    university_id       BIGINT NOT NULL,
    year                INT NOT NULL,
    major_name          VARCHAR(100) NOT NULL,
    category            VARCHAR(30),
    total_score         INT,
    line_score          INT,
    max_score           INT,
    avg_score           DECIMAL(6,1),
    pass_count          INT,
    enroll_count        INT,
    competition_ratio   DECIMAL(5,2),
    data_source         VARCHAR(100),
    status              TINYINT DEFAULT 1,
    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 表 6: employment_rate - 就业率数据
CREATE TABLE IF NOT EXISTS employment_rate (
    id              BIGINT PRIMARY KEY AUTO_INCREMENT,
    university_id   BIGINT NOT NULL,
    major_id        BIGINT,
    year            INT NOT NULL,
    rate            DECIMAL(5,2),
    avg_salary      DECIMAL(10,2),
    top_industry    VARCHAR(100),
    data_source     VARCHAR(100),
    status          TINYINT DEFAULT 1,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 表 7: province_control_line - 省控线
CREATE TABLE IF NOT EXISTS province_control_line (
    id              BIGINT PRIMARY KEY AUTO_INCREMENT,
    year            INT NOT NULL,
    exam_type       VARCHAR(20) NOT NULL,
    batch           VARCHAR(30) NOT NULL,
    subject_type    VARCHAR(20) NOT NULL,
    score           INT NOT NULL,
    remark          VARCHAR(200),
    data_source     VARCHAR(100),
    status          TINYINT DEFAULT 1,
    created_at      TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 表 8: major_mapping - 专升本专业对照表
CREATE TABLE IF NOT EXISTS major_mapping (
    id                  BIGINT PRIMARY KEY AUTO_INCREMENT,
    source_major_name   VARCHAR(100) NOT NULL,
    source_major_code   VARCHAR(20),
    target_major_name   VARCHAR(100) NOT NULL,
    target_university_id BIGINT NOT NULL,
    year                INT NOT NULL,
    is_limited          TINYINT DEFAULT 0,
    remark              VARCHAR(200),
    created_at          TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
