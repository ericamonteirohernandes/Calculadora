import tkinter as tk
from support import config
from math import log10


# Passo 01: Variável global
exp = ""
resultado = ""

# Passo 02.A: Função Press (Projeto > Colocar em support/funcs.py)
def press(c:str):
    """Função para concatenar expressão e definir o input"""
    global exp

    exp = exp + str(c)


    if c == 'log':
        exp += '('
    input.set(exp)


# Passo 02.B: Função press_equal (Projeto > Colocar em support/funcs.py)
def press_equal() -> None:
    """Função para avaliar a expressão final quando = é pressionado"""
    try:
        global exp
        exp = exp.replace('x', '*').replace('–', '-')\
            .replace('\u00F7', '/').replace('\u00b2', '*2').replace('\u221a*', '**0.5')\
            .replace('log', 'log10')

        total = str(eval(exp))  # Retorna o resultado de eval
        input.set(total)




    except ZeroDivisionError:
        input.set("ERRO: DIV 0")

    except NameError:
        input.set('ERRO: NAME')

    except:
        input.set('ERRO')

    finally:
        exp = ""    # Re-instancia exp

# Passo 02.C: Função clear (Projeto > Colocar em support/funcs.py)
def clear():
    global exp
    exp = ""
    input.set("")


def log():
    global exp, resultado
    exp = 'math.log(' + exp + ')'

    resultado = eval(exp)

    exp = resultado


# Passo 02.D: Função clear_one (Projeto > Colocar em support/funcs.py)
def clear_one():
    global exp
    exp = exp[:-1]
    input.set(exp)




# Passo 03A: Criar um Tk root
root = tk.Tk()
root['bg'] = config.colors.get(0)
root.geometry(config.sizes)
root.title(config.title)
#root.iconbitmap(r'.\img\icon.ico')
root.resizable(width=False, height=False)


# Passo 03B: Elementos Gráficos
# 3B.1 -> Display
input = tk.StringVar()

display_frame = tk.Frame(root, width=200, height=config.height, highlightbackground=config.colors.get(0),
                         highlightcolor=config.colors.get(0), highlightthickness=10)
display_frame.pack(side=tk.TOP)

disply_field = tk.Entry(display_frame, font=('Calibri', 18, 'bold'), textvariable=input, width=50, bg="#eee", bd=0, justify=tk.RIGHT)
disply_field.grid(row=0, column=0)

disply_field.pack(ipady=10)


# 3B.2 -> Buttons
btns_frame = tk.Frame(root, width=config.width, height=config.height)

btns_frame.pack()


for idx, el in enumerate(config.keys):
    if idx // 4 in range(2, 6) and idx % 4 in range(0, 3):
        _bg_ = config.colors.get(3)
        _font_ = font=('Calibri', 14, 'bold')

        _fg_ = config.colors.get(1)
    else:
        _bg_ = config.colors.get(1) if el == '=' else config.colors.get(2)
        _font_ = font = ('Calibri', 14)
        _fg_ = config.colors.get(3)


    match el:
        case '=':
            f = lambda: press_equal()  # <--- Corrigir
        case 'CE':
            f = lambda: clear()
        case 'C':
            f = lambda: clear_one()
        case _:
            f = lambda x=el: press(x)
            # f = lambda: press(el)


    btn = tk.Button(btns_frame, text=el, bg=_bg_, fg=_fg_,
                    font=_font_,
                    width=6, height=2, cursor="hand2",
                    relief='flat',
                    command=f)


    btn.grid(row = idx // 4, column = idx % 4, columnspan=1, padx=0, pady=0)

# 3B.3 -> Label
# Frame
author_frame = tk.Frame(root, width=config.width, height=config.height)
author_frame.pack(side=tk.BOTTOM)

# Elemento / Label
author_label = tk.Label(author_frame, text='Tiago Reis • 2022')
author_label.grid(row=0, column=0)


# Passo 04: Mainloop
root.mainloop()

