# fund_contrast_refactored.py
import os
import logging
import re
import time
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Tuple
from urllib.parse import urlparse

import akshare as ak
import pandas as pd
import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook, load_workbook
from openpyxl.styles import Alignment, PatternFill
from openpyxl.workbook.workbook import Workbook as OpenpyxlWorkbook
from openpyxl.worksheet.worksheet import Worksheet
from tqdm import tqdm

# ----------------- 配置常量 -----------------
class Config:
    BASE_DIR = Path(__file__).parent.absolute()
    TEMPLATE_FILE = BASE_DIR / "沪深300被动对比.xlsx"
    CODE_FILE = BASE_DIR / "沪深300被动代码.xlsx"
    
    COLORS = {
        "performance_highlight": "F8CBAD",
        "fee_highlight": "FFC000",
        "management_fee": "8EA9DB",
        "background": "D9D9D9",
        "excellent_fund": "A9D08E"
    }
    
    COLUMN_MAPPING = {
        "基金代码": 1,
        "基金名称": 2,
        "成立日期": 3,
        "今年来": 4,
        "近1周": 5,
        "近1月": 6,
        "近3月": 7,
        "近6月": 8,
        "近1年": 9,
        "近2年": 10,
        "近3年": 11,
        "近5年": 12,
        "年化跟踪误差": 13,
        "管理费率": 14,
        "托管费率": 15,
        "基金规模": 16
    }
    
    HEADERS = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

# ----------------- 工具函数 -----------------
def setup_logger() -> None:
    """配置日志记录器"""
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        handlers=[
            logging.FileHandler(Config.BASE_DIR / "fund_contrast.log"),
            logging.StreamHandler()
        ]
    )

def fetch_html(url: str, referer: str = None) -> str:
    """带重试机制的HTML请求函数"""
    headers = Config.HEADERS.copy()
    if referer:
        headers["Referer"] = referer
        headers["Host"] = urlparse(url).netloc

    for attempt in range(3):
        try:
            response = requests.get(url, headers=headers, timeout=15)
            response.raise_for_status()
            response.encoding = "utf-8"
            return response.text
        except requests.exceptions.RequestException as e:
            if attempt == 2:
                raise ConnectionError(f"请求失败: {url}") from e
            time.sleep(2 ** attempt)
    return ""

# ----------------- 数据处理类 -----------------
class FundDataProcessor:
    def __init__(self):
        self.output_data: List[Dict] = []
        self.workbook: Optional[OpenpyxlWorkbook] = None
        self.worksheet: Optional[Worksheet] = None
        self._init_workbook()
        
        # 初始化样式
        self.alignment = Alignment(horizontal="center", vertical="center")
        self.cell_formats = {
            "default": PatternFill(fill_type=None),
            "performance": PatternFill(fill_type="solid", fgColor=Config.COLORS["performance_highlight"]),
            "fee": PatternFill(fill_type="solid", fgColor=Config.COLORS["fee_highlight"]),
            "management": PatternFill(fill_type="solid", fgColor=Config.COLORS["management_fee"]),
            "background": PatternFill(fill_type="solid", fgColor=Config.COLORS["background"]),
            "excellent": PatternFill(fill_type="solid", fgColor=Config.COLORS["excellent_fund"])
        }

    def _init_workbook(self) -> None:
        """初始化Excel工作簿"""
        if not Config.TEMPLATE_FILE.exists():
            Workbook().save(Config.TEMPLATE_FILE)
        
        try:
            self.workbook = load_workbook(Config.TEMPLATE_FILE)
            self.worksheet = self.workbook.active
            self.worksheet["A1"] = datetime.now().strftime("%Y-%m-%d")
        except Exception as e:
            logging.error("Excel文件初始化失败: %s", str(e))
            raise

    def _load_fund_codes(self) -> List[str]:
        """加载基金代码"""
        if not Config.CODE_FILE.exists():
            raise FileNotFoundError(f"代码文件 {Config.CODE_FILE} 不存在")
        
        try:
            df = pd.read_excel(
                Config.CODE_FILE,
                header=None,
                dtype={0: str}
            )
            return df.iloc[:, 0].dropna().tolist()
        except Exception as e:
            logging.error("读取基金代码失败: %s", str(e))
            raise

    def _parse_performance_data(self, code: str) -> Dict:
        """解析业绩表现数据"""
        url = f"https://fundf10.eastmoney.com/FundArchivesDatas.aspx?type=jdzf&code={code}"
        try:
            html = fetch_html(url)
            content = re.search(r"content:\s*\"(.*?)\"\s*};", html, re.DOTALL).group(1)
            soup = BeautifulSoup(content, "html.parser")
            
            performance = {}
            for i, key in enumerate(Config.COLUMN_MAPPING.keys()):
                if i < 9:  # 跳过非业绩字段
                    continue
                if td := soup.select_one(f"div:nth-child({i+1}) > table > tbody > tr:nth-child(1) > td:nth-child(2)"):
                    performance[key] = td.text.strip()
            return performance
        except Exception as e:
            logging.warning("解析业绩数据失败: %s", str(e))
            return {}

    def _parse_fee_data(self, code: str) -> Dict:
        """解析费率数据"""
        url = f"https://fundf10.eastmoney.com/jbgk_{code}.html"
        try:
            soup = BeautifulSoup(fetch_html(url), "html.parser")
            return {
                "管理费率": self._parse_fee(soup, "管理费率"),
                "托管费率": self._parse_fee(soup, "托管费率")
            }
        except Exception as e:
            logging.warning("解析费率数据失败: %s", str(e))
            return {}

    def _parse_fee(self, soup: BeautifulSoup, fee_type: str) -> str:
        """解析具体费率"""
        if tag := soup.find("th", string=fee_type):
            return tag.find_next_sibling("td").text.split("%")[0] + "%"
        return ""

    def process_all_funds(self) -> None:
        """主处理流程"""
        fund_codes = self._load_fund_codes()
        index_df = ak.fund_info_index_em(symbol="沪深指数", indicator="被动指数型")

        with tqdm(
            fund_codes,
            desc="处理基金数据",
            unit="支",
            ncols=100,
            bar_format="{l_bar}{bar}| {n_fmt}/{total_fmt} [{elapsed}<{remaining}]"
        ) as pbar:
            for code in pbar:
                try:
                    fund_info = index_df[index_df["基金代码"] == code].iloc[0].to_dict()
                    performance = self._parse_performance_data(code)
                    fees = self._parse_fee_data(code)

                    self.output_data.append({
                        "基金代码": code,
                        "基金名称": fund_info.get("基金名称", ""),
                        "成立日期": fund_info.get("成立日期", ""),
                        **performance,
                        **fees,
                        "基金规模": fund_info.get("基金规模", "")
                    })
                    pbar.set_postfix_str(f"当前: {code}")
                except Exception as e:
                    logging.error("处理基金 %s 失败: %s", code, str(e))
                    continue
            print(self.output_data)

        self._write_to_excel()
        self.workbook.save(Config.TEMPLATE_FILE)
        logging.info("处理完成! 结果保存至: %s", Config.TEMPLATE_FILE)

    def _write_to_excel(self) -> None:
        """将数据写入Excel"""
        if not self.worksheet:
            raise ValueError("Excel工作表未初始化")

        averages = self._calculate_averages()
        for col_idx, fund_data in enumerate(self.output_data, start=3):
            col_letter = chr(64 + col_idx)
            self._write_basic_info(col_letter, fund_data)
            self._write_performance_data(col_letter, fund_data, averages)
            self._write_fee_data(col_letter, fund_data)

    def _calculate_averages(self) -> Dict[str, float]:
        """计算各指标平均值"""
        avg_keys = ["近1年", "近2年", "近3年", "近5年"]
        return {
            key: sum(
                float(d.get(key, "0%").rstrip("%"))  # 添加安全获取机制
                for d in self.output_data
            ) / len(self.output_data)  # 正确闭合sum括号并执行除法
            for key in avg_keys
        }  # 正确闭合字典推导式

    def _write_basic_info(self, col: str, data: Dict) -> None:
        """写入基础信息"""
        for field, row in Config.COLUMN_MAPPING.items():
            if row <= 3:
                cell = f"{col}{row}"
                self.worksheet[cell] = data.get(field, "")
                self.worksheet[cell].alignment = self.alignment

    def _write_performance_data(self, col: str, data: Dict, averages: Dict) -> None:
        """写入业绩数据并设置格式"""
        highlight_flags = {key: False for key in averages}
        
        for field, row in Config.COLUMN_MAPPING.items():
            if 4 <= row <= 12:
                cell = f"{col}{row}"
                self.worksheet[cell] = data.get(field, "")
                self._apply_performance_style(cell, field, data, averages, highlight_flags)

        if all(highlight_flags.values()):
            self.worksheet[f"{col}2"].fill = self.cell_formats["excellent"]

    def _apply_performance_style(self, cell: str, field: str, data: Dict, 
                               averages: Dict, flags: Dict) -> None:
        """应用业绩单元格样式"""
        try:
            value = float(data.get(field, "0%").rstrip("%"))
            avg = averages.get(field, 0)
            
            self.worksheet[cell].alignment = self.alignment
            self.worksheet[cell].fill = self.cell_formats["default"]
            
            if value > avg:
                self.worksheet[cell].fill = self.cell_formats["performance"]
                flags[field] = True
        except ValueError:
            pass

    def _write_fee_data(self, col: str, data: Dict) -> None:
        """写入费率数据"""
        for field in ["年化跟踪误差", "管理费率", "托管费率", "基金规模"]:
            row = Config.COLUMN_MAPPING[field]
            cell = f"{col}{row}"
            self.worksheet[cell] = data.get(field, "")
            self.worksheet[cell].alignment = self.alignment
            
            if field == "年化跟踪误差":
                self.worksheet[cell].fill = self.cell_formats["fee"]
            elif field in ["管理费率", "托管费率"]:
                self.worksheet[cell].fill = self.cell_formats["management"]
            else:
                self.worksheet[cell].fill = self.cell_formats["background"]

# ----------------- 主程序 -----------------
if __name__ == "__main__":
    setup_logger()
    try:
        processor = FundDataProcessor()
        processor.process_all_funds()
    except Exception as e:
        logging.error("程序运行失败: %s", str(e), exc_info=True)
        raise