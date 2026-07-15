"""爬虫配置"""
import random

HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
}

def random_delay(min_sec=2, max_sec=5):
    """礼貌延迟，避免被封"""
    import time
    time.sleep(random.uniform(min_sec, max_sec))
