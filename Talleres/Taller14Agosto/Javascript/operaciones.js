

exports.suma = function(numero1, numero2){
  return numero1 + numero2;
}

exports.multiplicacion = function(numero1, numero2){
  return numero1 * numero2;
}

exports.division = function(numero1, numero2){

  if(numero2 === 0){

    return 0;
  }
  return numero1 / numero2;
}


exports.resta = function(numero1, numero2){
  return numero1 - numero2;
}

exports.potenciacion =function(numero1, numero2){
  return Math.pow(numero1, numero2)
}

exports.logaritmacion = function(numero1, numero2){
  return Math.log(numero1, numero2)
}

exports.radicacion = function(numero1, numero2){
  return Math.sqrt(numero1, numero2)
}
