import matplotlib.pyplot as plt

def plot_sales_by_category(data):
    data.plot(kind="bar")

    plt.title("Sales by Category")
    plt.xlabel("Category")
    plt.ylabel("Total Value")

    plt.savefig("grafico_vendas.png")
    plt.show()
