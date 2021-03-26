import concurrent.futures  # modulo que fornece interface para a execução assincrona realizada na forma de thread ou processos
import time  # modulo que fornece suporte para trabalhar com funções relacionadas a tempo

import requests  # modulo que fornece suporte para solicitações HTTP

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

t1 = time.perf_counter()  # Inicio do contador de performace


# loop/função que recupera o conteudo da URL e escreve em um arquivo de mesmo nome. (download da imagem)
# for img_url in img_urls:
def download_image(img_url):
    img_bytes = requests.get(img_url).content  # recupera o conteudo da URL
    img_name = img_url.split(
        '/'
    )[3]  # separa a string considerando como separador a /, e armazena o nome da imagem (4 item apos o split)
    img_name = f'{img_name}.jpg'  # adiciona o tipo do arquivo baixado no caso é uma imagem jpg
    with open(img_name,
              'wb') as img_file:  # cria um arquivo e salva o conteudo da URL
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')


with concurrent.futures.ThreadPoolExecutor(
) as executor:  # cria um executor assincrono na forma da thread
    executor.map(
        download_image,
        img_urls)  # executor baixa a lista de imagens concorrentemente

t2 = time.perf_counter()  # fim do contador de performance

print(f'Finished in {t2-t1} seconds')
