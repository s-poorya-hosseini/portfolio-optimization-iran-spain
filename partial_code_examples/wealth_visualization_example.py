import pandas as pd
import matplotlib.pyplot as plt

# Example wealth evolution data
wealth_df = pd.DataFrame({
    "Date": pd.date_range(start="2022-01-01", periods=5),
    "Markowitz": [1.0, 1.1, 1.25, 1.4, 1.55],
    "MIP": [1.0, 1.08, 1.18, 1.35, 1.48]
})

# Plot wealth evolution
plt.figure(figsize=(10, 6))

plt.plot(
    wealth_df["Date"],
    wealth_df["Markowitz"],
    label="Markowitz Portfolio",
    linewidth=2
)

plt.plot(
    wealth_df["Date"],
    wealth_df["MIP"],
    label="MIP Portfolio",
    linewidth=2
)

plt.title("Portfolio Wealth Evolution")
plt.xlabel("Date")
plt.ylabel("Portfolio Wealth")
plt.grid(True, alpha=0.3)
plt.legend()

plt.tight_layout()
plt.show()
