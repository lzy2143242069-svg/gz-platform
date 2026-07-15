"""
贵州高校真实经纬度获取 — 高德地图 Web 服务 API
"""
import json, time, urllib.request, urllib.parse

AMAP_KEY = "a904f2f25aae522d9b842df7797779ca"

universities = [
    # 贵阳 本科
    {"name": "贵州大学", "city": "贵阳", "district": "花溪区"},
    {"name": "贵州医科大学", "city": "贵阳", "district": "云岩区"},
    {"name": "贵州师范大学", "city": "贵阳", "district": "花溪区"},
    {"name": "贵州财经大学", "city": "贵阳", "district": "花溪区"},
    {"name": "贵州民族大学", "city": "贵阳", "district": "花溪区"},
    {"name": "贵州中医药大学", "city": "贵阳", "district": "花溪区"},
    {"name": "贵州师范学院", "city": "贵阳", "district": "乌当区"},
    {"name": "贵州理工学院", "city": "贵阳", "district": "花溪区"},
    {"name": "贵阳学院", "city": "贵阳", "district": "南明区"},
    {"name": "贵州商学院", "city": "贵阳", "district": "白云区"},
    {"name": "贵阳康养职业大学", "city": "贵阳", "district": "观山湖区"},
    {"name": "贵州中医药大学时珍学院", "city": "贵阳", "district": ""},
    {"name": "贵阳信息科技学院", "city": "贵阳", "district": ""},
    {"name": "贵州医科大学神奇民族医药学院", "city": "贵阳", "district": ""},
    # 遵义
    {"name": "遵义医科大学", "city": "遵义", "district": ""},
    {"name": "遵义师范学院", "city": "遵义", "district": ""},
    {"name": "遵义医科大学医学与科技学院", "city": "遵义", "district": ""},
    {"name": "茅台学院", "city": "遵义", "district": ""},
    # 都匀
    {"name": "黔南民族师范学院", "city": "都匀", "district": ""},
    {"name": "贵州黔南经济学院", "city": "都匀", "district": ""},
    {"name": "贵州黔南科技学院", "city": "都匀", "district": ""},
    # 凯里
    {"name": "凯里学院", "city": "凯里", "district": ""},
    # 其他
    {"name": "六盘水师范学院", "city": "六盘水", "district": ""},
    {"name": "安顺学院", "city": "安顺", "district": ""},
    {"name": "兴义民族师范学院", "city": "兴义", "district": ""},
    {"name": "贵州工程应用技术学院", "city": "毕节", "district": ""},
    {"name": "铜仁学院", "city": "铜仁", "district": ""},
    # 贵阳 专科
    {"name": "贵州交通职业技术学院", "city": "贵阳", "district": "清镇市"},
    {"name": "贵州轻工职业技术学院", "city": "贵阳", "district": "花溪区"},
    {"name": "贵州职业技术学院", "city": "贵阳", "district": "观山湖区"},
    {"name": "贵州工业职业技术学院", "city": "贵阳", "district": "清镇市"},
    {"name": "贵阳职业技术学院", "city": "贵阳", "district": "观山湖区"},
    {"name": "贵州护理职业技术学院", "city": "贵阳", "district": "花溪区"},
    {"name": "贵州建设职业技术学院", "city": "贵阳", "district": "清镇市"},
    {"name": "贵州农业职业学院", "city": "贵阳", "district": ""},
    {"name": "贵州水利水电职业技术学院", "city": "贵阳", "district": "清镇市"},
    {"name": "贵州食品工程职业学院", "city": "贵阳", "district": ""},
    # 其他市州 专科
    {"name": "贵州电子信息职业技术学院", "city": "凯里", "district": ""},
    {"name": "黔南民族医学高等专科学校", "city": "都匀", "district": ""},
    {"name": "遵义职业技术学院", "city": "遵义", "district": ""},
    {"name": "毕节医学高等专科学校", "city": "毕节", "district": ""},
    {"name": "铜仁幼儿师范高等专科学校", "city": "铜仁", "district": ""},
    {"name": "铜仁职业技术大学", "city": "铜仁", "district": ""},
    {"name": "铜仁数据职业学院", "city": "铜仁", "district": ""},
    {"name": "毕节职业技术学院", "city": "毕节", "district": ""},
    {"name": "安顺职业技术学院", "city": "安顺", "district": ""},
    {"name": "六盘水职业技术学院", "city": "六盘水", "district": ""},
    {"name": "黔西南民族职业技术学院", "city": "兴义", "district": ""},
]

results = []
failed = []

for i, uni in enumerate(universities):
    keywords = uni["name"]
    city = uni["city"]
    url = f"https://restapi.amap.com/v3/place/text?key={AMAP_KEY}&keywords={urllib.parse.quote(keywords)}&city={urllib.parse.quote(city)}&types=141200&output=json"

    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))

        if data.get("status") == "1" and data.get("pois"):
            poi = data["pois"][0]
            lng, lat = poi["location"].split(",")
            results.append({
                "name": uni["name"],
                "city": uni["city"],
                "lng": float(lng),
                "lat": float(lat),
                "address": poi.get("address", ""),
            })
            print(f"[{i+1}/{len(universities)}] OK {uni['name']}: {lng}, {lat}")
        else:
            # Fallback: search without type filter
            url2 = f"https://restapi.amap.com/v3/place/text?key={AMAP_KEY}&keywords={urllib.parse.quote(keywords)}&city={urllib.parse.quote(city)}&output=json"
            req2 = urllib.request.Request(url2)
            with urllib.request.urlopen(req2, timeout=10) as resp2:
                data2 = json.loads(resp2.read().decode("utf-8"))
            if data2.get("status") == "1" and data2.get("pois"):
                poi2 = data2["pois"][0]
                lng2, lat2 = poi2["location"].split(",")
                results.append({
                    "name": uni["name"],
                    "city": uni["city"],
                    "lng": float(lng2),
                    "lat": float(lat2),
                    "address": poi2.get("address", ""),
                })
                print(f"[{i+1}/{len(universities)}] OK (fallback) {uni['name']}: {lng2}, {lat2}")
            else:
                failed.append(uni["name"])
                print(f"[{i+1}/{len(universities)}] MISS {uni['name']}: no result")
    except Exception as e:
        failed.append(uni["name"])
        print(f"[{i+1}/{len(universities)}] ERR {uni['name']}: {e}")

    time.sleep(0.3)

with open("crawler/data/university_coords.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\n=== Done: {len(results)} OK, {len(failed)} failed ===")
if failed:
    print(f"Failed: {failed}")
