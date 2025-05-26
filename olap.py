import pandas as pd

# Sample data based on inserts.md (partial for demonstration)

# Categories
categories = pd.DataFrame({
    'id_categoria': [1, 2, 3, 4, 5, 6, 7, 8],
    'nome_categoria': ['Eletrônicos', 'Alimentos e Bebidas', 'Vestuário', 'Casa e Decoração', 'Esportes e Lazer', 'Beleza e Cuidados', 'Livros e Papelaria', 'Brinquedos'],
    'descricao': [
        'Produtos eletrônicos, tecnologia e informática',
        'Produtos alimentícios, bebidas e snacks',
        'Roupas, calçados e acessórios',
        'Móveis, decoração e utilidades domésticas',
        'Produtos esportivos e equipamentos de lazer',
        'Cosméticos, perfumaria e cuidados pessoais',
        'Livros, material escolar e escritório',
        'Brinquedos e jogos infantis'
    ]
})

# Products
products = pd.DataFrame({
    'id_produto': range(1, 41),
    'codigo_produto': [
        'ELET001', 'ELET002', 'ELET003', 'ELET004', 'ELET005',
        'ALIM001', 'ALIM002', 'ALIM003', 'ALIM004', 'ALIM005',
        'VEST001', 'VEST002', 'VEST003', 'VEST004', 'VEST005',
        'CASA001', 'CASA002', 'CASA003', 'CASA004', 'CASA005',
        'ESPO001', 'ESPO002', 'ESPO003', 'ESPO004', 'ESPO005',
        'BELZ001', 'BELZ002', 'BELZ003', 'BELZ004', 'BELZ005',
        'LIVR001', 'LIVR002', 'LIVR003', 'LIVR004', 'LIVR005',
        'BRIN001', 'BRIN002', 'BRIN003', 'BRIN004', 'BRIN005'
    ],
    'nome_produto': [
        'Smartphone Galaxy S22', 'Notebook Dell Inspiron 15', 'TV Smart 50" 4K', 'Fone Bluetooth', 'Mouse Gamer',
        'Café Premium 500g', 'Chocolate ao Leite 200g', 'Água Mineral 1,5L', 'Biscoito Integral', 'Suco Natural 1L',
        'Camisa Polo Masculina', 'Calça Jeans Feminina', 'Tênis Running', 'Vestido Casual', 'Mochila Escolar',
        'Jogo de Panelas 5 peças', 'Edredom Casal', 'Conjunto de Toalhas', 'Luminária de Mesa', 'Organizador Multiuso',
        'Bola de Futebol', 'Kit Halteres 10kg', 'Tapete Yoga', 'Bicicleta Aro 29', 'Corda de Pular',
        'Shampoo 400ml', 'Creme Hidratante 200ml', 'Perfume Masculino 100ml', 'Base Líquida', 'Kit Maquiagem',
        'Livro Best Seller', 'Caderno Universitário', 'Kit Canetas Coloridas', 'Agenda 2024', 'Calculadora Científica',
        'Lego Classic 500 peças', 'Boneca Fashion', 'Quebra-cabeça 1000 peças', 'Carrinho Hot Wheels', 'Jogo de Tabuleiro'
    ],
    'id_categoria': [
        1, 1, 1, 1, 1,
        2, 2, 2, 2, 2,
        3, 3, 3, 3, 3,
        4, 4, 4, 4, 4,
        5, 5, 5, 5, 5,
        6, 6, 6, 6, 6,
        7, 7, 7, 7, 7,
        8, 8, 8, 8, 8
    ],
    'marca': [
        'Samsung', 'Dell', 'LG', 'JBL', 'Logitech',
        'Melitta', 'Nestlé', 'Crystal', 'Vitarella', 'Del Valle',
        'Lacoste', 'Levi\'s', 'Nike', 'Renner', 'Samsonite',
        'Tramontina', 'Santista', 'Karsten', 'Philips', 'Ordene',
        'Adidas', 'Kikos', 'Acte Sports', 'Caloi', 'Speedo',
        'Pantene', 'Nivea', 'Boticário', 'MAC', 'Ruby Rose',
        'Intrínseca', 'Tilibra', 'BIC', 'Foroni', 'Casio',
        'Lego', 'Mattel', 'Grow', 'Hot Wheels', 'Grow'
    ],
    'preco_atual': [
        3499.00, 2899.00, 2199.00, 249.90, 199.90,
        24.90, 8.90, 2.90, 4.50, 7.90,
        189.90, 259.90, 399.90, 119.90, 149.90,
        299.90, 189.90, 99.90, 89.90, 39.90,
        129.90, 199.90, 79.90, 1499.00, 39.90,
        18.90, 24.90, 189.90, 249.90, 89.90,
        49.90, 24.90, 19.90, 34.90, 89.90,
        299.90, 149.90, 59.90, 12.90, 89.90
    ]
})

# Stores
stores = pd.DataFrame({
    'id_loja': range(1, 9),
    'codigo_loja': ['LJ001', 'LJ002', 'LJ003', 'LJ004', 'LJ005', 'LJ006', 'LJ007', 'LJ008'],
    'nome_loja': ['Loja Shopping Center', 'Loja Barra Shopping', 'Loja BH Shopping', 'Loja Recife Shopping', 'Loja Salvador Shopping', 'Loja Porto Alegre', 'Loja Brasília Shopping', 'Loja Curitiba Shopping'],
    'cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Recife', 'Salvador', 'Porto Alegre', 'Brasília', 'Curitiba'],
    'estado': ['SP', 'RJ', 'MG', 'PE', 'BA', 'RS', 'DF', 'PR']
})

# Sales
sales = pd.DataFrame({
    'id_venda': range(1, 16),
    'numero_venda': [
        'VD202401001', 'VD202401002', 'VD202401003', 'VD202401004', 'VD202401005',
        'VD202401006', 'VD202401007', 'VD202401008', 'VD202401009', 'VD202401010',
        'VD202402001', 'VD202402002', 'VD202402003', 'VD202402004', 'VD202402005'
    ],
    'id_cliente': [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
    'id_loja': [1,1,2,3,4,5,6,7,8,1,2,3,4,5,6],
    'id_funcionario': [2,3,6,10,14,18,2,3,4,5,6,7,8,9,10],
    'data_venda': pd.to_datetime([
        '2024-01-15 10:30:00', '2024-01-15 14:45:00', '2024-01-16 11:00:00', '2024-01-17 15:30:00', '2024-01-18 09:15:00',
        '2024-01-19 16:00:00', '2024-01-20 10:45:00', '2024-01-21 13:20:00', '2024-01-22 11:30:00', '2024-01-23 14:00:00',
        '2024-02-01 09:30:00', '2024-02-02 15:45:00', '2024-02-03 10:15:00', '2024-02-04 14:30:00', '2024-02-05 11:00:00'
    ]),
    'valor_total': [3698.90, 449.80, 2199.00, 279.80, 519.70, 89.90, 1499.00, 349.70, 169.80, 787.50, 4298.80, 199.90, 659.60, 89.90, 349.80],
    'desconto_total': [0.00, 44.98, 0.00, 27.98, 0.00, 0.00, 149.90, 0.00, 16.98, 0.00, 429.88, 0.00, 65.96, 0.00, 34.98],
    'forma_pagamento': ['Cartão Crédito', 'PIX', 'Cartão Débito', 'Dinheiro', 'Cartão Crédito', 'PIX', 'Cartão Crédito', 'Cartão Débito', 'PIX', 'Cartão Crédito', 'Cartão Crédito', 'PIX', 'Cartão Débito', 'Dinheiro', 'PIX'],
    'status_venda': ['Finalizada']*15
})

# Items of sales
items_sales = pd.DataFrame({
    'id_venda': [1,1,2,2,2,3,4,4,5,5,5,6,7,8,8,8,9,9,10,10,11,11,12,13,13,13,14,15,15],
    'id_produto': [1,4,6,8,13,3,16,21,11,12,26,35,19,22,17,33,9,37,2,5,1,25,34,13,14,15,38,18,23],
    'quantidade': [1,1,2,3,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    'preco_unitario': [3499.00,199.90,24.90,8.90,399.90,2199.00,299.90,18.90,189.90,259.90,49.90,89.90,1499.00,24.90,189.90,59.90,4.50,149.90,2899.00,199.90,3499.00,89.90,199.90,399.90,119.90,149.90,89.90,39.90,249.90],
    'desconto': [0.00,0.00,2.49,0.89,39.99,0.00,29.99,1.89,0.00,0.00,0.00,0.00,149.90,0.00,0.00,0.00,0.45,14.99,0.00,0.00,349.90,8.99,0.00,39.99,11.99,14.99,0.00,3.99,24.99],
    'valor_total': [3499.00,199.90,47.31,24.87,359.91,2199.00,269.91,17.01,189.90,259.90,49.90,89.90,1349.10,49.80,189.90,59.90,8.55,134.91,2899.00,199.90,3149.10,80.91,199.90,359.91,107.91,134.91,89.90,71.82,224.91]
})

# Merge data for OLAP analysis
sales_items_merged = items_sales.merge(sales, on='id_venda', suffixes=('_item', '_venda'))
sales_items_merged = sales_items_merged.merge(products[['id_produto', 'nome_produto', 'id_categoria']], on='id_produto')
sales_items_merged = sales_items_merged.merge(categories[['id_categoria', 'nome_categoria']], on='id_categoria')
sales_items_merged = sales_items_merged.merge(stores[['id_loja', 'nome_loja', 'cidade', 'estado']], left_on='id_loja', right_on='id_loja')

# Example OLAP queries

def sales_by_store():
    return sales_items_merged.groupby('nome_loja').agg(
        total_vendas=('valor_total_item', 'sum'),
        quantidade_vendida=('quantidade', 'sum')
    ).sort_values('total_vendas', ascending=False)

def sales_by_category():
    return sales_items_merged.groupby('nome_categoria').agg(
        total_vendas=('valor_total_item', 'sum'),
        quantidade_vendida=('quantidade', 'sum')
    ).sort_values('total_vendas', ascending=False)

def sales_by_product():
    return sales_items_merged.groupby('nome_produto').agg(
        total_vendas=('valor_total_item', 'sum'),
        quantidade_vendida=('quantidade', 'sum')
    ).sort_values('quantidade_vendida', ascending=False).head(10)

def sales_by_city():
    return sales_items_merged.groupby('cidade').agg(
        total_vendas=('valor_total_item', 'sum'),
        quantidade_vendida=('quantidade', 'sum')
    ).sort_values('total_vendas', ascending=False)

def sales_by_state():
    return sales_items_merged.groupby('estado').agg(
        total_vendas=('valor_total_item', 'sum'),
        quantidade_vendida=('quantidade', 'sum')
    ).sort_values('total_vendas', ascending=False)

import matplotlib.pyplot as plt

def plot_sales_by_store():
    df = sales_by_store().reset_index()
    plt.figure(figsize=(10,6))
    plt.bar(df['nome_loja'], df['total_vendas'], color='skyblue')
    plt.title('Total Sales by Store')
    plt.xlabel('Store')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def plot_sales_by_category():
    df = sales_by_category().reset_index()
    plt.figure(figsize=(10,6))
    plt.bar(df['nome_categoria'], df['total_vendas'], color='lightgreen')
    plt.title('Total Sales by Category')
    plt.xlabel('Category')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def plot_sales_by_product():
    df = sales_by_product().reset_index()
    plt.figure(figsize=(12,6))
    plt.bar(df['nome_produto'], df['quantidade_vendida'], color='salmon')
    plt.title('Top 10 Products by Quantity Sold')
    plt.xlabel('Product')
    plt.ylabel('Quantity Sold')
    plt.xticks(rotation=75, ha='right')
    plt.tight_layout()
    plt.show()

def plot_sales_by_city():
    df = sales_by_city().reset_index()
    plt.figure(figsize=(10,6))
    plt.bar(df['cidade'], df['total_vendas'], color='orange')
    plt.title('Total Sales by City')
    plt.xlabel('City')
    plt.ylabel('Total Sales')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def plot_sales_by_state():
    df = sales_by_state().reset_index()
    plt.figure(figsize=(8,6))
    plt.bar(df['estado'], df['total_vendas'], color='purple')
    plt.title('Total Sales by State')
    plt.xlabel('State')
    plt.ylabel('Total Sales')
    plt.tight_layout()
    plt.show()

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plot_3d_sales_scatter():
    df = sales_items_merged.copy()
    df['day_of_month'] = df['data_venda'].dt.day
    fig = plt.figure(figsize=(10,8))
    ax = fig.add_subplot(111, projection='3d')
    sc = ax.scatter(df['day_of_month'], df['quantidade'], df['valor_total_item'], c=df['valor_total_item'], cmap='viridis', s=50)
    ax.set_xlabel('Dia (Dia do mês da venda)')
    ax.set_ylabel('Quantidade (Número de unidades vendidas)')
    ax.set_zlabel('Valor Total (Valor total das vendas em R$)')
    plt.colorbar(sc, label='Valor Total')
    # Add labels to points
    for i, row in df.iterrows():
        ax.text(row['day_of_month'], row['quantidade'], row['valor_total_item'], str(row['id_venda']), size=8, zorder=1, color='k')
    plt.title('3D Scatter Plot of Sales')
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    print("Sales by Store:")
    print(sales_by_store())
    plot_sales_by_store()

    print("\nSales by Category:")
    print(sales_by_category())
    plot_sales_by_category()

    print("\nTop 10 Products by Quantity Sold:")
    print(sales_by_product())
    plot_sales_by_product()

    print("\nSales by City:")
    print(sales_by_city())
    plot_sales_by_city()

    print("\nSales by State:")
    print(sales_by_state())
    plot_sales_by_state()

    print("\n3D Scatter Plot of Sales:")
    plot_3d_sales_scatter()
