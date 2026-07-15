"""
贵州高校真实经纬度获取脚本
使用 OpenStreetMap Nominatim 地理编码（免费，无需 API Key）
"""
import time
import json
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="guizhou_uni_platform/1.0")

# 贵州省所有高校（名称 + 城市 + 区县）
# 来源：阳光高考网 https://gaokao.chsi.com.cn/sch/schoolInfo--schId-369000,categoryId-10080,mindex-12.dhtml
# 以及各高校官网地址
universities = [
    # 贵阳 本科
    {"name": "贵州大学", "city": "贵阳", "query": "贵州大学 花溪区"},
    {"name": "贵州医科大学", "city": "贵阳", "query": "贵州医科大学 北京路"},
    {"name": "贵州师范大学", "city": "贵阳", "query": "贵州师范大学 花溪区"},
    {"name": "贵州财经大学", "city": "贵阳", "query": "贵州财经大学 花溪区"},
    {"name": "贵州民族大学", "city": "贵阳", "query": "贵州民族大学 花溪区"},
    {"name": "贵州中医药大学", "city": "贵阳", "query": "贵州中医药大学 花溪区"},
    {"name": "贵州师范学院", "city": "贵阳", "query": "贵州师范学院 乌当区"},
    {"name": "贵州理工学院", "city": "贵阳", "query": "贵州理工学院 花溪区"},
    {"name": "贵阳学院", "city": "贵阳", "query": "贵阳学院 龙洞堡"},
    {"name": "贵州商学院", "city": "贵阳", "query": "贵州商学院 白云区"},
    {"name": "贵阳康养职业大学", "city": "贵阳", "query": "贵阳康养职业大学 观山湖区"},
    {"name": "贵州中医药大学时珍学院", "city": "贵阳", "query": "贵州中医药大学时珍学院"},
    {"name": "贵阳信息科技学院", "city": "贵阳", "query": "贵阳信息科技学院"},
    {"name": "贵州医科大学神奇民族医药学院", "city": "贵阳", "query": "贵州医科大学神奇民族医药学院"},
    # 遵义 本科
    {"name": "遵义医科大学", "city": "遵义", "query": "遵义医科大学 新蒲新区"},
    {"name": "遵义师范学院", "city": "遵义", "query": "遵义师范学院"},
    {"name": "遵义医科大学医学与科技学院", "city": "遵义", "query": "遵义医科大学医学与科技学院"},
    {"name": "茅台学院", "city": "遵义", "query": "茅台学院 仁怀"},
    # 其他市州 本科
    {"name": "黔南民族师范学院", "city": "都匀", "query": "黔南民族师范学院"},
    {"name": "贵州黔南经济学院", "city": "都匀", "query": "贵州黔南经济学院"},
    {"name": "贵州黔南科技学院", "city": "都匀", "query": "贵州黔南科技学院"},
    {"name": "凯里学院", "city": "凯里", "query": "凯里学院"},
    {"name": "六盘水师范学院", "city": "六盘水", "query": "六盘水师范学院"},
    {"name": "安顺学院", "city": "安顺", "query": "安顺学院"},
    {"name": "兴义民族师范学院", "city": "兴义", "query": "兴义民族师范学院"},
    {"name": "贵州工程应用技术学院", "city": "毕节", "query": "贵州工程应用技术学院"},
    {"name": "铜仁学院", "city": "铜仁", "query": "铜仁学院"},
    # 贵阳 专科
    {"name": "贵州交通职业技术学院", "city": "贵阳", "query": "贵州交通职业技术学院 清镇"},
    {"name": "贵州轻工职业技术学院", "city": "贵阳", "query": "贵州轻工职业技术学院 花溪"},
    {"name": "贵州职业技术学院", "city": "贵阳", "query": "贵州职业技术学院 观山湖"},
    {"name": "贵州工业职业技术学院", "city": "贵阳", "query": "贵州工业职业技术学院 清镇"},
    {"name": "贵阳职业技术学院", "city": "贵阳", "query": "贵阳职业技术学院 观山湖"},
    {"name": "贵州护理职业技术学院", "city": "贵阳", "query": "贵州护理职业技术学院 花溪"},
    {"name": "贵州建设职业技术学院", "city": "贵阳", "query": "贵州建设职业技术学院 清镇"},
    {"name": "贵州农业职业学院", "city": "贵阳", "query": "贵州农业职业学院"},
    {"name": "贵州水利水电职业技术学院", "city": "贵阳", "query": "贵州水利水电职业技术学院 清镇"},
    {"name": "贵州食品工程职业学院", "city": "贵阳", "query": "贵州食品工程职业学院"},
    # 其他市州 专科
    {"name": "贵州电子信息职业技术学院", "city": "凯里", "query": "贵州电子信息职业技术学院"},
    {"name": "黔南民族医学高等专科学校", "city": "都匀", "query": "黔南民族医学高等专科学校"},
    {"name": "遵义职业技术学院", "city": "遵义", "query": "遵义职业技术学院"},
    {"name": "毕节医学高等专科学校", "city": "毕节", "query": "毕节医学高等专科学校"},
    {"name": "铜仁幼儿师范高等专科学校", "city": "铜仁", "query": "铜仁幼儿师范高等专科学校"},
    {"name": "铜仁职业技术大学", "city": "铜仁", "query": "铜仁职业技术大学"},
    {"name": "铜仁数据职业学院", "city": "铜仁", "query": "铜仁数据职业学院"},
    {"name": "毕节职业技术学院", "city": "毕节", "query": "毕节职业技术学院"},
    {"name": "安顺职业技术学院", "city": "安顺", "query": "安顺职业技术学院"},
    {"name": "六盘水职业技术学院", "city": "六盘水", "query": "六盘水职业技术学院"},
    {"name": "黔西南民族职业技术学院", "city": "兴义", "query": "黔西南民族职业技术学院"},
]

results = []
failed = []

for i, uni in enumerate(universities):
    try:
        loc = geolocator.geocode(f"{uni['query']}, 贵州省, 中国", timeout=10, language="zh")
        if loc:
            results.append({
                "name": uni["name"],
                "city": uni["city"],
                "lng": round(loc.longitude, 6),
                "lat": round(loc.latitude, 6),
                "address": loc.address,
            })
            print(f"[{i+1}/{len(universities)}] ✓ {uni['name']}: {loc.longitude:.6f}, {loc.latitude:.6f}")
        else:
            # Fallback: try with just city
            loc2 = geolocator.geocode(f"{uni['name']}, 贵州", timeout=10, language="zh")
            if loc2:
                results.append({
                    "name": uni["name"],
                    "city": uni["city"],
                    "lng": round(loc2.longitude, 6),
                    "lat": round(loc2.latitude, 6),
                    "address": loc2.address,
                })
                print(f"[{i+1}/{len(universities)}] ✓ {uni['name']} (fallback): {loc2.longitude:.6f}, {loc2.latitude:.6f}")
            else:
                failed.append(uni["name"])
                print(f"[{i+1}/{len(universities)}] ✗ {uni['name']}: 未找到")
    except Exception as e:
        failed.append(uni["name"])
        print(f"[{i+1}/{len(universities)}] ✗ {uni['name']}: {e}")
    time.sleep(1.1)  # Nominatim rate limit: 1 req/sec

# Save results
with open("crawler/data/university_coords.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\n完成: {len(results)} 成功, {len(failed)} 失败")
if failed:
    print(f"失败列表: {failed}")
print(f"结果已保存到 crawler/data/university_coords.json")
