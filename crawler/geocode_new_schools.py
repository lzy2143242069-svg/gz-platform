"""Geocode newly added Guizhou universities"""
import json, time, urllib.request, urllib.parse

AMAP_KEY = "a904f2f25aae522d9b842df7797779ca"

new_schools = [
    {"name": "贵州警察学院", "city": "贵阳", "district": ""},
    {"name": "贵阳人文科技学院", "city": "贵阳", "district": ""},
    {"name": "贵州工商职业大学", "city": "贵阳", "district": ""},
    {"name": "贵州航天职业技术学院", "city": "遵义", "district": ""},
    {"name": "贵州电力职业技术学院", "city": "贵阳", "district": ""},
    {"name": "遵义医药高等专科学校", "city": "遵义", "district": ""},
    {"name": "贵阳幼儿师范高等专科学校", "city": "贵阳", "district": ""},
    {"name": "黔南民族幼儿师范高等专科学校", "city": "都匀", "district": ""},
    {"name": "毕节幼儿师范高等专科学校", "city": "毕节", "district": ""},
    {"name": "贵州电子商务职业技术学院", "city": "贵阳", "district": ""},
    {"name": "贵州电子科技职业学院", "city": "贵阳", "district": ""},
    {"name": "贵州装备制造职业学院", "city": "贵阳", "district": ""},
    {"name": "贵州健康职业学院", "city": "铜仁", "district": ""},
    {"name": "贵州经贸职业技术学院", "city": "都匀", "district": ""},
    {"name": "六盘水幼儿师范高等专科学校", "city": "六盘水", "district": ""},
    {"name": "毕节工业职业技术学院", "city": "毕节", "district": ""},
    {"name": "贵州机电职业技术学院", "city": "都匀", "district": ""},
    {"name": "贵州财经职业学院", "city": "贵阳", "district": ""},
    {"name": "贵州文化旅游职业学院", "city": "贵阳", "district": ""},
    {"name": "贵州航空职业技术学院", "city": "贵阳", "district": ""},
    {"name": "贵州体育职业学院", "city": "贵阳", "district": ""},
    {"name": "贵州传媒职业学院", "city": "贵阳", "district": ""},
    {"name": "贵州生态能源职业学院", "city": "贵阳", "district": ""},
    {"name": "黔东南理工职业学院", "city": "凯里", "district": ""},
    {"name": "贵州城市职业学院", "city": "贵阳", "district": ""},
    {"name": "贵州盛华职业学院", "city": "都匀", "district": ""},
    {"name": "贵州工程职业学院", "city": "铜仁", "district": ""},
    {"name": "贵州工贸职业学院", "city": "毕节", "district": ""},
    {"name": "贵州应用技术职业学院", "city": "都匀", "district": ""},
    {"name": "贵州民用航空职业学院", "city": "安顺", "district": ""},
]

results = []
failed = []

for i, uni in enumerate(new_schools):
    kw = urllib.parse.quote(uni["name"])
    c = urllib.parse.quote(uni["city"])
    url = f"https://restapi.amap.com/v3/place/text?key={AMAP_KEY}&keywords={kw}&city={c}&output=json"
    try:
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode("utf-8"))
        if data.get("status") == "1" and data.get("pois"):
            poi = data["pois"][0]
            lng, lat = poi["location"].split(",")
            results.append({"name": uni["name"], "city": uni["city"], "lng": float(lng), "lat": float(lat), "address": poi.get("address", "")})
            print(f"[{i+1}/{len(new_schools)}] OK {uni['name']}: {lng}, {lat}")
        else:
            failed.append(uni["name"])
            print(f"[{i+1}/{len(new_schools)}] MISS {uni['name']}")
    except Exception as e:
        failed.append(uni["name"])
        print(f"[{i+1}/{len(new_schools)}] ERR {uni['name']}: {e}")
    time.sleep(0.3)

with open("crawler/data/new_schools_coords.json", "w", encoding="utf-8") as f:
    json.dump(results, f, ensure_ascii=False, indent=2)

print(f"\nDone: {len(results)} OK, {len(failed)} failed")
if failed:
    print(f"Failed: {failed}")
