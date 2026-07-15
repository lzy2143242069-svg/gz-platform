"""Generate data.sql with real coordinates from Amap API results"""
import json

with open('crawler/data/university_coords.json', 'r', encoding='utf-8') as f:
    coords = json.load(f)

coord_map = {c['name']: (c['lng'], c['lat']) for c in coords}

benke_data = [
    ('贵州大学', '贵大', '10657', '公办', '211/双一流', '贵阳', '花溪区', 'https://www.gzu.edu.cn', 1902, 0, 87),
    ('贵州医科大学', '贵医', '10660', '公办', '普通本科', '贵阳', '云岩区', 'https://www.gmc.edu.cn', 1938, 1, 350),
    ('贵州师范大学', '贵师大', '10663', '公办', '普通本科', '贵阳', '云岩区', 'https://www.gznu.edu.cn', 1941, 1, 260),
    ('贵州财经大学', '贵财', '10671', '公办', '普通本科', '贵阳', '花溪区', 'https://www.gzufe.edu.cn', 1958, 1, 370),
    ('贵州民族大学', '贵民大', '10672', '公办', '普通本科', '贵阳', '花溪区', 'https://www.gzmu.edu.cn', 1951, 1, 380),
    ('贵州中医药大学', '贵中医', '10662', '公办', '普通本科', '贵阳', '花溪区', 'https://www.gzucm.edu.cn', 1965, 1, 420),
    ('遵义医科大学', '遵医', '10661', '公办', '普通本科', '遵义', '新蒲新区', 'https://www.zmc.edu.cn', 1947, 1, 300),
    ('遵义师范学院', '遵师', '10664', '公办', '普通本科', '遵义', '红花岗区', 'https://www.zync.edu.cn', 1907, 1, 500),
    ('贵州师范学院', '贵师院', '10667', '公办', '普通本科', '贵阳', '乌当区', 'https://www.gznc.edu.cn', 1978, 1, 550),
    ('贵州理工学院', '贵理工', '14440', '公办', '普通本科', '贵阳', '花溪区', 'https://www.git.edu.cn', 2013, 1, 490),
    ('贵阳学院', '贵院', '10976', '公办', '普通本科', '贵阳', '南明区', 'https://www.gyu.cn', 1978, 1, 560),
    ('黔南民族师范学院', '黔南师院', '10670', '公办', '普通本科', '都匀', '都匀市', 'https://www.sgmtu.edu.cn', 1958, 1, 510),
    ('铜仁学院', '铜院', '10665', '公办', '普通本科', '铜仁', '碧江区', 'https://www.trxy.edu.cn', 1920, 1, 530),
    ('凯里学院', '凯院', '10669', '公办', '普通本科', '凯里', '凯里市', 'https://www.kluniv.edu.cn', 1958, 1, 540),
    ('六盘水师范学院', '六师', '10977', '公办', '普通本科', '六盘水', '钟山区', 'https://www.lpssy.edu.cn', 1978, 1, 570),
    ('安顺学院', '安院', '10667', '公办', '普通本科', '安顺', '西秀区', 'https://www.asu.edu.cn', 1938, 1, 555),
    ('兴义民族师范学院', '兴义师院', '10666', '公办', '普通本科', '兴义', '兴义市', 'https://www.xynun.edu.cn', 1813, 1, 565),
    ('贵州工程应用技术学院', '贵工程', '10668', '公办', '普通本科', '毕节', '七星关区', 'https://www.gues.edu.cn', 1938, 1, 545),
    ('贵阳康养职业大学', '贵康养', '11652', '公办', '职业本科', '贵阳', '观山湖区', 'https://www.gykz.edu.cn', 2021, 0, None),
    ('贵州商学院', '贵商', '11731', '公办', '普通本科', '贵阳', '白云区', 'https://www.gzcc.edu.cn', 2015, 1, 580),
    ('贵州中医药大学时珍学院', '时珍学院', '13647', '民办', '独立学院', '贵阳', '花溪区', 'https://www.gzszk.edu.cn', 2001, 0, None),
    ('贵州黔南经济学院', '贵经院', '13648', '民办', '独立学院', '都匀', '都匀市', 'https://www.gzqjxy.edu.cn', 2001, 0, None),
    ('贵州黔南科技学院', '贵科院', '13649', '民办', '独立学院', '都匀', '都匀市', 'https://www.gzqkkj.edu.cn', 2001, 0, None),
    ('贵阳信息科技学院', '贵信科', '13650', '民办', '独立学院', '贵阳', '花溪区', 'https://www.gyist.edu.cn', 2001, 0, None),
    ('贵州医科大学神奇民族医药学院', '神奇学院', '13676', '民办', '独立学院', '贵阳', '花溪区', 'https://www.gysqxy.edu.cn', 2004, 0, None),
    ('遵义医科大学医学与科技学院', '遵医科技', '13653', '民办', '独立学院', '遵义', '新蒲新区', 'https://www.zmckjxy.edu.cn', 2001, 0, None),
    ('茅台学院', '茅院', '14625', '民办', '普通本科', '遵义', '仁怀市', 'https://www.mtxy.edu.cn', 2017, 0, None),
    ('铜仁职业技术大学', '铜仁职大', '13055', '公办', '职业本科', '铜仁', '碧江区', 'https://www.trkxy.cn', 2002, 1, None),
]

zhuanke_data = [
    ('贵州交通职业技术学院', '贵交职院', '12222', '公办', '高职高专', '贵阳', '清镇市', 'https://www.gzjtzy.edu.cn', 1958, 0),
    ('贵州轻工职业技术学院', '贵轻职院', '13818', '公办', '高职高专', '贵阳', '花溪区', 'https://www.gzqy.edu.cn', 1978, 0),
    ('贵州职业技术学院', '贵职院', '14260', '公办', '高职高专', '贵阳', '观山湖区', 'https://www.gzvti.edu.cn', 2008, 0),
    ('贵州电子信息职业技术学院', '贵电子职院', '12336', '公办', '高职高专', '凯里', '凯里市', 'https://www.gzeic.edu.cn', 1973, 0),
    ('贵州工业职业技术学院', '贵工业职院', '13052', '公办', '高职高专', '贵阳', '清镇市', 'https://www.gzky.edu.cn', 1958, 0),
    ('贵阳职业技术学院', '贵职', '14129', '公办', '高职高专', '贵阳', '观山湖区', 'https://www.gyvtc.edu.cn', 2007, 0),
    ('遵义职业技术学院', '遵职', '12824', '公办', '高职高专', '遵义', '新蒲新区', 'https://www.zyzy.edu.cn', 1956, 0),
    ('贵州护理职业技术学院', '贵护职院', '14622', '公办', '高职高专', '贵阳', '花溪区', 'https://www.gzhlxy.edu.cn', 2017, 0),
    ('黔南民族医学高等专科学校', '黔南医专', '11663', '公办', '高职高专', '都匀', '都匀市', 'https://www.qnyz.edu.cn', 1985, 0),
    ('毕节医学高等专科学校', '毕节医专', '14499', '公办', '高职高专', '毕节', '金海湖新区', 'https://www.bjygz.edu.cn', 2014, 0),
    ('铜仁幼儿师范高等专科学校', '铜仁幼专', '14470', '公办', '高职高专', '铜仁', '碧江区', 'https://www.trpec.edu.cn', 2012, 0),
    ('毕节职业技术学院', '毕职', '14198', '公办', '高职高专', '毕节', '金海湖新区', 'https://www.bjzyjsxy.edu.cn', 2008, 0),
    ('黔东南民族职业技术学院', '黔东南职院', '12822', '公办', '高职高专', '凯里', '凯里市', 'https://www.qdnpt.edu.cn', 2001, 0),
    ('安顺职业技术学院', '安职', '12821', '公办', '高职高专', '安顺', '西秀区', 'https://www.aszy.edu.cn', 1956, 0),
    ('六盘水职业技术学院', '六职', '13051', '公办', '高职高专', '六盘水', '钟山区', 'https://www.lpszy.edu.cn', 2002, 0),
    ('黔西南民族职业技术学院', '黔西南职院', '13817', '公办', '高职高专', '兴义', '兴义市', 'https://www.qxnzy.edu.cn', 2004, 0),
    ('贵州建设职业技术学院', '贵建职院', '14516', '公办', '高职高专', '贵阳', '清镇市', 'https://www.gzcte.edu.cn', 2014, 0),
    ('贵州农业职业学院', '贵农职院', '14549', '公办', '高职高专', '贵阳', '清镇市', 'https://www.gzavc.edu.cn', 2015, 0),
    ('贵州水利水电职业技术学院', '贵水电职院', '14577', '公办', '高职高专', '贵阳', '清镇市', 'https://www.gzsdxy.edu.cn', 2016, 0),
    ('贵州食品工程职业学院', '贵食职院', '14617', '公办', '高职高专', '贵阳', '花溪区', 'https://www.gzspgc.edu.cn', 2017, 0),
    ('铜仁数据职业学院', '铜仁数据', '14801', '民办', '高职高专', '铜仁', '碧江区', 'https://www.trsdxy.cn', 2020, 0),
]

lines = []
lines.append('-- 贵州高校数据平台 - 种子数据\n')
lines.append('-- 高校坐标来源：高德地图 Web服务 API 真实查询\n')
lines.append('-- 专升本/高考分数线、招生计划：待补充（需真实数据来源）\n')
lines.append('\n')
lines.append('-- =============================================\n')
lines.append('-- 高校基础信息\n')
lines.append('-- =============================================\n\n')

# 本科
lines.append(f'-- 本科院校 ({len(benke_data)}所)\n')
lines.append('INSERT INTO university (name, short_name, code, type, nature, level, city, district, longitude, latitude, website, founded_year, is_zsb_target, rank_soft, status) VALUES\n')
rows = []
for d in benke_data:
    name, sn, code, nature, level, city, dist, web, year, zsb, rank = d
    lng, lat = coord_map.get(name, (0, 0))
    rank_str = str(rank) if rank else 'NULL'
    rows.append(f"('{name}', '{sn}', '{code}', '本科', '{nature}', '{level}', '{city}', '{dist}', {lng:.6f}, {lat:.6f}, '{web}', {year}, {zsb}, {rank_str}, 1)")
lines.append(',\n'.join(rows) + ';\n\n')

# 专科
lines.append(f'-- 专科院校 ({len(zhuanke_data)}所)\n')
lines.append('INSERT INTO university (name, short_name, code, type, nature, level, city, district, longitude, latitude, website, founded_year, is_zsb_target, status) VALUES\n')
rows2 = []
for d in zhuanke_data:
    name, sn, code, nature, level, city, dist, web, year, zsb = d
    lng, lat = coord_map.get(name, (0, 0))
    rows2.append(f"('{name}', '{sn}', '{code}', '专科', '{nature}', '{level}', '{city}', '{dist}', {lng:.6f}, {lat:.6f}, '{web}', {year}, {zsb}, 1)")
lines.append(',\n'.join(rows2) + ';\n\n')

lines.append('-- =============================================\n')
lines.append('-- 专升本分数线：待补充（需真实数据来源）\n')
lines.append('-- 数据来源要求：贵州省招生考试院官网 / 各校招生简章\n')
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

# Verify
missing = []
for name in [d[0] for d in benke_data] + [d[0] for d in zhuanke_data]:
    if name not in coord_map:
        missing.append(name)
    elif coord_map[name] == (0, 0):
        missing.append(name)

print(f'Done! Benke: {len(benke_data)}, Zhuanke: {len(zhuanke_data)}, Total: {len(benke_data)+len(zhuanke_data)}')
if missing:
    print(f'Missing coords: {missing}')
else:
    print('All coordinates verified OK')
