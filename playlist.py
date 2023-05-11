# Minha Playlist

'''

Dependências:

pip install pytube
pip install tqdm

'''

import requests
import os
import pytube as pt
from tqdm import tqdm

# URL do arquivo de texto raw no GitHub
url = "url em breve"

# fazer uma solicitação GET para o arquivo raw do GitHub
response = requests.get(url)

# verificar se a solicitação foi bem sucedida
if response.status_code == 200:
    # ler o conteúdo do arquivo de texto e armazenar as URLs em uma lista
    urls = response.text.split("\n")

    # loop sobre as URLs e baixar as músicas
    for url in urls:
        print('Aguarde...')
        yt = pt.YouTube(https://raw.githubusercontent.com/Jetrom17/Youtube-py/main/list.txt)
        t = yt.streams.filter(only_audio=True)
        filename = t[0].download()

        with tqdm(total=100, desc=f"Download concluído: {os.path.splitext(filename)[0]}") as pbar:
            # renomear o arquivo para .mp3
            new_filename = os.path.splitext(filename)[0] + '.mp3'
            os.rename(filename, new_filename)

            # atualizar a barra de progresso
            pbar.update(100)

        print("Arquivo salvo como: ", new_filename)
else:
    print(f"Erro: status code {response.status_code}")
