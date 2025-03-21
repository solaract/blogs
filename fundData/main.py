import akshare as ak
import pandas as pd
import time
from tqdm import tqdm  # 新增进度条库

def get_hs300_fund_data():
    """获取沪深300基金数据（含基金类型）"""
    # 获取全市场基金基础信息
    fund_df = ak.fund_info_index_em()
    
    # 筛选目标基金并保留类型字段
    hs300_funds = fund_df[fund_df['基金名称'].str.contains('沪深300', na=False)]
    hs300_funds = hs300_funds[['基金代码', '基金名称', '跟踪方式']]
    # print(hs300_funds)

    # print(ak.fund_individual_basic_info_xq(symbol='023065'))
    scale_df = 

    
    # # 初始化进度条
    # scale_list = []
    # pbar = tqdm(hs300_funds['基金代码'], 
    #             desc='获取基金规模',
    #             unit='支',
    #             ncols=100)  # 控制进度条宽度
    
    # for code in pbar:
    #     try:
    #         time.sleep(0.3)
    #         pbar.set_postfix_str(f"当前处理：{code}")  # 显示当前基金代码
            
    #         scale_df = ak.fund_individual_basic_info_xq(symbol=code)
    #         latest_scale = scale_df.iloc[4,1]
    #         # scale_value = float(str(latest_scale).replace('亿', ''))
    #         scale_list.append(latest_scale)
    #     except Exception as e:
    #         pbar.write(f"⚠️ 基金 {code} 获取失败: {str(e)}")  # 保留错误提示
    #         print(scale_df)
    #         scale_list.append(None)
    
    # 合并数据
    hs300_funds['基金规模'] = scale_list
    print(scale_list)
    return hs300_funds.dropna()
    # return hs300_funds.rename(columns={'基金简称': '基金名称'}).dropna()

def save_to_excel(df, filename="沪深300基金数据.xlsx"):
    """保存数据到Excel"""
    df = df[['基金代码', '基金名称', '跟踪方式', '基金规模']]
    df.to_excel(filename, index=False)
    print(f"\n✅ 文件已保存至: {filename}")

if __name__ == "__main__":
    try:
        # 带进度条的数据获取
        print("🚀 开始获取沪深300基金数据...")
        fund_data = get_hs300_fund_data()
        
        if not fund_data.empty:
            save_to_excel(fund_data)
            print(f"📊 共获取有效数据 {len(fund_data)} 条")
        else:
            print("❌ 未获取到有效数据，请检查网络或接口状态")
    except Exception as e:
        print(f"💥 程序运行异常: {str(e)}")