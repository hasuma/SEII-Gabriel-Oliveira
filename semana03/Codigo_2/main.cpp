//**********************************************************
// Bibliotecas
#include <bits/stdc++.h>//All basic librarys
//**********************************************************
#define PI 3.14159265358979323846
#define rad2deg (180/PI)
#define deg2rad (PI/180)
	
using namespace std;

int main(int argc, char *argv[]) {
	if (argc != 3) {
		std::cout << "Quantidade de argumentos de entrada invalida\n";
		return 1;
	}
	
	ifstream in{argv[1]}; 	// Primeiro argumento para leitura
	remove(argv[2]); 		// Deleta se existir o segundo argumento
	ofstream out{argv[2]};	// Cria Segundo argumento para edição (operações de entrada/saida)

	if (!out) {
		std::cerr << "Não foi possivel criar o arquivo de saida" << argv[2] << '\n';
		return 1;
	}

	static constexpr std::size_t buffsize{1024}; // tamanho do buffer (calculado em tempo de compilação)
	char buffer[buffsize]; // Buffer para leitura/escrita de 1024 bytes (1 char = 1 byte)

	while (in.read(buffer, buffsize)) {	// Leitura do arg1
		out.write(buffer, buffsize);	// Escrita no arg2
	}
	out.write(buffer, in.gcount());	// Escrita dos ultimos caracteres do arg1 no arg2
}
