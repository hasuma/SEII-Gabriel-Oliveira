import concurrent.futures	# modulo que fornece interface para a execução assincrona realizada na forma de thread ou processos
import time			# modulo que fornece suporte para trabalhar com funções relacionadas a tempo

from PIL import Image, ImageFilter	# modulo que fornce suporte a filtros de imagem

img_names = [
    'photo-1516117172878-fd2c41f4a759.jpg',
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1524429656589-6633a470097c.jpg',
    'photo-1530224264768-7ff8c1789d79.jpg',
    'photo-1564135624576-c5c88640f235.jpg',
    'photo-1541698444083-023c97d3f4b6.jpg',
    'photo-1522364723953-452d3431c267.jpg',
    'photo-1513938709626-033611b8cc03.jpg',
    'photo-1507143550189-fed454f93097.jpg',
    'photo-1493976040374-85c8e12f0c0e.jpg',
    'photo-1504198453319-5ce911bafcde.jpg',
    'photo-1530122037265-a5f1f91d3b99.jpg',
    'photo-1516972810927-80185027ca84.jpg',
    'photo-1550439062-609e1531270e.jpg', 'photo-1549692520-acc6669e2f0c.jpg'
]

t1 = time.perf_counter()	# Inicio do contador de performace

size = (1200, 1200)

# loop/função que aplica filtro gausiano no arquivo passado como parametro.
# for img_name in img_names:
def process_image(img_name):
    img = Image.open(img_name)	# abre o arquivo

    img = img.filter(ImageFilter.GaussianBlur(15))	# aplica o filtro

    img.thumbnail(size)				
    img.save(f'processed/{img_name}')		# salva imagem apos processamento
    print(f'{img_name} was processed...')


# with concurrent.futures.ThreadPoolExecutor() as executor:
with concurrent.futures.ProcessPoolExecutor() as executor:	# executor assincrono na forma de processo
    executor.map(process_image, img_names)			# executor que processa uma lista de imagens paralelamente

t2 = time.perf_counter()	# fim do contador de performance

print(f'Finished in {t2-t1} seconds')
