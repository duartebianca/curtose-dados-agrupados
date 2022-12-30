import pandas as pd
import math

#funcao para calcular quartil
def CalculaQuartil (qi, df, qtd, h):
  tam = len(df.index)
  if qi == 1:
    localiza_quartil = 0.25 * qtd
    multi = qtd
  if qi == 2:
    localiza_quartil = 0.5 * qtd
    multi = 2 * qtd
  if qi == 3:
    localiza_quartil = 0.75 * qtd
    multi = 3 * qtd
  valor = 0
  for i in range(tam):
    valor += df['fi'][i]
    if (localiza_quartil < valor and df['fi'][i-1] < localiza_quartil):
      break;
  lq = int(df.iloc[i, 0][1])
  if i > 0:
    F = df['Fi'][i-1]
  else:
    F = 0;
  fq = df['fi'][i]
  return lq + (((multi/4) -  F) * h) / fq

#funcao para calcular o percentil
def CalculaPercentil (pi, df, qtd, h):
  tam = len(df.index)
  multi = pi * qtd;
  pi = pi/100;
  localiza_percentil = pi * qtd;
  valor = 0
  for i in range(tam):
    valor += df['fi'][i]
    if (localiza_percentil < valor and (i-1) == 0):
      i = i-1
      break;
    elif (pi*100 != 10):
      if (localiza_percentil < valor and df['fi'][i-1] < localiza_percentil):
        break;
  lp = int(df.iloc[i, 0][1])
  if i > 0:
    F = df['Fi'][i-1]
  else:
    F = 0;
  fp = df['fi'][i]
  return lp + (((multi/100) -  F) * h) / fp

def CalculaCurtose(df, qtd, h):
  p90 = CalculaPercentil(90, df, qtd, h)
  p10 = CalculaPercentil(10, df, qtd, h)
  q3 = CalculaQuartil(3, df, qtd, h)
  q1 = CalculaQuartil(1, df, qtd, h)
  return (q3 - q1) / (2*(p90 - p10))

#dados de exemplo
qtd = 200 #total de elementos
intervalo = ['[0, 2)', '[2, 4)', '[4, 6)', '[6, 8)', '[8, 10]'] #para o código funcionar, use a mesma notação
frequencia = [30, 40, 20, 10, 100]
ponto_medio = [1, 3, 5, 7, 9]
frequencia_acumulada = [30, 70, 90, 100, 200]

df = pd.DataFrame({'intervalo': intervalo,
                   'fi': frequencia,
                   'xi': ponto_medio,
                   'Fi': frequencia_acumulada})

#calculo da curtose com duas casas decimais
curtose = round(CalculaCurtose (df, qtd, 2), 2)
print(curtose)
