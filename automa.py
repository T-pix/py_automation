import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")

list_arquivo = os.listdir(caminho)

locais = {
    'imagens': ['.png', '.jpg', '.jpeg'],
    'planilhas': ['.xlsx', '.csv'],
    'pdf-s': ['.pdf'],
    'exec': ['.exe']
}

for arquivo in list_arquivo:
    nome, extencao = os.path.splitext(f'{caminho}/{arquivo}')
    for pasta in locais:
        if extencao in locais[pasta]:
            if not os.path.exists(f'{caminho}/{pasta}'):
                os.mkdir(f'{caminho}/{pasta}')
            os.rename(f'{caminho}/{arquivo}', f'{caminho}/{pasta}/{arquivo}')
            
