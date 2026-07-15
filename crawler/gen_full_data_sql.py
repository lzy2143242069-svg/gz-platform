"""Generate complete data.sql with all 80 Guizhou universities, real coords, real rankings"""
import json

# Load all geocoded data
with open('crawler/data/university_coords.json', 'r', encoding='utf-8') as f:
    old_coords = json.load(f)
with open('crawler/data/new_schools_coords.json', 'r', encoding='utf-8') as f:
    new_coords = json.load(f)

coord_map = {}
for c in old_coords + new_coords:
    coord_map[c['name']] = (c['lng'], c['lat'])

# User's complete 80-school ranking list with real data
# Format: (rank, name, short_name, code, type, nature, level, city, district_hint, website, founded_year, is_zsb_target)
schools = [
    # 本科 公办 (24所)
    (1,  '贵州大学', '贵大', '10657', '本科', '公办', '211/双一流', '贵阳', '花溪区', 'https://www.gzu.edu.cn', 1902, 0),
    (2,  '贵州医科大学', '贵医', '10660', '本科', '公办', '普通本科', '贵阳', '贵安新区', 'https://www.gmc.edu.cn', 1938, 1),
    (3,  '遵义医科大学', '遵医', '10661', '本科', '公办', '普通本科', '遵义', '新蒲新区', 'https://www.zmc.edu.cn', 1947, 1),
    (4,  '贵州中医药大学', '贵中医', '10662', '本科', '公办', '普通本科', '贵阳', '花溪区', 'https://www.gzucm.edu.cn', 1965, 1),
    (5,  '贵州师范大学', '贵师大', '10663', '本科', '公办', '普通本科', '贵阳', '花溪区', 'https://www.gznu.edu.cn', 1941, 1),
    (6,  '遵义师范学院', '遵师', '10664', '本科', '公办', '普通本科', '遵义', '红花岗区', 'https://www.zync.edu.cn', 1907, 1),
    (7,  '铜仁学院', '铜院', '10665', '本科', '公办', '普通本科', '铜仁', '碧江区', 'https://www.trxy.edu.cn', 1920, 1),
    (8,  '兴义民族师范学院', '兴义师院', '10666', '本科', '公办', '普通本科', '兴义', '兴义市', 'https://www.xynun.edu.cn', 1813, 1),
    (9,  '安顺学院', '安院', '10667', '本科', '公办', '普通本科', '安顺', '西秀区', 'https://www.asu.edu.cn', 1938, 1),
    (10, '贵州工程应用技术学院', '贵工程', '10668', '本科', '公办', '普通本科', '毕节', '七星关区', 'https://www.gues.edu.cn', 1938, 1),
    (11, '凯里学院', '凯院', '10669', '本科', '公办', '普通本科', '凯里', '凯里市', 'https://www.kluniv.edu.cn', 1958, 1),
    (12, '黔南民族师范学院', '黔南师院', '10670', '本科', '公办', '普通本科', '都匀', '都匀市', 'https://www.sgmtu.edu.cn', 1958, 1),
    (13, '贵州财经大学', '贵财', '10671', '本科', '公办', '普通本科', '贵阳', '花溪区', 'https://www.gzufe.edu.cn', 1958, 1),
    (14, '贵州民族大学', '贵民大', '10672', '本科', '公办', '普通本科', '贵阳', '花溪区', 'https://www.gzmu.edu.cn', 1951, 1),
    (15, '贵阳学院', '贵院', '10976', '本科', '公办', '普通本科', '贵阳', '南明区', 'https://www.gyu.cn', 1978, 1),
    (16, '六盘水师范学院', '六师', '10977', '本科', '公办', '普通本科', '六盘水', '钟山区', 'https://www.lpssy.edu.cn', 1978, 1),
    (17, '贵州商学院', '贵商', '11731', '本科', '公办', '普通本科', '贵阳', '白云区', 'https://www.gzcc.edu.cn', 2015, 1),
    (18, '贵州警察学院', '贵警', '12109', '本科', '公办', '普通本科', '贵阳', '花溪区', 'https://www.gzjgxy.cn', 1950, 1),
    (19, '贵阳康养职业大学', '贵康养', '11652', '本科', '公办', '职业本科', '贵阳', '观山湖区', 'https://www.gykz.edu.cn', 2021, 1),
    (20, '贵州师范学院', '贵师院', '10667', '本科', '公办', '普通本科', '贵阳', '乌当区', 'https://www.gznc.edu.cn', 1978, 1),
    (21, '贵州理工学院', '贵理工', '14440', '本科', '公办', '普通本科', '贵阳', '花溪区', 'https://www.git.edu.cn', 2013, 1),
    (22, '贵州交通职业大学', '贵交大', '12222', '本科', '公办', '职业本科', '贵阳', '清镇市', 'https://www.gzjtzy.edu.cn', 1958, 1),
    (23, '铜仁职业技术大学', '铜仁职大', '13055', '本科', '公办', '职业本科', '铜仁', '碧江区', 'https://www.trkxy.cn', 2002, 1),
    (24, '贵州轻工职业大学', '贵轻大', '13818', '本科', '公办', '职业本科', '贵阳', '花溪区', 'https://www.gzqy.edu.cn', 1978, 1),
    # 本科 民办 (8所)
    (25, '贵州中医药大学时珍学院', '时珍学院', '13647', '本科', '民办', '独立学院', '贵阳', '花溪区', 'https://www.gzszk.edu.cn', 2001, 1),
    (26, '贵州黔南经济学院', '贵经院', '13648', '本科', '民办', '独立学院', '都匀', '惠水县', 'https://www.gzqjxy.edu.cn', 2001, 1),
    (27, '贵州黔南科技学院', '贵科院', '13649', '本科', '民办', '独立学院', '都匀', '惠水县', 'https://www.gzqkkj.edu.cn', 2001, 1),
    (28, '贵阳信息科技学院', '贵信科', '13650', '本科', '民办', '独立学院', '贵阳', '花溪区', 'https://www.gyist.edu.cn', 2001, 1),
    (29, '贵阳人文科技学院', '贵人文', '13651', '本科', '民办', '独立学院', '贵阳', '花溪区', 'https://www.gzmdc.edu.cn', 2001, 1),
    (30, '遵义医科大学医学与科技学院', '遵医科技', '13653', '本科', '民办', '独立学院', '遵义', '新蒲新区', 'https://www.zmckjxy.edu.cn', 2001, 1),
    (31, '贵州医科大学神奇民族医药学院', '神奇学院', '13676', '本科', '民办', '独立学院', '贵阳', '花溪区', 'https://www.gysqxy.edu.cn', 2004, 1),
    (32, '茅台学院', '茅院', '14625', '本科', '民办', '普通本科', '遵义', '仁怀市', 'https://www.mtxy.edu.cn', 2017, 1),
    (33, '贵州工商职业大学', '贵工商大', '14765', '本科', '民办', '职业本科', '贵阳', '清镇市', 'https://www.gzgsc.edu.cn', 2012, 1),
    # 专科 公办 (41所)
    (34, '黔南民族医学高等专科学校', '黔南医专', '11663', '专科', '公办', '高职高专', '都匀', '都匀市', 'https://www.qnyz.edu.cn', 1985, 0),
    (35, '贵州航天职业技术学院', '贵航职院', '12223', '专科', '公办', '高职高专', '遵义', '新蒲新区', 'https://www.gzhtzy.edu.cn', 1984, 0),
    (36, '贵州电子信息职业技术学院', '贵电子职院', '12336', '专科', '公办', '高职高专', '凯里', '凯里市', 'https://www.gzeic.edu.cn', 1973, 0),
    (37, '安顺职业技术学院', '安职', '12821', '专科', '公办', '高职高专', '安顺', '西秀区', 'https://www.aszy.edu.cn', 1956, 0),
    (38, '黔东南民族职业技术学院', '黔东南职院', '12822', '专科', '公办', '高职高专', '凯里', '凯里市', 'https://www.qdnpt.edu.cn', 2001, 0),
    (39, '黔南民族职业技术学院', '黔南职院', '12823', '专科', '公办', '高职高专', '都匀', '都匀市', 'https://www.qnzy.net', 2001, 0),
    (40, '遵义职业技术学院', '遵职', '12824', '专科', '公办', '高职高专', '遵义', '新蒲新区', 'https://www.zyzy.edu.cn', 1956, 0),
    (41, '贵州工业职业技术学院', '贵工业职院', '13052', '专科', '公办', '高职高专', '贵阳', '清镇市', 'https://www.gzky.edu.cn', 1958, 0),
    (42, '贵州电力职业技术学院', '贵电力职院', '13053', '专科', '公办', '高职高专', '贵阳', '清镇市', 'https://www.gzepi.edu.cn', 2002, 0),
    (43, '六盘水职业技术学院', '六职', '13051', '专科', '公办', '高职高专', '六盘水', '钟山区', 'https://www.lpszy.edu.cn', 2002, 0),
    (44, '黔西南民族职业技术学院', '黔西南职院', '13817', '专科', '公办', '高职高专', '兴义', '兴义市', 'https://www.qxnzy.edu.cn', 2004, 0),
    (45, '遵义医药高等专科学校', '遵义医专', '14011', '专科', '公办', '高职高专', '遵义', '新蒲新区', 'https://www.zunyiyx.edu.cn', 2006, 0),
    (46, '贵阳职业技术学院', '贵职', '14129', '专科', '公办', '高职高专', '贵阳', '观山湖区', 'https://www.gyvtc.edu.cn', 2007, 0),
    (47, '毕节职业技术学院', '毕职', '14198', '专科', '公办', '高职高专', '毕节', '金海湖新区', 'https://www.bjzyjsxy.edu.cn', 2008, 0),
    (48, '贵州职业技术学院', '贵职院', '14260', '专科', '公办', '高职高专', '贵阳', '观山湖区', 'https://www.gzvti.edu.cn', 2008, 0),
    (49, '贵阳幼儿师范高等专科学校', '贵阳幼专', '14466', '专科', '公办', '高职高专', '贵阳', '清镇市', 'https://www.gypec.edu.cn', 2012, 0),
    (50, '铜仁幼儿师范高等专科学校', '铜仁幼专', '14470', '专科', '公办', '高职高专', '铜仁', '碧江区', 'https://www.trpec.edu.cn', 2012, 0),
    (51, '黔南民族幼儿师范高等专科学校', '黔南幼专', '14497', '专科', '公办', '高职高专', '都匀', '贵定县', 'https://www.qnyz.edu.cn', 2014, 0),
    (52, '毕节医学高等专科学校', '毕节医专', '14499', '专科', '公办', '高职高专', '毕节', '金海湖新区', 'https://www.bjygz.edu.cn', 2014, 0),
    (53, '贵州建设职业技术学院', '贵建职院', '14516', '专科', '公办', '高职高专', '贵阳', '清镇市', 'https://www.gzcte.edu.cn', 2014, 0),
    (54, '毕节幼儿师范高等专科学校', '毕节幼专', '14539', '专科', '公办', '高职高专', '毕节', '金海湖新区', 'https://www.bjyz.edu.cn', 2015, 0),
    (55, '贵州农业职业学院', '贵农职院', '14549', '专科', '公办', '高职高专', '贵阳', '清镇市', 'https://www.gzavc.edu.cn', 2015, 0),
    (56, '贵州水利水电职业技术学院', '贵水电职院', '14577', '专科', '公办', '高职高专', '贵阳', '清镇市', 'https://www.gzsdxy.edu.cn', 2016, 0),
    (57, '贵州电子商务职业技术学院', '贵电商职院', '14578', '专科', '公办', '高职高专', '贵阳', '清镇市', 'https://www.gzdzswxy.edu.cn', 2016, 0),
    (58, '贵州电子科技职业学院', '贵电科职院', '14579', '专科', '公办', '高职高专', '贵阳', '花溪区', 'https://www.gzekxy.cn', 2016, 0),
    (59, '贵州装备制造职业学院', '贵装备职院', '14614', '专科', '公办', '高职高专', '贵阳', '清镇市', 'https://www.gzzzxy.cn', 2017, 0),
    (60, '贵州健康职业学院', '贵健康职院', '14615', '专科', '公办', '高职高专', '铜仁', '碧江区', 'https://www.gzjky.cn', 2017, 0),
    (61, '贵州食品工程职业学院', '贵食职院', '14617', '专科', '公办', '高职高专', '贵阳', '花溪区', 'https://www.gzspgc.edu.cn', 2017, 0),
    (62, '贵州经贸职业技术学院', '贵经贸职院', '14618', '专科', '公办', '高职高专', '都匀', '都匀市', 'https://www.gzjmzy.edu.cn', 2017, 0),
    (63, '贵州护理职业技术学院', '贵护职院', '14622', '专科', '公办', '高职高专', '都匀', '贵定县', 'https://www.gzhlxy.edu.cn', 2017, 0),
    (64, '六盘水幼儿师范高等专科学校', '六盘水幼专', '14630', '专科', '公办', '高职高专', '六盘水', '钟山区', 'https://www.lpsyz.edu.cn', 2018, 0),
    (65, '毕节工业职业技术学院', '毕节工职院', '14648', '专科', '公办', '高职高专', '毕节', '金海湖新区', 'https://www.bjgyxy.cn', 2018, 0),
    (66, '贵州机电职业技术学院', '贵机电职院', '14733', '专科', '公办', '高职高专', '都匀', '都匀市', 'https://www.gzjdxy.cn', 2020, 0),
    (67, '贵州财经职业学院', '贵财经职院', '14734', '专科', '公办', '高职高专', '贵阳', '清镇市', 'https://www.gzcjzy.edu.cn', 2020, 0),
    (68, '贵州文化旅游职业学院', '贵文旅职院', '14735', '专科', '公办', '高职高专', '贵阳', '清镇市', 'https://www.gzwly.edu.cn', 2020, 0),
    (69, '贵州航空职业技术学院', '贵航空职院', '14736', '专科', '公办', '高职高专', '贵阳', '花溪区', 'https://www.gzavc.cn', 2020, 0),
    (70, '贵州体育职业学院', '贵体育职院', '14737', '专科', '公办', '高职高专', '贵阳', '清镇市', 'https://www.gstzzy.cn', 2020, 0),
    (71, '贵州传媒职业学院', '贵传媒职院', '14738', '专科', '公办', '高职高专', '贵阳', '花溪区', 'https://www.gzcmzy.cn', 2020, 0),
    (72, '贵州生态能源职业学院', '贵生态职院', '14739', '专科', '公办', '高职高专', '贵阳', '花溪区', 'https://www.gzstny.cn', 2021, 0),
    (73, '黔东南理工职业学院', '黔东南理工', '14740', '专科', '公办', '高职高专', '凯里', '凯里市', 'https://www.qdnlg.cn', 2021, 0),
    # 专科 民办 (6所)
    (74, '贵州城市职业学院', '贵城市职院', '12851', '专科', '民办', '高职高专', '贵阳', '花溪区', 'https://www.gzcvc.cn', 2001, 0),
    (75, '贵州盛华职业学院', '贵盛华职院', '14371', '专科', '民办', '高职高专', '都匀', '惠水县', 'https://www.forerunner.edu.cn', 2011, 0),
    (76, '贵州工程职业学院', '贵工程职院', '14558', '专科', '民办', '高职高专', '铜仁', '德江县', 'https://www.gzgcxy.cn', 2015, 0),
    (77, '贵州工贸职业学院', '贵工贸职院', '14559', '专科', '民办', '高职高专', '毕节', '威宁县', 'https://www.gzgmxy.cn', 2015, 0),
    (78, '贵州应用技术职业学院', '贵应用职院', '14560', '专科', '民办', '高职高专', '都匀', '福泉市', 'https://www.gzyyjs.cn', 2016, 0),
    (79, '贵州民用航空职业学院', '贵民航职院', '14741', '专科', '民办', '高职高专', '安顺', '平坝区', 'https://www.gzmhhk.cn', 2021, 0),
    (80, '贵州铜仁数据职业学院', '铜仁数据', '14801', '专科', '民办', '高职高专', '铜仁', '碧江区', 'https://www.trsdxy.cn', 2020, 0),
]

# Generate SQL
lines = []
lines.append('-- 贵州高校数据平台 - 种子数据\n')
lines.append('-- 高校坐标来源：高德地图 Web服务 API 真实查询\n')
lines.append('-- 排名来源：用户提供的官方排名（1=最强）\n')
lines.append('-- 专升本/高考分数线、招生计划：待补充（需真实数据来源）\n')
lines.append('\n')
lines.append('-- 清空旧数据\n')
lines.append('DELETE FROM zhuanshengben_score;\n')
lines.append('DELETE FROM zhuanshengben_plan;\n')
lines.append('DELETE FROM province_control_line;\n')
lines.append('DELETE FROM admission_score;\n')
lines.append('DELETE FROM employment_rate;\n')
lines.append('DELETE FROM major_mapping;\n')
lines.append('DELETE FROM major;\n')
lines.append('DELETE FROM university;\n\n')

# Benke
benke = [s for s in schools if s[4] == '本科']
zhuanke = [s for s in schools if s[4] == '专科']

lines.append(f'-- =============================================\n')
lines.append(f'-- 高校基础信息（共 {len(schools)} 所）\n')
lines.append(f'-- =============================================\n\n')

# Benke INSERT
lines.append(f'-- 本科院校 ({len(benke)}所)\n')
lines.append('INSERT INTO university (name, short_name, code, type, nature, level, city, district, longitude, latitude, website, founded_year, is_zsb_target, rank_soft, status) VALUES\n')
rows = []
for s in benke:
    rank, name, sn, code, typ, nature, level, city, dist, web, year, zsb = s
    lng, lat = coord_map.get(name, (0, 0))
    if (lng, lat) == (0, 0):
        print(f"WARNING: No coords for {name}")
    rows.append(f"('{name}', '{sn}', '{code}', '本科', '{nature}', '{level}', '{city}', '{dist}', {lng:.6f}, {lat:.6f}, '{web}', {year}, {zsb}, {rank}, 1)")
lines.append(',\n'.join(rows) + ';\n\n')

# Zhuanke INSERT
lines.append(f'-- 专科院校 ({len(zhuanke)}所)\n')
lines.append('INSERT INTO university (name, short_name, code, type, nature, level, city, district, longitude, latitude, website, founded_year, is_zsb_target, status) VALUES\n')
rows2 = []
for s in zhuanke:
    rank, name, sn, code, typ, nature, level, city, dist, web, year, zsb = s
    lng, lat = coord_map.get(name, (0, 0))
    if (lng, lat) == (0, 0):
        print(f"WARNING: No coords for {name}")
    rows2.append(f"('{name}', '{sn}', '{code}', '专科', '{nature}', '{level}', '{city}', '{dist}', {lng:.6f}, {lat:.6f}, '{web}', {year}, {zsb}, 1)")
lines.append(',\n'.join(rows2) + ';\n\n')

lines.append('-- =============================================\n')
lines.append('-- 专升本分数线：待补充（需真实数据来源）\n')
lines.append('-- =============================================\n\n')
lines.append('-- =============================================\n')
lines.append('-- 专升本招生计划：待补充（需真实数据来源）\n')
lines.append('-- =============================================\n\n')
lines.append('-- =============================================\n')
lines.append('-- 省控线：待补充（需真实数据来源）\n')
lines.append('-- =============================================\n\n')
lines.append('-- =============================================\n')
lines.append('-- 高考录取分数线：待补充（需真实数据来源）\n')
lines.append('-- =============================================\n')

with open('server/src/main/resources/data.sql', 'w', encoding='utf-8') as f:
    f.writelines(lines)

print(f"Done! Total: {len(schools)} (本科 {len(benke)} + 专科 {len(zhuanke)})")
