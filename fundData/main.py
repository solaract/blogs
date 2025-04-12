import akshare as ak
import pandas as pd
import time
import os
from tqdm import tqdm
import fundScale  # 自定义模块，用于备用获取基金规模

# 常量定义
COLUMNS_ORDER = ['基金代码', '基金名称', '基金规模（亿）', '成立时间', '跟踪方式']
SLEEP_INTERVAL = 0.3  # 请求间隔防止频率过高


def get_hs300_fund_data(fund_type):
    """
    获取沪深300基金数据（含基金类型）
    :param fund_type: str, 可选 {"全部", "被动指数型", "增强指数型"}
    :return: DataFrame 包含基金代码、名称、规模、成立时间和跟踪方式的数据
    """
    # 获取原始基金数据
    fund_df = ak.fund_info_index_em(symbol="全部", indicator=fund_type)
    
    # 筛选目标基金
    hs300_funds = fund_df[fund_df['基金名称'].str.contains('沪深300', na=False)]
    hs300_funds = hs300_funds[['基金代码', '基金名称', '跟踪方式']].copy()
    
    # 准备数据容器
    scale_list, date_list = [], []
    
    # 创建进度条
    with tqdm(hs300_funds['基金代码'], 
             desc='获取基金详情', 
             unit='支',
             ncols=100) as pbar:
        
        for code in pbar:
            pbar.set_postfix_str(f"当前处理：{code}")
            time.sleep(SLEEP_INTERVAL)
            
            # 获取单支基金数据
            detail_df = _get_fund_detail(code, pbar)
            
            # 提取规模和成立时间
            scale_value = _get_fund_scale(code, detail_df, pbar)
            establish_date = _get_establishment_date(detail_df, pbar)
            
            scale_list.append(scale_value)
            date_list.append(establish_date)

    # 组装结果
    hs300_funds.insert(2, '基金规模（亿）', scale_list)
    hs300_funds.insert(3, '成立时间', date_list)
    return hs300_funds


def _get_fund_detail(code, progress_bar):
    """获取单支基金详细信息"""
    try:
        return ak.fund_individual_basic_info_xq(symbol=code)
    except Exception as e:
        progress_bar.write(f"⚠️ 基金 {code} 基本信息获取失败: {str(e)}")
        return pd.DataFrame()  # 返回空DataFrame防止后续处理出错


def _get_fund_scale(code, detail_df, progress_bar):
    """从详情数据中解析基金规模"""
    try:
        # print(detail_df)
        # 优先从主要接口获取
        if not detail_df.empty:
            scale_row = detail_df[detail_df['item'] == '最新规模']
            if not scale_row.empty:
                return _convert_scale(scale_row.iloc[0]['value'])
            
        # 主接口无数据时尝试备用接口
        backup_data = fundScale.fetch_fund_data(code)
        backup_scale = backup_data['Data_fluctuationScale']['series'][-1]['y']
        return round(backup_scale, 2) if backup_scale else None
    except Exception as e:
        # print(11111)
        progress_bar.write(f"⚠️ 基金 {code} 规模解析失败: {str(e)}")
        return None


def _convert_scale(scale_str):
    """将规模字符串转换为数值（单位：亿）"""
    try:
        if '亿' in scale_str:
            return round(float(scale_str.replace('亿', '').strip()), 2)
        if '万' in scale_str:
            return round(float(scale_str.replace('万', '').strip()) / 10000, 2)
        return None
    except ValueError:
        return None


def _get_establishment_date(detail_df, progress_bar):
    """从详情数据中解析成立时间"""
    try:
        date_row = detail_df[detail_df['item'] == '成立时间']
        return date_row.iloc[0]['value'].strip() if not date_row.empty else None
    except Exception as e:
        progress_bar.write(f"⚠️ 成立时间解析失败: {str(e)}")
        return None


def save_to_excel(df, filename):
    """保存结果数据到Excel文件"""
    if df.empty:
        print("⚠️ 空数据集无需保存")
        return

    # 准备保存路径
    file_path = os.path.join(os.path.dirname(__file__), f"{filename}.xlsx")
    
    # 数据排序和格式化
    sorted_df = df.sort_values('基金规模（亿）', ascending=False)
    formatted_df = sorted_df[COLUMNS_ORDER].round({'基金规模（亿）': 2})
    
    # 保存文件
    formatted_df.to_excel(file_path, index=False)
    print(f"\n✅ 文件已保存至: {file_path}")
    print(f"📊 共处理有效数据 {len(formatted_df)} 条")


if __name__ == "__main__":
    try:
        print("🚀 开始获取沪深300基金数据...")
        selected_type = "被动指数型"
        # selected_type = "增强指数型"
        result_df = get_hs300_fund_data(selected_type)
        
        if not result_df.empty:
            save_to_excel(result_df, f"沪深300{selected_type}基金数据")
        else:
            print("❌ 未获取到有效数据，请检查网络或接口状态")
    except Exception as e:
        print(f"💥 程序运行异常: {str(e)}")