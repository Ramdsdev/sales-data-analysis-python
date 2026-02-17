from src.load_data import load_sales_data
from src.analysis import total_sales, sales_by_category, best_product
from src.visualization import plot_sales_by_category

# carregar dados
df = load_sales_data("data/vendas.csv")

print("\nTotal sales:", total_sales(df))

categoria = sales_by_category(df)
print("\nSales by category:")
print(categoria)

print("\nBest product:", best_product(df))

plot_sales_by_category(categoria)
