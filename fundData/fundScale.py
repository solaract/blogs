import re
import json
import requests

def parse_js_value(raw_value):
    """智能解析JS变量值"""
    raw_value = raw_value.strip()
    
    # 处理基础类型
    if raw_value in ('true', 'false'):
        return raw_value == 'true'
    if raw_value == 'null':
        return None
    if raw_value.startswith(('"', "'")) and len(raw_value) > 1:
        return raw_value[1:-1].replace("'", '"')  # 统一双引号
    
    # 处理数字
    try:
        return float(raw_value) if '.' in raw_value else int(raw_value)
    except ValueError:
        pass
    
    # 处理复杂结构
    try:
        # 转换JS对象为合法JSON：处理未加引号的键名
        json_str = re.sub(r'([{,]\s*)(\w+)(\s*:)', r'\1"\2"\3', raw_value)
        # 移除尾随逗号
        json_str = re.sub(r',(\s*[}\]])', r'\1', json_str)
        # 单引号转双引号
        json_str = json_str.replace("'", '"')
        return json.loads(json_str)
    except json.JSONDecodeError as e:
        print(f"JSON解析错误: {e}")
        return raw_value  # 保留原始值

def fetch_fund_data(fund_code):
    url = f"https://fund.eastmoney.com/pingzhongdata/{fund_code}.js"
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        content = re.sub(r'/\*.*?\*/', '', response.text, flags=re.DOTALL)  # 移除注释
        
        # 提取所有var变量，改进正则以匹配多行值
        pattern = r"var\s+(\w+)\s*=\s*([^;]*);"
        matches = re.findall(pattern, content, re.DOTALL)
        
        result = {}
        for var_name, raw_value in matches:
            result[var_name] = parse_js_value(raw_value)
        
        return result
        
    except Exception as e:
        print(f"解析失败: {str(e)}")
        return None

# 示例用法
fund_code = "110020"
data = fetch_fund_data(fund_code)
print(data['Data_fluctuationScale']['series'][-1]['y'])

# if data:
#     print(json.dumps(data, indent=2, ensure_ascii=False))
#     with open(f"fund_{fund_code}.json", "w", encoding="utf-8") as f:
#         json.dump(data, f, ensure_ascii=False, indent=2)

