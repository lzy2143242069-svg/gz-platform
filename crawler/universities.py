"""贵州高校基础信息采集脚本
数据源: 阳光高考网 / 掌上高考
"""
import requests
import json
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from config import HEADERS, random_delay

# 贵州省全部高校名单（手动整理，作为爬虫入口）
GUIZHOU_UNIVERSITIES = [
    # 本科 - 公办
    {"name": "贵州大学", "code": "10657", "city": "贵阳", "type": "本科", "nature": "公办", "level": "211/双一流"},
    {"name": "贵州医科大学", "code": "10660", "city": "贵阳", "type": "本科", "nature": "公办", "level": "普通本科"},
    {"name": "贵州师范大学", "code": "10663", "city": "贵阳", "type": "本科", "nature": "公办", "level": "普通本科"},
    {"name": "贵州财经大学", "code": "10671", "city": "贵阳", "type": "本科", "nature": "公办", "level": "普通本科"},
    {"name": "贵州民族大学", "code": "10672", "city": "贵阳", "type": "本科", "nature": "公办", "level": "普通本科"},
    {"name": "贵州中医药大学", "code": "10662", "city": "贵阳", "type": "本科", "nature": "公办", "level": "普通本科"},
    {"name": "遵义医科大学", "code": "10661", "city": "遵义", "type": "本科", "nature": "公办", "level": "普通本科"},
    {"name": "遵义师范学院", "code": "10664", "city": "遵义", "type": "本科", "nature": "公办", "level": "普通本科"},
    {"name": "贵州师范学院", "code": "10667", "city": "贵阳", "type": "本科", "nature": "公办", "level": "普通本科"},
    {"name": "贵州理工学院", "code": "14440", "city": "贵阳", "type": "本科", "nature": "公办", "level": "普通本科"},
    {"name": "贵阳学院", "code": "10976", "city": "贵阳", "type": "本科", "nature": "公办", "level": "普通本科"},
    {"name": "黔南民族师范学院", "code": "10670", "city": "都匀", "type": "本科", "nature": "公办", "level": "普通本科"},
    {"name": "铜仁学院", "code": "10665", "city": "铜仁", "type": "本科", "nature": "公办", "level": "普通本科"},
    {"name": "凯里学院", "code": "10669", "city": "凯里", "type": "本科", "nature": "公办", "level": "普通本科"},
    {"name": "六盘水师范学院", "code": "10977", "city": "六盘水", "type": "本科", "nature": "公办", "level": "普通本科"},
    {"name": "安顺学院", "code": "10667", "city": "安顺", "type": "本科", "nature": "公办", "level": "普通本科"},
    {"name": "兴义民族师范学院", "code": "10666", "city": "兴义", "type": "本科", "nature": "公办", "level": "普通本科"},
    {"name": "贵州工程应用技术学院", "code": "10668", "city": "毕节", "type": "本科", "nature": "公办", "level": "普通本科"},
    {"name": "贵阳康养职业大学", "code": "11652", "city": "贵阳", "type": "本科", "nature": "公办", "level": "职业本科"},
    {"name": "贵州商学院", "code": "11731", "city": "贵阳", "type": "本科", "nature": "公办", "level": "普通本科"},
    # 本科 - 民办
    {"name": "贵州中医药大学时珍学院", "code": "13647", "city": "贵阳", "type": "本科", "nature": "民办", "level": "独立学院"},
    {"name": "贵州黔南经济学院", "code": "13648", "city": "都匀", "type": "本科", "nature": "民办", "level": "独立学院"},
    {"name": "贵州黔南科技学院", "code": "13649", "city": "都匀", "type": "本科", "nature": "民办", "level": "独立学院"},
    {"name": "贵阳信息科技学院", "code": "13650", "city": "贵阳", "type": "本科", "nature": "民办", "level": "独立学院"},
    {"name": "贵州医科大学神奇民族医药学院", "code": "13676", "city": "贵阳", "type": "本科", "nature": "民办", "level": "独立学院"},
    {"name": "遵义医科大学医学与科技学院", "code": "13653", "city": "遵义", "type": "本科", "nature": "民办", "level": "独立学院"},
    {"name": "茅台学院", "code": "14625", "city": "遵义", "type": "本科", "nature": "民办", "level": "普通本科"},
    # 专科
    {"name": "贵州交通职业技术学院", "code": "12222", "city": "贵阳", "type": "专科", "nature": "公办", "level": "高职高专"},
    {"name": "贵州轻工职业技术学院", "code": "13818", "city": "贵阳", "type": "专科", "nature": "公办", "level": "高职高专"},
    {"name": "贵州职业技术学院", "code": "14260", "city": "贵阳", "type": "专科", "nature": "公办", "level": "高职高专"},
    {"name": "贵州电子信息职业技术学院", "code": "12336", "city": "凯里", "type": "专科", "nature": "公办", "level": "高职高专"},
    {"name": "贵州工业职业技术学院", "code": "13052", "city": "贵阳", "type": "专科", "nature": "公办", "level": "高职高专"},
    {"name": "贵阳职业技术学院", "code": "14129", "city": "贵阳", "type": "专科", "nature": "公办", "level": "高职高专"},
    {"name": "遵义职业技术学院", "code": "12824", "city": "遵义", "type": "专科", "nature": "公办", "level": "高职高专"},
    {"name": "贵州护理职业技术学院", "code": "14622", "city": "贵阳", "type": "专科", "nature": "公办", "level": "高职高专"},
    {"name": "黔南民族医学高等专科学校", "code": "11663", "city": "都匀", "type": "专科", "nature": "公办", "level": "高职高专"},
    {"name": "毕节医学高等专科学校", "code": "14499", "city": "毕节", "type": "专科", "nature": "公办", "level": "高职高专"},
]

# 贵州省各市经纬度 (用于地图标注)
CITY_COORDS = {
    "贵阳": (106.7134, 26.6470),
    "遵义": (106.9273, 27.7254),
    "都匀": (107.5175, 26.2592),
    "铜仁": (109.1810, 27.7240),
    "凯里": (107.9810, 26.5660),
    "六盘水": (104.8300, 26.5920),
    "安顺": (105.9470, 26.2530),
    "兴义": (104.8960, 25.0890),
    "毕节": (105.2910, 27.3040),
}


def enrich_with_coords(universities):
    """为高校添加经纬度坐标"""
    for uni in universities:
        city = uni.get("city", "")
        if city in CITY_COORDS:
            base_lng, base_lat = CITY_COORDS[city]
            # 同城高校添加小偏移，避免重叠
            import random
            uni["longitude"] = base_lng + random.uniform(-0.02, 0.02)
            uni["latitude"] = base_lat + random.uniform(-0.02, 0.02)
    return universities


def export_to_json(universities, output_path="data/universities.json"):
    """导出为 JSON"""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(universities, f, ensure_ascii=False, indent=2)
    print(f"已导出 {len(universities)} 所高校到 {output_path}")


def main():
    print("=== 贵州高校基础信息采集 ===")
    print(f"共 {len(GUIZHOU_UNIVERSITIES)} 所高校")

    universities = enrich_with_coords(GUIZHOU_UNIVERSITIES)

    output_dir = os.path.join(os.path.dirname(__file__), "data")
    export_to_json(universities, os.path.join(output_dir, "universities.json"))

    print("采集完成！")


if __name__ == "__main__":
    main()
