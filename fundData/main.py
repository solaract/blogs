import akshare as ak
import pandas as pd
import time
import os
from tqdm import tqdm

import fundScale

def get_hs300_fund_data(fund_type):
    """
    获取沪深300基金数据（含基金类型）
    :param fund_type:choice of {"全部", "被动指数型", "增强指数型"}
    """
    fund_df = ak.fund_info_index_em(symbol="全部", indicator=fund_type)
    
    # 筛选目标基金
    hs300_funds = fund_df[fund_df['基金名称'].str.contains('沪深300', na=False)]
    hs300_funds = hs300_funds[['基金代码', '基金名称', '跟踪方式']].copy()
    
    scale_list = []
    date_list = []
    pbar = tqdm(hs300_funds['基金代码'], 
                desc='获取基金规模',
                unit='支',
                ncols=100)

    for code in pbar:
        time.sleep(0.3)
        pbar.set_postfix_str(f"当前处理：{code}")
        try:
            detail_df = ak.fund_individual_basic_info_xq(symbol=code)

            # print(detail_df)
            
            try:
            # 修正1：使用准确字段名匹配
                scale_row = detail_df[detail_df['item'] == '最新规模']
                if not scale_row.empty:
                    scale_str = scale_row.iloc[0]['value']

                    # print(scale_str)
                    
                    # 修正2：处理不同单位
                    if '亿' in scale_str:
                        scale_value = round(float(scale_str.replace('亿', '').strip()),2)
                        # print(scale_value)
                    elif '万' in scale_str:
                        scale_value = round((float(scale_str.replace('万', '').strip()) / 10000),2)
                        # print(scale_value)
                    else:
                        scale_value = fundScale.fetch_fund_scale(code)
                        if(not scale_value):scale_value = None
                else:
                    scale_value = fundScale.fetch_fund_scale(code)
                    if(not scale_value):scale_value = None
            except Exception as e:
                pbar.write(f"⚠️ 基金 {code} 最新规模获取失败: {str(e)}")
                scale_value = fundScale.fetch_fund_scale(code)
                if(not scale_value):scale_value = None
            
            try:
                date = detail_df.iloc[3,1]
                if not date:
                    date = None
            except Exception as e:
                pbar.write(f"⚠️ 基金 {code} 成立时间获取失败: {str(e)}")
                date = None
                

            # print(f"{code}:{str(scale_value)}/{str(value2)}")
            
        except Exception as e:
            pbar.write(f"⚠️ 基金 {code} 获取失败: {str(e)}")
            scale_value = fundScale.fetch_fund_scale(code)
            if(not scale_value):scale_value = None
            date = None
            
        scale_list.append(scale_value)
        date_list.append(date)
    # print(scale_list)
    # print(len(scale_list))
    # print(scale_list2)
    # print(len(scale_list2))
    hs300_funds.insert(2,'基金规模（亿）',scale_list)
    hs300_funds.insert(3,'成立时间',date_list)
    # hs300_funds['成立时间'] = date_list
    return hs300_funds

def save_to_excel(df, filename):
    """保存数据到脚本所在目录"""
    filename = filename + ".xlsx"
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)
    
    # # 格式标准化
    # df = df.assign(
    #     基金规模_亿 = df['基金规模（亿）'].apply(lambda x: round(x, 2))
    # )
    
    df.sort_values('基金规模（亿）', ascending=False).to_excel(
        file_path, 
        index=False,
        columns=['基金代码', '基金名称', '基金规模（亿）','成立时间', '跟踪方式']
    )
    print(f"\n✅ 文件已保存至: {file_path}")

if __name__ == "__main__":
    try:
        print("🚀 开始获取沪深300基金数据...")
        # fund_type = "被动指数型"
        fund_type = "增强指数型"
        fund_data = get_hs300_fund_data(fund_type)
        fund_name = "沪深300" + fund_type + "基金数据"
        
        if not fund_data.empty:
            save_to_excel(fund_data,fund_name)
            print(f"📊 共获取有效数据 {len(fund_data)} 条")
        else:
            print("❌ 未获取到有效数据，请检查网络或接口状态")
    except Exception as e:
        print(f"💥 程序运行异常: {str(e)}")