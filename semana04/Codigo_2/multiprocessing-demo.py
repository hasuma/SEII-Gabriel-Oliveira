import concurrent.futures	# modulo que fornece interface para a execução assincrona realizada na forma de thread ou processos
import multiprocessing		# modulo que fornece suporte para trabalhar com multiprocessos
import time			# modulo que fornece suporte para trabalhar com funções relacionadas a tempo

start = time.perf_counter()	# Inicio do contador de performace

# função exemplo
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    # print('Done Sleeping...')
    return f'Done Sleeping...{seconds}'


with concurrent.futures.ProcessPoolExecutor() as executor:	# executor assincrono na forma de processo
    # f1 = executor.submit(do_something, 1)	# executor para executar a função exemplo
    # f2 = executor.submit(do_something, 1)	# executor para executar a função exemplo
    # print(f1.result())	# mostra o retorno do primeiro executor
    # print(f2.result())	# mostra o retorno do segundo executor
    secs = [5, 4, 3, 2, 1]
    # results = [executor.submit(do_something, sec) for sec in secs]	# cria uma lista de executores para executar a função exemplo para cada parametro contido na lista.
    # for f in concurrent.futures.as_completed(results):	# mostra os resultados na ordem de termino
    #    print(f.result())
    results = executor.map(do_something, secs)	# executor executa a função exemplo para cada parametro da lista

    # for result in results:	# mostra os resultados obtidos pelo map.
    #    print(result)

# processes = []	# cria lista vazia

# for _ in range(10):
#    p = multiprocessing.Process(target=do_something, args=[1.5])	# cria processo para executar a função exemplo para o parametro args.
#    p.start()	# inicializa o processo
#    processes.append(p)	# adiciona os processos na lista

# for process in processes:	# bloqueia ate cada um dos process em processes terminarem 
#    process.join()

# p1 = multiprocessing.Process(target=do_something)	# cria processo para executar função exemplo
# p2 = multiprocessing.Process(target=do_something)	# cria processo para executar função exemplo

# p1.start()	# inicializa o processo
# p2.start()	# inicializa o processo

# p1.join()	# bloqueia ate processo terminar
# p2.join()	# bloqueia ate processo terminar

# do_something()	# chama função exemplo
# do_something()	# chama função exemplo

finish = time.perf_counter()	# fim do contador de performance

print(f'Finished in {round(finish-start, 2)} second(s)')
