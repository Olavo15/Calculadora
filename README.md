# Calculadora

Este repositório contém o código-fonte de uma aplicação de calculadora desenvolvida em Python usando a biblioteca Kivy. A calculadora é uma interface gráfica simples que permite aos usuários realizar operações matemáticas básicas, como adição, subtração, multiplicação e divisão.

Funcionalidades:

    A interface da calculadora é construída usando layouts de caixa (BoxLayout) e botões (Button) da biblioteca Kivy.

    A calculadora possui duas caixas de texto (TextInput), uma para exibir a expressão atual e outra para exibir o resultado da operação.
    
    Os botões numéricos de 0 a 9, os operadores matemáticos (+, -, *, /), o botão de ponto decimal (.) e o botão de limpar (C) são todos implementados como botões interativos.
    
    Os botões são estilizados com cores de fundo e texto para uma melhor experiência visual.
    
    A lógica da calculadora é implementada nos métodos on_button_press e on_solution, que lidam com a entrada do usuário e calculam o resultado da expressão, respectivamente.
    
    A aplicação é inicializada através da classe MainApp, que herda da classe App do Kivy e cria a interface gráfica da calculadora.
    Quando o botão "=" é pressionado, a calculadora avalia a expressão matemática inserida pelo usuário e exibe o resultado na caixa de texto apropriada.
