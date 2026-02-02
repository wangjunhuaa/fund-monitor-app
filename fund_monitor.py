import streamlit as st
import pandas as pd
from datetime import datetime

# 页面配置
st.set_page_config(
    page_title="国内基金实时涨幅观测器（简化版）",
    page_icon="📈",
    layout="wide"
)

# 标题
st.title("📈 国内基金实时涨幅观测器（简化版）")
st.caption("支持多基金同时观测 | 手动录入数据 | 无复杂依赖冲突")

# 侧边栏：基金配置
with st.sidebar:
    st.header("基金配置")
    # 预设你关注的3只基金
    default_funds = "014089 永赢稳健增强债券C\n012922 易方达全球成长精选混合C\n025500 东方阿尔法科技智选混合发起C"
    fund_text = st.text_area(
        "输入基金信息（格式：代码 名称，一行一个）",
        value=default_funds,
        height=150
    )
    # 手动录入净值和涨幅（避免akshare依赖冲突）
    st.subheader("手动更新数据")
    latest_net_value = st.text_input("最新净值（示例：1.2345）", placeholder="输入对应基金最新净值")
    daily_change = st.text_input("当日涨幅（示例：+0.56% 或 -0.23%）", placeholder="输入对应基金当日涨幅")

# 解析基金信息
funds = []
for line in fund_text.split("\n"):
    if line.strip():
        parts = line.strip().split(" ", 1)
        if len(parts) == 2:
            code, name = parts
            funds.append({
                "基金代码": code,
                "基金名称": name,
                "最新净值": latest_net_value if latest_net_value else "待更新",
                "当日涨幅": daily_change if daily_change else "待更新",
                "更新时间": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

# 展示基金数据
if funds:
    st.subheader("📊 多基金实时表现对比")
    df_funds = pd.DataFrame(funds)
    st.dataframe(df_funds, use_container_width=True)
else:
    st.warning("请在侧边栏输入正确格式的基金信息")

# 补充说明
st.caption("✨ 简化版说明：1. 无复杂依赖，仅需 streamlit 和 pandas；2. 净值和涨幅需手动从基金平台查询录入；3. 避免 pip 依赖冲突")