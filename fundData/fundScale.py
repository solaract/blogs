import re
import json
import requests

def fetch_fund_scale(fund_code):
    url = f"https://fund.eastmoney.com/pingzhongdata/{fund_code}.js"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        js_content = response.text
        
        # 提取Data_fluctuationScale变量
        pattern = r"var Data_fluctuationScale = (.*?);"
        match = re.search(pattern, js_content, re.DOTALL)
        if not match:
            return None
        
        # 处理JSON格式并解析
        json_str = match.group(1).replace("'", '"')  # 确保双引号
        data = json.loads(json_str)
        
        # 提取规模数据
        length = len(data["series"])
        if data.get("series") and length > 0:
            return data["series"][length - 1].get("y")
        return None
        
    except requests.exceptions.RequestException as e:
        print(f"请求失败: {e}")
    except json.JSONDecodeError as e:
        print(f"JSON解析失败: {e}")
    except Exception as e:
        print(f"发生错误: {e}")
    return None

# # 示例用法
# fund_code = "110020"
# scale = fetch_fund_scale(fund_code)
# print(f"基金代码 {fund_code} 的规模变动数据为: {scale}")