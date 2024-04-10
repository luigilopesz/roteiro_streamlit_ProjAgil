import streamlit as st

st.title("Roteiro 2: Widgets Interativos")

slider = st.slider("Escolha um valor", 0, 100)
checkbox = st.checkbox('caixinha :)')
radio = st.radio('escolha seu animal favorito:', ['cachorro', 'gato', 'peixe', 'coelho', 'hamster', 'calopsita'])
selectbox = st.selectbox('escolha um super poder:', ['força', 'invisibilidade', 'voo', 'ler mentes', 'manipulaçâo de metal'])

toggle = st.toggle('quer saber suas respostas?')

if toggle:
    st.write(f'valor: {slider}')
    if checkbox:
        resposta_caixinha = 'sim!!'
    else:
        resposta_caixinha = 'não :('
    st.write(f'clicou na caixinha?: {resposta_caixinha}')
    st.write(f'animal fav: {radio}')
    st.write(f'seu super poder: {selectbox}')
    
