from tkinter import *
from tkinter import ttk
import re
import tkinter
import tkinter.font as font
from copy import deepcopy
from os import listdir
import os
import inspect


def listar_arquivos(caminho=None):
    lista_arqs = [arq for arq in listdir(caminho)]
    return lista_arqs


def novoarquivo():
    global arquivotemp, arqaberto, CheckVar, path , Pastadarq, Pastadarqcb
    nomedigitado = str(texto_digitado1.get()) + '.txt'
    arqconteudo.set(' ')
    arqaberto = nomedigitado
    arquivo = open(Pastadarq + "/ArquivoTemp.txt", "a")
    arquivo.close()
    arquivotemp = os.path.join(Pastadarqcb, "ArquivoTemp.txt")
    nomedigitado = os.path.join(Pastadarqcb, nomedigitado)
    os.rename(arquivotemp, nomedigitado)
    arqatual.set('Conteúdo do arquivo: ' + arqaberto)
    if __name__ == '__main__':
        nomedosarquivos = listar_arquivos(
            caminho=Pastadarq)
    for n1 in range(len(nomedosarquivos)):
        if n1 == 0:
            listatemp1 = deepcopy(nomedosarquivos[n1]) + '\n'
        else:
            listatemp1 = listatemp1 + deepcopy(nomedosarquivos[n1]) + '\n'
    fila.set(listatemp1)


def salvaarquivo():
    global CheckVar, contadort, path, Pastadarq, Pastadarqcb
    rs = 0
    nomearquivo = str(texto_digitado1.get()) + '.txt'
    if __name__ == '__main__':
        nomedosarquivos = listar_arquivos(
            caminho=Pastadarq)
    if len(nomedosarquivos) != 0:
        for n1 in range(len(nomedosarquivos)):
            if nomearquivo == nomedosarquivos[n1]:
                arquivo = open(
                    Pastadarqcb + nomearquivo,
                    "a")
                if CheckVar.get() == 0:
                    arqconteudo.set(' ')
                if CheckVar.get() == 1 and record.get() != '' and contadort < 5:  # Salva caso a opção Record tenha sido marcada
                    listconteudo[contadort] = record.get() + '\n'
                    contadort = contadort + 1
                    if contadort == 5:
                        listconteudo[contadort - 1] = listconteudo[contadort - 1] + '\n'
                        arquivo.writelines(listconteudo)
                        contadortext.set('[' + str(contadort) + '/5]')
                        rs = 1
                    else:
                        contadortext.set('[' + str(contadort) + '/5]')
                if CheckVar.get() == 2 and texto_digitado.get() != '':
                    conteudo = texto_digitado.get()
                    contadort = contadort + 1
                    if contadort == 5:
                        arquivo.writelines(conteudo + '\n' + '\n')
                        contadortext.set('[' + str(contadort) + '/5]')
                    else:
                        arquivo.writelines(conteudo + '\n')
                        contadortext.set('[' + str(contadort) + '/5]')
                arquivo.close()
                mostraarquivo()
                texto_digitado.delete(0, END)
                record.delete(0, END)
                if contadort == 1:
                    setatext1.config(fg='#d2ffff')
                    setarec1.config(fg='#d2ffff')
                if contadort == 2:
                    setatext2.config(fg='#d2ffff')
                    setarec2.config(fg='#d2ffff')
                if contadort == 3:
                    setatext3.config(fg='#d2ffff')
                    setarec3.config(fg='#d2ffff')
                if contadort == 4:
                    setatext4.config(fg='#d2ffff')
                    setarec4.config(fg='#d2ffff')
                if contadort == 5:
                    setatext5.config(fg='#d2ffff')
                    setarec5.config(fg='#d2ffff')
                    contatext.config(fg='#d2ffff')
                    contarec.config(fg='#d2ffff')
                if contadort == 6:
                    contatext.config(fg='Black')
                    contarec.config(fg='Black')
                    setatext2.config(fg='Black')
                    setarec2.config(fg='Black')
                    setatext3.config(fg='Black')
                    setarec3.config(fg='Black')
                    setatext4.config(fg='Black')
                    setarec4.config(fg='Black')
                    setatext5.config(fg='Black')
                    setarec5.config(fg='Black')
                    contadort = 1
                    contadortext.set('[' + str(contadort) + '/5]')
                if rs == 1:
                    contatext.config(fg='Black')
                    contarec.config(fg='Black')
                    setatext1.config(fg='Black')
                    setarec1.config(fg='Black')
                    setatext2.config(fg='Black')
                    setarec2.config(fg='Black')
                    setatext3.config(fg='Black')
                    setarec3.config(fg='Black')
                    setatext4.config(fg='Black')
                    setarec4.config(fg='Black')
                    setatext5.config(fg='Black')
                    setarec5.config(fg='Black')
                    contadort = 0
                    contadortext.set('[' + str(contadort) + '/5]')


def apagavalor():
    global Pastadarqcb, Pastadarq, path
    arqconteudo.set(' ')
    arqatual.set('Conteúdo do arquivo:')
    nomedigitado = str(texto_digitado1.get()) + '.txt'
    nomedigitado = os.path.join(Pastadarqcb, nomedigitado)
    os.remove(nomedigitado)
    if __name__ == '__main__':
        nomedosarquivos = listar_arquivos(caminho=Pastadarq)
    if len(nomedosarquivos) != 0:
        for n1 in range(len(nomedosarquivos)):
            if n1 == 0:
                listatemp1 = deepcopy(nomedosarquivos[n1]) + '\n'
            else:
                listatemp1 = listatemp1 + deepcopy(nomedosarquivos[n1]) + '\n'
        fila.set(listatemp1)
    else:
        fila.set('')


def resetacont():
    global  contadort
    contadort = 0
    contadortext.set('[' + str(contadort) + '/5]')
    contatext.config(fg='Black')
    contarec.config(fg='Black')
    setatext1.config(fg='Black')
    setarec1.config(fg='Black')
    setatext2.config(fg='Black')
    setarec2.config(fg='Black')
    setatext3.config(fg='Black')
    setarec3.config(fg='Black')
    setatext4.config(fg='Black')
    setarec4.config(fg='Black')
    setatext5.config(fg='Black')
    setarec5.config(fg='Black')


def mostraarquivo():
    global Pastadarqcb, Pastadarq, path
    nomearquivo = str(texto_digitado1.get()) + '.txt'
    if __name__ == '__main__':
        nomedosarquivos = listar_arquivos(caminho=Pastadarq)
    if len(nomedosarquivos) != 0:
        for n1 in range(len(nomedosarquivos)):
            if nomearquivo == nomedosarquivos[n1]:
                arquivo = open(
                    Pastadarqcb + nomearquivo,
                    "r")
                conteudo = arquivo.readlines()
                arqconteudo.set(''.join(conteudo))
                arqatual.set('Conteúdo do arquivo: ' + nomearquivo)
                arquivo.close()


def pesquisa():
    global Pastadarqcb, Pastadarq, path
    Op = MenuOP.get()
    conf = 0
    nomearquivo = str(texto_digitado1.get()) + '.txt'
    if __name__ == '__main__':
        nomedosarquivos = listar_arquivos(
            caminho=Pastadarq)
    if len(nomedosarquivos) != 0:
        for n1 in range(len(nomedosarquivos)):
            if nomearquivo == nomedosarquivos[n1]:
                arquivo = open(
                    Pastadarqcb + nomearquivo,
                    "r")
                conteudo = arquivo.readlines()
                palavrace = PalavraBusca.get() + '\n'
                palavrase = PalavraBusca.get()
                for n2 in range(len(conteudo)):
                    if Op == 'Texto':
                        if re.search(palavrace,conteudo[n2]) or re.search(palavrase,conteudo[n2]):
                            arqconteudo.set(str(n2+1) + "º Linha " + ": " + conteudo[n2])
                            conf = 1
                if Op == 'Record':
                    conteudo = blocar(conteudo)
                    for n4 in range(len(conteudo)):
                        if re.search(palavrace, conteudo[n4]) or re.search(palavrase, conteudo[n4]):
                            arqconteudo.set(str(n4 + 1) + "º Lote " + ": \n\n" + conteudo[n4])
                            conf = 1
                if conf == 0:
                    arqconteudo.set("Entrada não encontada no arquivo")
                arqatual.set('Conteúdo do arquivo: ' + nomearquivo)
                arquivo.close()


def blocar(lista):
    vld1 = 1
    vld2 = 0
    ranger = deepcopy(len(lista) - 1)
    for n10 in range(ranger):
        if vld1 < (len(lista) - 1):
            if lista[vld1] == '\n':
                lista.pop(vld1)
                vld1 = vld1 + 1
                vld2 = vld2 + 1
            else:
                lista[vld2] = lista[vld2] + lista[vld1]
                lista.pop(vld1)
    return lista


#busca e salva o diretorio atual
filename = inspect.getframeinfo(inspect.currentframe()).filename
path = os.path.dirname(os.path.abspath(filename))
Pastadarq = path + '/Arquivos do Simulador'
Pastadarq = re.sub(r'\\', '/', Pastadarq)
Pastadarqcb = Pastadarq + '/'
path = re.sub(r'\\', '/', path)


# criação da janela
sist=Tk()

# titulo da janela
sist.title('📁 Sistemas de Arquivos')

# cor do background
sist['bg'] = "light blue"

# tamanho da janela
sist.resizable(False, False)

#declaração da variavel dos arquivos
Menuvalor = tkinter.StringVar(sist)
Menuvalor.set("")
listconteudo = ['', '', '', '', '']
contadort = 0
contadortext = StringVar()
contadortext.set('[' + str(contadort) + '/5]')
arqaberto = ' '
arqatual = StringVar()
fila = StringVar()
arqconteudo = StringVar()
CheckVar = IntVar()
arqconteudo.set(' ')
arqatual.set('Conteúdo do arquivo:' + arqaberto)
if __name__ == '__main__':
    nomedosarquivos = listar_arquivos(caminho=Pastadarq)
if len(nomedosarquivos) != 0:
    for n1 in range(len(nomedosarquivos)):
        if n1 == 0:
             listatemp1 = deepcopy(nomedosarquivos[n1]) + '\n'
        else:
            listatemp1 = listatemp1 + deepcopy(nomedosarquivos[n1]) + '\n'
    fila.set(listatemp1)
else:
    fila.set('')


# janelas de tab

# Criação dos Tabs
tabControl = ttk.Notebook(sist)
tab1 = ttk.Frame(tabControl)
tab2 = ttk.Frame(tabControl)

# Cor e estilo dos tabs
style = ttk.Style()

style.theme_create('Meutema', settings={
    ".": {
        "configure": {
            "background": '#add8e6',  # cor dentro dos tabs
        }
    },
    "TNotebook": {
        "configure": {
            "background": '#add8e6',  # Cor da margem
            "tabmargins": [0, 0, 0, 0],  # margins: left, top, right, separator
        }
    },
    "TNotebook.Tab": {
        "configure": {
            "background": 'White',  # Cor do tab não selecionado
            "padding": [5, 1],
            # espaço do texto as extremidades do tab
        },
        "map": {
            "background": [("selected", '#d2ffff')],  # Cor do tab selecionado
            "expand": [("selected", [2, 0, 2, 2])]  # Margens do texto
        }
    }
})

style.theme_use('Meutema')

tabControl.add(tab1, text='Record',)

tabControl.add(tab2, text='Texto ')

#dentro do tab record

#ttk.Label(tab1, text="A").grid(column=0, row=0,) #separador

contarec = Label(tab1, textvariable = contadortext, bg = '#add8e6')

contarec.grid(column=0, row=1, sticky = 'S') #contador

ttk.Label(tab1, text = " Entrada: ").grid(column=0, row=1) #Entrada

setarec1 = Label(tab1, text = " ➜ ", bg = '#add8e6')

setarec1.grid(column=1, row=1, sticky = 'SW') # ➜ 1

setarec2 = Label(tab1, text = " ➜ ", bg = '#add8e6')

setarec2.grid(column=1, row=1, sticky = 'SW', padx = 20) # ➜ 2

setarec3 = Label(tab1, text = " ➜ ", bg = '#add8e6')

setarec3.grid(column=1, row=1, sticky = 'SW', padx = 40) # ➜ 3

setarec4 = Label(tab1, text = " ➜ ", bg = '#add8e6')

setarec4.grid(column=1, row=1, sticky = 'SW', padx = 60) # ➜ 4

setarec5 = Label(tab1, text = " ➜ ", bg = '#add8e6')

setarec5.grid(column=1, row=1, sticky = 'SW', padx = 80) # ➜ 5

record = Entry(tab1, width=23)

record.grid(column=1, row=1, pady = 25, padx = 5, sticky = 'W')

botaoprox = Button(tab1, text = " ➜ ",
                command=lambda: salvaarquivo(),
                bg = "#d2ffff",
                fg = "black",)

botaoprox.grid(column=1, row=1, padx = 7, sticky = 'E')

myFont = font.Font(size=1)

botaoR = Button(tab1, text = "",
                command=lambda: resetacont(),
                bg = "black",
                fg = "black",
                height = 1,
                width = 15,)

botaoR['font'] = myFont

botaoR.grid(column=0, row=1, sticky = 'S')

ttk.Label(tab1, text = " Entrada: ").grid(column=0, row=1) #Entrada


#dentro do tab Texto

#ttk.Label(tab2, text="A").grid(column=0, row=0,) #separador


contatext = Label(tab2, textvariable = contadortext, bg = '#add8e6')

contatext.grid(column=0, row=1, sticky = 'S') #contador

ttk.Label(tab2, text = " Entrada: ").grid(column=0, row=1) #Entrada

setatext1 = Label(tab2, text = " ➜ ", bg = '#add8e6')

setatext1.grid(column=1, row=1, sticky = 'SW') # ➜ 1

setatext2 = Label(tab2, text = " ➜ ", bg = '#add8e6')

setatext2.grid(column=1, row=1, sticky = 'SW', padx = 20) # ➜ 2

setatext3 = Label(tab2, text = " ➜ ", bg = '#add8e6')

setatext3.grid(column=1, row=1, sticky = 'SW', padx = 40) # ➜ 3

setatext4 = Label(tab2, text = " ➜ ", bg = '#add8e6')

setatext4.grid(column=1, row=1, sticky = 'SW', padx = 60) # ➜ 4

setatext5 = Label(tab2, text = " ➜ ", bg = '#add8e6')

setatext5.grid(column=1, row=1, sticky = 'SW', padx = 80) # ➜ 5

texto_digitado = Entry(tab2, width=23)

texto_digitado.grid(column=1, row=1, pady = 25, padx = 5, sticky = 'W')


botaoprox = Button(tab2, text = " ➜ ",
                command=lambda: salvaarquivo(),
                bg = "#d2ffff",
                fg = "black",)

botaoT = Button(tab2, text = "",
                command=lambda: resetacont(),
                bg = "black",
                fg = "black",
                height = 1,
                width = 15,)

botaoT['font'] = myFont

botaoT.grid(column=0, row=1, sticky = 'S')

botaoprox.grid(column=1, row=1, padx = 7, sticky = 'E')


# check box


C1 = Checkbutton(sist,
                 text = "Record",
                 variable = CheckVar,
                 onvalue = 1,
                 offvalue = 0,
                 bg = "Light Blue",
                 fg = "black")

C2 = Checkbutton(sist,
                 text = "Texto",
                 variable = CheckVar,
                 onvalue = 2,
                 offvalue = 0,
                 bg = "Light Blue",
                 fg = "black")


# label/caixa de testo


texto1 = Label(sist,
               text = ("Arquivos:"),
               bg = "Light Blue",
               fg = "black",
               bd = 2,
               relief = "groove",
               width = 45)

texto2 = Label(sist,
               textvariable = arqatual,
               bg = "Light Blue",
               fg = "black",
               bd = 2,
               relief = "groove",
               width = 45)

texto3 = Label(sist,
               text = "Nome do arquivo:",
               bg = "Light Blue",
               fg = "black")

texto4 = Label(sist,
               text = "Tipo de Salvamento:",
               bg = "Light Blue",
               fg = "black")

lv = Label(sist,
               text = "v",
               bg = "Light Blue",
               fg = "Light Blue")


QuadroBranco1 = Label(sist,
               textvariable = fila,
               bg = "White",
               fg = "Black",
               bd = 1,
               relief = "solid",
               width = 45,
               height = 25,
               anchor = NW,
               justify = LEFT)

QuadroBranco2 = Label(sist,
               textvariable = arqconteudo,
               bg = "White",
               fg = "Black",
               bd = 1,
               relief = "solid",
               width = 45,
               height = 25,
               anchor = NW,
               justify = LEFT)

#caixa de entrada de texto


texto_digitado1 = Entry(sist,
                       width=25)



# botões


botan1 = Button(sist, text = " 👁 ",
                command=lambda: mostraarquivo(),
                bg = "#e6e6e6",
                fg = "black",)

botan2 = Button(sist, text = " -  📁",
                command=lambda: apagavalor(),
                bg = "#ffb3b3",
                fg = "black",
                width=3,
                height=1,
                )

botan3 = Button(sist, text = "+ 📁",
                command=lambda: (novoarquivo()),
                bg = "#b3ffb3",
                fg = "black",
                width=3,
                height=1,
                )

# organização da parte da pesquisa


textopesquisa1 = Label(sist,
               text = "  Entrada da busca:",
               bg = "Light Blue",
               fg = "black")

textopesquisa2 = Label(sist,
               text = "   Tipo de pesquisa:",
               bg = "Light Blue",
               fg = "black")

PalavraBusca = Entry(sist, width=18)

MenuOP = ttk.Combobox(sist,
         values=[
         "Record",
         "Texto"],
         width=16)


bustao = Button(sist, text = " 🔍 ",
                command=lambda: (pesquisa()),
                bg = "#ffcc80",
                fg = "black",
                width=5,
                height=2,
                )

FontGG = font.Font(size=13)

bustao['font'] = FontGG

# organização da janela por Grid
C1.grid(row = 1, column=2, sticky = 'E') #checkbox Record
C2.grid(row = 1, column=3, sticky = 'W') #checkbox Texto
tabControl.grid(columnspan = 5, row = 2, column=0, sticky = 'W') #tabs
texto_digitado1.grid(row = 1, column=1, sticky = 'w') # Caixa de texto do nome do Arquivo para criação
botan1.grid(row = 1, column=2, padx = 31, sticky = 'W') # 👁
botan2.grid(row = 1, column=2, sticky = 'W') # -  📁
botan3.grid(row = 1, column=1, sticky = 'E') # +  📁
texto1.grid(columnspan = 2, row = 5, column=0) #arquivo
texto2.grid(columnspan = 2, row = 5, column=2, sticky = 'W') #Conteudo do Arquivo
texto3.grid(row = 1, column=0, sticky = 'E') # Nome do Arquivo
texto4.grid(row = 1, column=2, padx = 75) #Tipo de Salvamento
lv.grid(row = 3, column=2) #vazio na 3/3
QuadroBranco1.grid(columnspan = 2, row = 6, column=0) #quadro branco dos arquivos
QuadroBranco2.grid(columnspan = 2, row = 6, column=2, sticky = 'W') #quadro branco do conteudo do arquivo
textopesquisa1.grid(row = 2, column=2, sticky = 'W') #Entrada de busca
textopesquisa2.grid(row = 2, column=2, sticky = 'SW') #Tipo de Pesquisa
PalavraBusca.grid(row = 2, column=2, sticky = 'E', padx = 43) #Palvra da Busca
MenuOP.grid(row = 2, column=2, sticky = 'SE', padx = 41) #Menu da busca
bustao.grid(row = 2, column= 2, sticky = 'SE', columnspan = 2, padx = 25, pady = 2) # 🔍

#looping da janela
sist.mainloop()
