import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Ler dados do arquivo CSV
    df = pd.read_csv('epa-sea-level.csv')

    # Criar gráfico de dispersão
    x = df['Year']  # Eixo x: anos
    y = df['CSIRO Adjusted Sea Level']  # Eixo y: nível do mar ajustado pelo CSIRO
    
    fig, ax = plt.subplots()  # Criar uma nova figura e eixos
    plt.scatter(x, y)  # Adicionar os pontos de dispersão

    # Criar a primeira linha de melhor ajuste (para todos os anos)
    res = linregress(x, y)  # Calcular a regressão linear
    x_prediction = pd.Series([i for i in range(1880, 2051)])  # Criar série de anos para previsão
    y_prediction = res.slope * x_prediction + res.intercept  # Calcular a previsão do nível do mar
    plt.plot(x_prediction, y_prediction, 'r', label='Line of Best Fit (1880-2050)')  # Plotar a linha de melhor ajuste

    # Criar a segunda linha de melhor ajuste (para anos >= 2000)
    new_df = df.loc[df['Year'] >= 2000]  # Filtrar os dados para anos a partir de 2000
    new_x = new_df['Year']  # Eixo x: anos a partir de 2000
    new_y = new_df['CSIRO Adjusted Sea Level']  # Eixo y: nível do mar ajustado
    new_res = linregress(new_x, new_y)  # Calcular a regressão linear para os dados filtrados
    new_x_prediction = pd.Series([i for i in range(2000, 2051)])  # Criar série de anos para previsão
    new_y_prediction = new_res.slope * new_x_prediction + new_res.intercept  # Calcular a previsão do nível do mar
    plt.plot(new_x_prediction, new_y_prediction, 'green', label='Line of Best Fit (2000-2050)')  # Plotar a linha de melhor ajuste para anos a partir de 2000

    # Adicionar rótulos e título ao gráfico
    ax.set_xlabel('Year')  # Rótulo do eixo x
    ax.set_ylabel('Sea Level (inches)')  # Rótulo do eixo y
    ax.set_title('Rise in Sea Level')  # Título do gráfico
    
    # Adicionar legenda
    ax.legend()

    # Salvar o gráfico e retornar os dados para testes (NÃO MODIFICAR)
    plt.savefig('sea_level_plot.png')
    return plt.gca()  # Retornar os eixos atuais
