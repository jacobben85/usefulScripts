# global exports

Calculator = ->

Calculator.prototype.add = (param1, param2) ->
  param1 + param2;
  
Calculator.prototype.sub = (param1, param2) ->
  param1 - param2;
  
Calculator.prototype.mulitply = (param1, param2) ->
  param1 * param2;

Calculator.prototype.divide = (param1, param2) ->
  param1 / param2;
  
calc = new Calculator;

exports.calc = calc;