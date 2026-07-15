"""导出工具 - 将 JSON 数据转为 SQL INSERT 语句"""
import json
import os


def json_to_sql_universities(json_path, sql_path):
    """将 universities.json 转为 SQL INSERT"""
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    with open(sql_path, "w", encoding="utf-8") as f:
        f.write("-- 由爬虫自动生成\n")
        f.write("-- 高校基础信息\n\n")
        for uni in data:
            name = uni["name"].replace("'", "''")
            short_name = uni.get("short_name", "").replace("'", "''")
            code = uni.get("code", "")
            u_type = uni["type"]
            nature = uni["nature"]
            level = uni.get("level", "")
            city = uni["city"]
            lng = uni.get("longitude", "NULL")
            lat = uni.get("latitude", "NULL")
            is_zsb = 1 if uni.get("is_zsb_target") else 0

            lng_str = f"{lng}" if lng != "NULL" else "NULL"
            lat_str = f"{lat}" if lat != "NULL" else "NULL"

            f.write(
                f"INSERT INTO university (name, short_name, code, type, nature, level, city, longitude, latitude, is_zsb_target, status) VALUES "
                f"('{name}', '{short_name}', '{code}', '{u_type}', '{nature}', '{level}', '{city}', {lng_str}, {lat_str}, {is_zsb}, 1);\n"
            )

    print(f"已生成 SQL: {sql_path} ({len(data)} 条)")


def main():
    base_dir = os.path.dirname(__file__)
    data_dir = os.path.join(base_dir, "data")

    json_path = os.path.join(data_dir, "universities.json")
    sql_path = os.path.join(data_dir, "universities.sql")

    if os.path.exists(json_path):
        json_to_sql_universities(json_path, sql_path)
    else:
        print(f"未找到 {json_path}，请先运行 universities.py")


if __name__ == "__main__":
    main()
