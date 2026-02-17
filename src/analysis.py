def total_sales(df):
    return df["valor"].sum()

def sales_by_category(df):
    return df.groupby("categoria")["valor"].sum()

def best_product(df):
    return df.groupby("produto")["valor"].sum().idxmax()
