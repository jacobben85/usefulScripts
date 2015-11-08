var Calculator, calc;

Calculator = function() {};

Calculator.prototype.add = function(param1, param2) {
  return param1 + param2;
};

Calculator.prototype.sub = function(param1, param2) {
  return param1 - param2;
};

Calculator.prototype.multiply = function(param1, param2) {
  return param1 * param2;
};

Calculator.prototype.divide = function(param1, param2) {
  return param1 / param2;
};

calc = new Calculator;

exports.calc = calc;
