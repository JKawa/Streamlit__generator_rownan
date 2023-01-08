import random

import streamlit as st


def run():
    st.set_page_config(page_title="Generator równań")

    st.sidebar.header("Jakie równania chcesz generować")
    st.sidebar.markdown("---")
    radio_format = {"fillcolor": 'red', 'color': 'blue', 'weight': 2, 'font_family': 'courier new',
                    'font-weight': 'bold', 'padding': '2px'}

    rodzaj_rownania = st.sidebar.radio(
        "Wybierz rodzaj równania",
        ('Równanie', 'Równanie z ułamkami', 'Układ równań', "Układ równań z ułamkami"))
    par = st.sidebar.number_input("Parametr", min_value=2, max_value=9, step=1)
    par_w = st.sidebar.number_input("Wyraz wolny", min_value=1, max_value=50, step=1)
    number = st.sidebar.number_input("Ilość równań", min_value=1, max_value=100, step=1)
    # parametr=st.sidebar.number_input("Parametr k", min_value=0, max_value=100,  step=1)
    z = st.container()
    z.title("Wyniki")

    def random_number(l: int, k: int) -> int:
        x = random.randint(l, k)
        return x

    def random_symbol() -> str:
        lista = ['+', '-']
        x = random.choice(lista)
        return x

    def random_symbol_p() -> str:
        lista = ['', '-']
        x = random.choice(lista)
        return x

    def random_from_list(lista: list) -> int:
        x = random.choice(lista)
        return x

    def wynik():
        z.empty()
        if rodzaj_rownania == 'Równanie':
            for a in range(number):
                with z:
                    st.latex(
                        rf'''{random_symbol_p()}{random_number(2, par)}x{random_symbol()}{random_number(1, par_w)}={random_symbol_p()}{random_number(2, par)}x{random_symbol()}{random_number(1, par_w)}''')
        elif rodzaj_rownania == 'Równanie z ułamkami':
            for a in range(number):
                with z:
                    if random_from_list([0, 1, 2, 3, 4, 5, 6]) == 0:
                        st.latex(
                            rf'''{random_symbol_p()}\frac{random_number(1, par)}{random_number(2, par)}\left(x\right){random_symbol()}\frac{random_number(1, par)}{random_number(2, par)}={random_symbol_p()}\frac{random_number(1, par)}{random_number(2, par)}\left(x\right){random_symbol()}\frac{random_number(1, par)}{random_number(2, par)}''')
                    elif random_from_list([0, 1, 2, 3, 4, 5, 6]) == 1:
                        st.latex(
                            rf'''{random_symbol_p()}{random_number(1, par)}x{random_symbol()}\frac{random_number(1, par)}{random_number(2, par)}={random_symbol_p()}\frac{random_number(1, par)}{random_number(2, par)}\left(x\right){random_symbol()}\frac{random_number(1, par)}{random_number(2, par)}''')
                    elif random_from_list([0, 1, 2, 3, 4, 5, 6]) == 2:
                        st.latex(
                            rf'''{random_symbol_p()}\frac{random_number(1, par)}{random_number(2, par)}\left(x\right){random_symbol()}{random_number(1, par_w)}={random_symbol_p()}\frac{random_number(1, par)}{random_number(2, par)}\left(x\right){random_symbol()}\frac{random_number(1, par)}{random_number(2, par)}''')
                    elif random_from_list([0, 1, 2, 3, 4, 5, 6]) == 3:
                        st.latex(
                            rf'''{random_symbol_p()}\frac{random_number(1, par)}{random_number(2, par)}\left(x\right){random_symbol()}\frac{random_number(1, par)}{random_number(2, par)}={random_symbol_p()}{random_number(1, par)}x{random_symbol()}\frac{random_number(1, par)}{random_number(2, par)}''')
                    elif random_from_list([0, 1, 2, 3, 4, 5, 6]) == 4:
                        st.latex(
                            rf'''{random_symbol_p()}\frac{random_number(1, par)}{random_number(2, par)}\left(x\right){random_symbol()}\frac{random_number(1, par)}{random_number(2, par)}={random_symbol_p()}\frac{random_number(1, par)}{random_number(2, par)}\left(x\right){random_symbol()}{random_number(1, par_w)}''')
                    elif random_from_list([0, 1, 2, 3, 4, 5, 6]) == 5:
                        st.latex(
                            rf'''{random_symbol_p()}\frac{random_number(1, par)}{random_number(2, par)}\left(x\right){random_symbol()}{random_number(1, par_w)}={random_symbol_p()}\frac{random_number(1, par)}{random_number(2, par)}\left(x\right){random_symbol()}{random_number(1, par_w)}''')
                    else:
                        st.latex(
                            rf'''{random_symbol_p()}\frac{random_number(1, par)}{random_number(2, par)}\left(x\right){random_symbol()}\frac{random_number(1, par)}{random_number(2, par)}={random_number(1, par)}x{random_symbol()}{random_number(1, par_w)}''')

        elif rodzaj_rownania == 'Układ równań':
            for a in range(number):
                with z:
                    st.latex(
                        r'''\left\{\begin{matrix}''' + rf'''{random_symbol_p()}{random_number(1, par)}x{random_symbol()}{random_number(1, par)}y{random_symbol()}{random_number(1, par_w)}=0 \\ {random_symbol_p()}{random_number(1, par)}x{random_symbol()}{random_number(1, par)}y{random_symbol()}{random_number(1, par_w)}=0 ''' + r'''\end{matrix}\right.''')

        elif rodzaj_rownania == "Układ równań z ułamkami":
            for a in range(number):
                with z:
                    if random_from_list([0, 1, 2, 3, 4, 5]) == 0:
                        st.latex(
                            r'''\left\{\begin{matrix}''' + rf'''{random_symbol_p()}\frac{random_number(1, par)}{random_number(2, par)}\left(x\right){random_symbol()}{random_number(1, par)}y{random_symbol()}{random_number(1, par_w)}=0 \\ {random_symbol_p()}\frac{random_number(1, par)}{random_number(2, par)}\left(x\right){random_symbol()}{random_number(1, par)}y{random_symbol()}{random_number(1, par_w)}=0 ''' + r'''\end{matrix}\right.''')
                    elif random_from_list([0, 1, 2, 3, 4, 5]) == 1:
                        st.latex(
                            r'''\left\{\begin{matrix}''' + rf'''{random_symbol_p()}{random_number(1, par)}x{random_symbol()}\frac{random_number(1, par)}{random_number(2, par)}\left(y\right){random_symbol()}{random_number(1, par_w)}=0 \\ {random_symbol_p()}{random_number(1, par)}x{random_symbol()}\frac{random_number(1, par)}{random_number(2, par)}\left(y\right){random_symbol()}{random_number(1, par_w)}=0 ''' + r'''\end{matrix}\right.''')
                    elif random_from_list([0, 1, 2, 3, 4, 5]) == 2:
                        st.latex(
                            r'''\left\{\begin{matrix}''' + rf'''{random_symbol_p()}\frac{random_number(1, par)}{random_number(2, par)}\left(x\right){random_symbol()}{random_number(1, par)}y{random_symbol()}{random_number(1, par_w)}=0 \\ {random_symbol_p()}{random_number(1, par)}x{random_symbol()}\frac{random_number(1, par)}{random_number(2, par)}\left(y\right){random_symbol()}{random_number(1, par_w)}=0 ''' + r'''\end{matrix}\right.''')
                    elif random_from_list([0, 1, 2, 3, 4, 5]) == 3:
                        st.latex(
                            r'''\left\{\begin{matrix}''' + rf'''{random_symbol_p()}\frac{random_number(1, par)}{random_number(2, par)}\left(x\right){random_symbol()}{random_number(1, par)}y{random_symbol()}\frac{random_number(1, par)}{random_number(2, par)}=0 \\ {random_symbol_p()}{random_number(1, par)}x{random_symbol()}\frac{random_number(1, par)}{random_number(2, par)}\left(y\right){random_symbol()}{random_number(1, par_w)}=0 ''' + r'''\end{matrix}\right.''')
                    elif random_from_list([0, 1, 2, 3, 4, 5]) == 4:
                        st.latex(
                            r'''\left\{\begin{matrix}''' + rf'''{random_symbol_p()}\frac{random_number(1, par)}{random_number(2, par)}\left(x\right){random_symbol()}{random_number(1, par)}y{random_symbol()}\frac{random_number(1, par)}{random_number(2, par)}=0 \\ {random_symbol_p()}{random_number(1, par)}x{random_symbol()}\frac{random_number(1, par)}{random_number(2, par)}\left(y\right){random_symbol()}\frac{random_number(1, par)}{random_number(2, par)}=0 ''' + r'''\end{matrix}\right.''')
                    else:
                        st.latex(
                            r'''\left\{\begin{matrix}''' + rf'''{random_symbol_p()}\frac{random_number(1, par)}{random_number(2, par)}\left(x\right){random_symbol()}{random_number(1, par)}y{random_symbol()}{random_number(1, par_w)}=0 \\ {random_symbol_p()}{random_number(1, par)}x{random_symbol()}\frac{random_number(1, par)}{random_number(2, par)}\left(y\right){random_symbol()}\frac{random_number(1, par)}{random_number(2, par)}=0 ''' + r'''\end{matrix}\right.''')

    m = st.markdown("""
    <style>
    div.stButton > button: {
        background-color: #762A83;
        color:#ffffff;
    }
    </style>""", unsafe_allow_html=True)

    st.sidebar.button(label="Pokaż wynik", on_click=wynik)


if __name__ == "__main__":
    run()
