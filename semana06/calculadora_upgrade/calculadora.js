var valor = '';
var resultado = 0;

function botao(num){
    valor = document.calc.visor_eq.value += num; 
}

function deletar(){
    document.calc.visor_eq.value = document.calc.visor_eq.value.substring(0, document.calc.visor_eq.value.length-1);
    document.calc.visor_res.value = "Ans = "+resultado;
}

function resetar(){
    document.calc.visor_eq.value = '';
    document.calc.visor_res.value = 'Ans = 0';
}

function calcular() {
    if (testFirst()) {
        resultado = eval(valor);
        document.calc.visor_res.value = "Ans = " + resultado;
    }
}

function testFirst()
{
	var a = valor.substring(0,1);
	if (a == '+' || a == '-' || a == '.' || a == '0'  || a== '1' || a == '2' || a =='3' || a == '4' || a == '5' || a == '6' || a == '7' || a == '8' || a == '9'){
	    if(testLast()){
            return true;
        }else{
            return false;
        }
    }else{
	    document.calc.visor_eq.value = 'Error...';
	    document.calc.visor_res.value = 'Enter Number First!'
        return false;
    }
}

function testLast()
{
	var b = valor.substring(valor.length,valor.length-1);
	if (b == '0' || b == '1' || b == '2' || b =='3' || b == '4' || b == '5' || b == '6' || b == '7' || b == '8' || b == '9'){
	    return true;
    }else{
        document.calc.visor_eq.value = 'Error...';
	    document.calc.visor_res.value = 'Entry Incomplete!'
        return false;
    }
}