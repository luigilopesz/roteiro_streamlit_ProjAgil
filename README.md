## Roteiro Streamlit

### Preparação

Antes de começarmos, é importante preparar o ambiente:

1. Crie um ambiente virtual:
```bash
python -m venv nome_do_ambiente
```

2. Instale o Streamlit:
```bash
pip install streamlit
```

3. Para executar o Streamlit, utilize o seguinte comando:
```bash
streamlit run nome_do_arquivo.py
```

### 1. Introdução
Conheça o Streamlit, uma ferramenta poderosa para construção rápida de aplicativos web para visualização de dados e outras aplicações.

**Recursos para introdução:**
- [Introdução a Streamlit (Vídeo)](https://www.youtube.com/watch?v=0sxWFeFlsHs&ab_channel=HashtagPrograma%C3%A7%C3%A3o)

---

### Roteiro 1: Primeiros Passos com Streamlit

**Objetivo:** Entender a estrutura básica de um aplicativo Streamlit e interagir com elementos básicos.

**Tarefas:**
1. Clone o repositório e navegue até a pasta `roteiro_1`.
2. Examine o código inicial e rode-o para ver como funciona.
3. Adicione um input de texto. Após clicar no botão, o conteúdo do input de texto deve ser exibido no label ao invés do texto predefinido.

**[widgets do Streamlit](https://docs.streamlit.io/library/api-reference/widgets)**

---

### Roteiro 2: Widgets Interativos

**Objetivo:** Aprenda a interagir com diversos widgets do Streamlit.

**Tarefas:**
1. Clone/navegue até a pasta `roteiro_2`.
2. Examine o código e note que o botão já interage com o slider.
3. Implemente a lógica para que o valor do slider, checkbox, radio e selectbox sejam exibidos no label ao clicar no botão (Adicione os elementos consultando a documentação no link abaixo).
4. Adicione um componente "toggle" ao layout.

**[widgets do Streamlit](https://docs.streamlit.io/library/api-reference/widgets)**

---

### Roteiro 3: Organizando sua Interface

**Objetivo:** Organizar a interface usando componentes de layout.

**Tarefas:**
1. Clone/navegue até a pasta `roteiro_3`.
2. Implemente um sidebar com duas páginas.
3. Em uma das páginas, adicione tabs, um com componentes dentro de um expander e outro com componentes organizados em colunas dentro de um container.
4. Integre um componente de imagem à sua aplicação.

**[Layout do Streamlit](https://docs.streamlit.io/library/api-reference/layout)**

---

### Roteiro 4: Integração com APIs

**Objetivo:** Fazer requisições a uma API e exibir os resultados.

**Tarefas:**
1. Clone/navegue até a pasta `roteiro_4`.
2. Implemente uma caixa de texto para que o usuário insira o nome de um país.
3. Ao clicar no botão, faça uma requisição à API REST Countries para obter informações sobre esse país.
4. Exiba o nome comum e o nome oficial (dentro de `nativeName`) do país na aplicação.

**[Requests Quickstart](https://requests.readthedocs.io/en/latest/user/quickstart/)**

---

### Conclusão
Parabéns por concluir este roteiro! Agora você tem uma boa noção do Streamlit e suas capacidades. Próximos passos:

1. Explore componentes adicionais da comunidade para o Streamlit [aqui](https://streamlit.io/components?category=page-navigation).
2. Aprenda como fazer o deploy de seu aplicativo Streamlit com este [tutorial](https://www.youtube.com/watch?v=vw0I8i7QJRk&ab_channel=HashtagPrograma%C3%A7%C3%A3o).
3. Consulte a [documentação oficial](https://streamlit.io/) para mais detalhes e funcionalidades.

---

**Estrutura de pastas sugerida:**

```plaintext
.
├── roteiro_1
│   └── app_1.py
├── roteiro_2
│   └── app_2.py
├── roteiro_3
│   └── app_3.py
└── roteiro_4
    └── app_4.py
```
