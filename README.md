# 🌡️ Conversor de Temperatura

Um projeto simples em Python com interface gráfica (Tkinter) que converte temperaturas entre **Celsius** e **Fahrenheit**. Desenvolvido para fins de estudo e prática.

## 📋 Sobre o projeto

A aplicação abre uma janela inicial com duas opções. Ao escolher uma delas, uma nova janela é aberta onde o usuário digita um valor e obtém o resultado da conversão na tela.

## ✨ Funcionalidades

- Conversão de Celsius para Fahrenheit
- Conversão de Fahrenheit para Celsius
- Interface gráfica simples e intuitiva
- Janelas separadas para cada tipo de conversão

## 🛠️ Tecnologias utilizadas

- [Python 3](https://www.python.org/)
- [Tkinter](https://docs.python.org/3/library/tkinter.html) (biblioteca padrão do Python para interfaces gráficas)


## 📖 Como usar

1. Ao iniciar, escolha entre **Conversão de Celcius** ou **Conversão de Fahrenheit**.
2. Na nova janela, digite o valor da temperatura no campo de texto.
3. Clique em **Converter**.
4. O resultado aparecerá logo abaixo do botão.

## 🧮 Fórmulas utilizadas

| Conversão | Fórmula |
|---|---|
| Celsius → Fahrenheit | `F = (C × 9/5) + 32` |
| Fahrenheit → Celsius | `C = (F − 32) × 5/9` |

## 📁 Estrutura do projeto

```
📦 nome-do-repositorio
 ┣ 📜 main.py
 ┗ 📜 README.md
```

## 🔮 Melhorias futuras

- [ ] Tratamento de erros para entradas inválidas (letras ou campo vazio)
- [ ] Limpar o resultado anterior ao fazer uma nova conversão
- [ ] Usar `Toplevel` em vez de múltiplas instâncias de `Tk`
- [ ] Arredondar o resultado para duas casas decimais
- [ ] Adicionar conversão para Kelvin
- [ ] Melhorar o visual da interface

---

💡 *Projeto criado com o objetivo de praticar Python e desenvolvimento de interfaces gráficas.*
