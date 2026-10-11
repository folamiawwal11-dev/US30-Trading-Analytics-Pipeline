import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd
import seaborn as sns

# 1. Database Connection Configuration
db_config = {
    "host": "localhost",
    "user": "root",
    "password": "newpassword123",
    "database": "trading_analytics",
}

try:
    # 2. Connect to MySQL & Query the Equity Curve View
    conn = mysql.connector.connect(**db_config)
    query = "SELECT * FROM vw_running_equity_curve ORDER BY trade_id;"
    df = pd.read_sql(query, conn)
    conn.close()

    # 3. Configure Plot Theme
    sns.set_theme(style="darkgrid")
    plt.figure(figsize=(12, 6))

    # 4. Plot Cumulative Equity Trajectory
    plt.plot(
        df["trade_id"],
        df["running_net_roi"],
        marker="o",
        color="#00A86B",
        linewidth=2.5,
        label="Cumulative ROI (R)",
    )

    # 5. Add Reference Lines and Formatting
    plt.axhline(0, color="gray", linestyle="--", alpha=0.7)
    plt.title(
        "US30 Portfolio Performance - Cumulative Equity Trajectory",
        fontsize=14,
        fontweight="bold",
    )
    plt.xlabel("Trade Sequence Number (trade_id)", fontsize=11)
    plt.ylabel("Cumulative Net ROI (Units)", fontsize=11)

    # 6. Annotate Final Performance Point
    final_roi = df["running_net_roi"].iloc[-1]
    final_trade = df["trade_id"].iloc[-1]
    plt.annotate(
        f"Final ROI: +{final_roi}R",
        xy=(final_trade, final_roi),
        xytext=(final_trade - 4, final_roi + 2),
        arrowprops=dict(facecolor="#00A86B", shrink=0.05),
        fontweight="bold",
    )

    plt.tight_layout()

    # 7. Save Image Directly to Documents Folder
    output_path = r"C:\Users\folam\Documents\equity_curve.png"
    plt.savefig(output_path, dpi=300, bbox_inches="tight")
    print(f"\nSUCCESS! High-res chart saved to: {output_path}")

    # 8. Display Chart
    plt.show()

except Exception as e:
    print(f"Error connecting to database or plotting: {e}")