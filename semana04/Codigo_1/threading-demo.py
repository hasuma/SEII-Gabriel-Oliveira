import concurrent.futures  # modulo que fornece interface para a execução assincrona realizada na forma de thread ou processos
import threading  # modulo que fornece suporte para trabalhar com threads
import time  # modulo que fornece suporte para trabalhar com funções relacionadas a tempo

start = time.perf_counter(
)  # função que retorna um contador de performanece (começo)


# Função exemplo
def do_something(seconds):
    print(f'Sleeping {seconds} second(s)...')
    time.sleep(seconds)
    # print('Done Sleeping...')
    return f'Done Sleeping...{seconds}'


with concurrent.futures.ThreadPoolExecutor(
) as executor:  # executor assincrono na forma de thread
    # f1 = executor.submit(do_something, 1)		# executor para executar a função exemplo
    # f2 = executor.submit(do_something, 1)		# executor para executar a função exemplo
    # print(f1.result())		# mostra o retorno do primeiro executor
    # print(f2.result())		# mostra o retorno do segundo executor
    # results = [executor.submit(do_something, 1) for _ in range(10)]	# cria uma lista de 10 executores para executar a função exemplo
    secs = [5, 4, 3, 2, 1]
    # results = [executor.submit(do_something, sec) for sec in secs] # cria uma lista de executores para executar a função exemplo para cada parametro contido na lista.
    # for f in concurrent.futures.as_completed(results):  # mostra os resultados na ordem de termino
    #    print(f.result())
    results = executor.map(
        do_something,
        secs)  # executor executa a função exemplo para cada parametro da lista

    for result in results:  # mostra os resultados obtidos pelo map na ordem de execução.
        print(result)

# threads = []		# cria lista vazia

# for _ in range(10):
#    t = threading.Thread(target=do_something, args=[1.5])	# cria thread para executar a função exemplo para o parametro args.
#    t.start()		 # inicializa a thread
#    threads.append(t)	 # adiciona as thread na lista

# for thread in threads:	# bloqueia ate cada uma das thread em threads terminarem
#    thread.join()

# t1 = threading.Thread(target=do_something) # cria thread para executar função exemplo
# t2 = threading.Thread(target=do_something) # cria thread para executar função exemplo

# t1.start()	# inicializa a thread
# t2.start()	# inicializa a thread

# t1.join()	# bloqueia ate thread terminar
# t2.join()	# bloqueia ate thread terminar

# do_something()	# chama função exemplo
# do_something()	# chama função exemplo

finish = time.perf_counter(
)  # função que retorna um contador de performanece (fim)
print(f'Finished in {round(finish-start, 2)} second(s)')
