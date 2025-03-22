import akshare as ak
import pandas as pd
import time
import os
from tqdm import tqdm

import fundScale

def get_hs300_fund_data():
    """获取沪深300基金数据（含基金类型）"""
    fund_df = ak.fund_info_index_em(symbol="全部", indicator="增强指数型")
    
    # 筛选目标基金
    hs300_funds = fund_df[fund_df['基金名称'].str.contains('沪深300', na=False)]
    hs300_funds = hs300_funds[['基金代码', '基金名称', '跟踪方式']].copy()
    
    scale_list = []
    scale_list2 = []
    pbar = tqdm(hs300_funds['基金代码'], 
                desc='获取基金规模',
                unit='支',
                ncols=100)

    for code in pbar:
        try:
            time.sleep(0.3)
            pbar.set_postfix_str(f"当前处理：{code}")
            
            detail_df = ak.fund_individual_basic_info_xq(symbol=code)

            # print(detail_df)
            
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
                    scale_value = None
            else:
                scale_value = None
                
            scale_list.append(scale_value)

            value2 = fundScale.fetch_fund_scale(code)
            scale_list2.append(value2)
            
        except Exception as e:
            pbar.write(f"⚠️ 基金 {code} 获取失败: {str(e)}")
            scale_list.append(None)
    
    print(scale_list)
    print(len(scale_list))
    print(scale_list2)
    print(len(scale_list2))
    hs300_funds.insert(2,'基金规模（亿）',scale_list)
    hs300_funds.insert(2,'基金规模2（亿）',scale_list2)
    # hs300_funds['基金规模（亿）'] = scale_list
    return hs300_funds

def save_to_excel(df, filename="沪深300基金数据.xlsx"):
    """保存数据到脚本所在目录"""
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)
    
    # # 格式标准化
    # df = df.assign(
    #     基金规模_亿 = df['基金规模（亿）'].apply(lambda x: round(x, 2))
    # )
    
    df.sort_values('基金规模（亿）', ascending=False).to_excel(
        file_path, 
        index=False,
        columns=['基金代码', '基金名称', '基金规模（亿）','基金规模2（亿）', '跟踪方式']
    )
    print(f"\n✅ 文件已保存至: {file_path}")

if __name__ == "__main__":
    # try:
        print("🚀 开始获取沪深300基金数据...")
        fund_data = get_hs300_fund_data()
        
        if not fund_data.empty:
            save_to_excel(fund_data)
            print(f"📊 共获取有效数据 {len(fund_data)} 条")
        else:
            print("❌ 未获取到有效数据，请检查网络或接口状态")
    # except Exception as e:
    #     print(f"💥 程序运行异常: {str(e)}")