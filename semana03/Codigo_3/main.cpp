//**********************************************************
// Bibliotecas
#include <bits/stdc++.h>//All basic librarys
//**********************************************************
#define PI 3.14159265358979323846
#define rad2deg (180/PI)
#define deg2rad (PI/180)
	
using namespace std;
int DISCOS;
stack<int> pilha1;
stack<int> pilha2;
stack<int> pilha3;
 
//int contagem = 0;
 
void inicializaJogo(){
	for(int i = DISCOS; i > 0;){
		pilha1.push(i);
		i--;
	}  
}
 
void imprimeResultadoFinal(stack<int> pilha){
	if(!pilha.empty()){
		for(int i = 0; i < DISCOS; i++){
			cout << pilha.top() << endl;
			pilha.pop();
		}
		cout << endl; 
	}
}

void aeb(){
	if(pilha1.empty()){
		pilha1.push(pilha2.top());
		pilha2.pop();
		cout<<"B --> A"<<endl;
	}else if(pilha2.empty()){
		pilha2.push(pilha1.top());
		pilha1.pop();
		cout<<"A --> B"<<endl;
	}else if(pilha1.top() < pilha2.top()){  
		pilha2.push(pilha1.top());
		pilha1.pop();
		cout<<"A --> B"<<endl; 
	}else if(pilha2.top() < pilha1.top()){ 
		pilha1.push(pilha2.top());
		pilha2.pop();
		cout<<"B --> A"<<endl;
	}
}
 
void aec(){
	if(pilha1.empty()){       
		pilha1.push(pilha3.top());
		pilha3.pop();
		cout<<"C --> A"<<endl;  
	}else if(pilha3.empty()){     
		pilha3.push(pilha1.top());
		pilha1.pop();
		cout<<"A --> C"<<endl;   
	}else if(pilha1.top() < pilha3.top()){   
		pilha3.push(pilha1.top());
		pilha1.pop();
		cout<<"A --> C"<<endl;   
	}else if(pilha3.top() < pilha1.top()){
		pilha1.push(pilha3.top());
		pilha3.pop();
		cout<<"C --> A"<<endl; 
	}  
}
 
void bec(){
	if(pilha3.empty()){
		pilha3.push(pilha2.top());
		pilha2.pop();
		cout<<"B --> C"<<endl; 
	} else if(pilha2.empty()){
		pilha2.push(pilha3.top());
		pilha3.pop();
		cout<<"C --> B"<<endl; 
	}else if(pilha3.top() < pilha2.top()){
		pilha2.push(pilha3.top());
		pilha3.pop();
		cout<<"C --> B"<<endl; 
	}else if(pilha2.top() < pilha3.top()){      
		pilha3.push(pilha2.top());
		pilha2.pop();
		cout<<"B --> C"<<endl; 
	}   
}
 
int main(int argc, char *argv[]){
	if (argc != 2) {
		std::cout << "Quantidade de argumentos de entrada invalida\n";
		return 1;
	}
	stringstream ss;
	ss << argv[1];
	ss >> DISCOS;
		
	inicializaJogo();

	if(DISCOS % 2 == 0){ // Verifica se é par ou Ímpar
		while(pilha3.size() < DISCOS){
			aeb();
			if(pilha3.size() == DISCOS) break;
			aec();
			if(pilha3.size() == DISCOS) break;
			bec();
		}
	}else{
		while(pilha3.size() < DISCOS){
			aec();
			if(pilha3.size() == DISCOS) break;
			aeb();
			if(pilha3.size() == DISCOS) break;
			bec();
		}
	}
	cout << endl;
	cout <<"Fim da execução."<<endl;
	cout << "A pilha A contem " << pilha1.size() << " discos." <<endl;
	cout << "A pilha B contem " << pilha2.size() << " discos." <<endl;
	cout << "A pilha C contem " << pilha3.size() << " discos." <<endl;
	cout << endl;
	cout <<"Estado da ultima pilha:" << endl;
	imprimeResultadoFinal(pilha3);
	}
