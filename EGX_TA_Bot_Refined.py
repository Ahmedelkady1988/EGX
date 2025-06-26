
from tradingview_ta import TA_Handler, Interval
import pandas as pd

# EGX symbols to analyze (without .CA suffix)
symbols = ['COMI', 'PHDC', 'AMOC', 'PRDC', 'IDRE', 'HRHO', 'FWRY', 'SWDY', 'QNBE', 'ABUK']

results = []

for symbol in symbols:
    try:
        handler = TA_Handler(
            symbol=symbol,
            exchange="EGX",
            screener="egypt",
            interval=Interval.INTERVAL_1_DAY
        )
        analysis = handler.get_analysis()
        results.append({
            "Symbol": symbol,
            "RSI": analysis.indicators.get("RSI"),
            "MACD": analysis.indicators.get("MACD.macd"),
            "MA Trend": analysis.moving_averages.get("RECOMMENDATION"),
            "Recommendation": analysis.summary.get("RECOMMENDATION")
        })
    except Exception as e:
        results.append({
            "Symbol": symbol,
            "Error": str(e)
        })

# Export to CSV
df = pd.DataFrame(results)
df.to_csv("egx_technical_analysis.csv", index=False)
print("✅ Exported to egx_technical_analysis.csv")
