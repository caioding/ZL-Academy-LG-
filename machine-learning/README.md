# 🤖 Machine Learning

## 📈 Algorítimo de Regressão Linear

É um dos métodos mais simples e populares para fazer previsões numéricas. A ideia básica aqui é encontrar uma linha que se ajuste aos dados de maneira que a diferença entre as previsões do modelo e os valores reais seja minimizada. Para fazer isso, usamos uma função de custo chamada erro quadrático médio (Mean Squared Error - MSE), que basicamente calcula a média dos quadrados das diferenças entre as previsões e os valores reais.

### 🔢 Regressão Linear com uma Variável Independente

Quando falamos de regressão linear com uma variável, a fórmula é bem simples:

y = w<sub>0</sub> + w<sub>1</sub> x<sub>1</sub>

em que:
- **y**: é o valor que estamos prevendo
- **w<sub>0</sub>**: é o viés, que ajusta a linha.
- **w<sub>1</sub>**: é o peso da característica x<sub>1</sub>
- **x<sub>1</sub>**: é o valor da característica

Agora, se quisermos ser ainda mais precisos, podemos adicionar uma variável para representar o erro aleatório, que é basicamente a diferença entre os valores previstos e os reais de *y*.

A regressão linear define uma reta que mostra a tendência geral dos dados. Com isso, ela consegue fazer previsões a partir de novos dados. **Ela funciona bem quando temos mais exemplos (instâncias) do que características (atributos)**.

Vamos ver agora como implementar um exemplo de regressão linear. O objetivo aqui é **usar o modelo de regressão para prever a emissão de CO2 com base em dados sobre veículos**. O primeiro passo é analisar as colunas do conjunto de dados para descobrir qual delas tem uma correlação direta com a variável que queremos prever, que é o **CO2**.