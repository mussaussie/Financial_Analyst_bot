import pandas as pd
df = pd.read_excel(r"C:\Users\mussa\Downloads\financial_data_extracted.xlsx")
print(df.head())
df['Revenue Growth (%)'] = df.groupby(['Company'])['Total Revenue'].pct_change() * 100 
df['Net Income Growth (%)'] = df.groupby(['Company'])['Net Income'].pct_change() * 100
print(df.head())
# Calculate the average revenue growth by company
average_revenue_growth = df.groupby('Company')['Revenue Growth (%)'].mean()
# Calculate the total net income by company
total_net_income = df.groupby('Company')['Net Income'].sum()
# Display the results
print(average_revenue_growth)
print(total_net_income)
import matplotlib.pyplot as plt
# Plot Revenue Growth (%) for each company
plt.figure(figsize=(10, 6))
for company in df['Company'].unique():
    company_data = df[df['Company'] == company]
    plt.plot(company_data['Year'], company_data['Revenue Growth (%)'], label=company)

plt.title('Revenue Growth (%) by Company')
plt.xlabel('Year')
plt.ylabel('Revenue Growth (%)')
plt.legend(title='Company')
plt.grid(True)
plt.show()
# Plot Net Income for each company
plt.figure(figsize=(10, 6))
for company in df['Company'].unique():
    company_data = df[df['Company'] == company]
    plt.plot(company_data['Year'], company_data['Net Income'], label=company)

plt.title('Net Income by Company')
plt.xlabel('Year')
plt.ylabel('Net Income')
plt.legend(title='Company')
plt.grid(True)
plt.show()
## We’ll analyze Apple’s Revenue Decline in 2023 and Tesla’s Low Net Income:
# Apple's Revenue Decline (2023) We'll check Apple's revenue and analyze its slight decline in 2023
# Filter data for Apple
apple_data = df[df['Company'] == 'Apple']

# Get Apple's Revenue Growth and Net Income in 2023
apple_2023_revenue = apple_data[apple_data['Year'] == 2023]['Revenue Growth (%)'].values[0]
apple_2023_net_income = apple_data[apple_data['Year'] == 2023]['Net Income'].values[0]

print(f"Apple's Revenue Growth in 2023: {apple_2023_revenue}%")
print(f"Apple's Net Income in 2023 (million): {apple_2023_net_income}")

def get_total_revenue(company, year):
    data = df[(df['Company'] == company) & (df['Year'] == year)]
    if not data.empty:
        # Convert revenue from millions to billions
        revenue_in_billions = data['Total Revenue'].values[0] / 1000
        return f"The total revenue for {company} in {year} is {revenue_in_billions:.2f} billion."
    return "Data not available."

