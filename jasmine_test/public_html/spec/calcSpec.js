var calculator;

calculator = require('./../calculator');

describe("Add operation in calculator", function() {
  var a, b;
  a = Math.floor(Math.random() * 10000);
  b = Math.floor(Math.random() * 10000);
  it("Adds two numbers " + a + " and " + b + "", function() {
    expect(calculator.calc.add(a, b)).toEqual(a + b);
  });
});

describe("Sub operation in calculator", function() {
  var a, b;
  a = Math.floor(Math.random() * 10000);
  b = Math.floor(Math.random() * 10000);
  it("Sub two numbers " + a + " and " + b + "", function() {
    expect(calculator.calc.sub(a, b)).toEqual(a - b);
  });
});

describe("Multiply operation in calculator", function() {
  var a, b;
  a = Math.floor(Math.random() * 10000);
  b = Math.floor(Math.random() * 10000);
  it("Adds two numbers " + a + " and " + b + "", function() {
    expect(calculator.calc.multiply(a, b)).toEqual(a * b);
  });
});

describe("Divide operation in calculator", function() {
  var a, b;
  a = Math.floor(Math.random() * 10000);
  b = Math.floor(Math.random() * 10000);
  it("Adds two numbers " + a + " and " + b + "", function() {
    expect(calculator.calc.divide(a, b)).toEqual(a / b);
  });
});
