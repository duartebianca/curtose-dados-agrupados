# Cálculo da Curtose

## 🎯 Objetivo do Projeto
Calcular a **curtose** para uma tabela de frequência com os dados agrupados. A fórmula utilizada nesse cálculo é:
curtose = ${q3-q1 \over 2*(p90 - p10)}$

Em que pi, qi representam percentis e quartis, respectivamente.

## 📌 Orientações básicas

* Esse código é baseado no cálculo de quartis e percentis para tabelas com dados agrupados. Você pode extrair um dataFrame diretamente de uma planilha ou pode, como eu fiz, criar o dataFrame durante o código. Há um exemplo para tornar as coisas mais visuais.
* A amplitude da classe deve ser alterada na chamada da função: 
  
  ```
  curtose = round(CalculaCurtose (df, qtd, 4), 2)
   print(curtose)
  ```
  No exemplo acima, o argumento da função calcula curtose corresponde a amplitude da classe que, nesse caso, é 4.
* Utilizamos a biblioteca [Pandas](https://www.acervolima.com.br/2021/01/como-instalar-o-python-pandas-no.html) e o módulo [Math](https://docs.python.org/pt-br/3/library/math.html).
* É importante que o seu dataFrame siga, na coluna de intervalos, a mesma sintaxe:
```
intervalo = ['[0, 2)', '[2, 4)', '[4, 6)', '[6, 8)', '[8, 10]']
```
* Caso não se saiba a quantidade total de elementos, ela pode ser descoberta assim:
```
qtd = 0
for i in range(tam):
  qtd += df['fi'][i]
```

## ✨ Exemplo de Uso 
*  Note que nosso código já vem com um exemplo de uso. Os dados a serem substituídos se encontram nesse trecho:
```
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
curtose = round(CalculaCurtose (df, qtd, h), x)
print(curtose)
```
* Note que h deve ser substituído pela amplitude da classe, e x pela quantidade de casas decimais que eu quero minha resposta.
qtd é o total de dados.
* Caso modifique o nome das colunas, é importante alterar no restante do código também.
