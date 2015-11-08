calculator = require './../calculator';



describe "Add operation in calculator", ->
    a = Math.floor(Math.random()*10000);
    b = Math.floor(Math.random()*10000);
    it "Adds two numbers "+a+" and "+b+"", ->
        expect(calculator.calc.add(a, b)).toEqual(a + b);
        return
    return
    
describe "Sub operation in calculator", ->
    a = Math.floor(Math.random()*10000);
    b = Math.floor(Math.random()*10000);
    it "Sub two numbers "+a+" and "+b+"", ->
        expect(calculator.calc.sub(a, b)).toEqual(a - b);
        return
    return
    
describe "Multiply operation in calculator", ->
    a = Math.floor(Math.random()*10000);
    b = Math.floor(Math.random()*10000);
    it "Adds two numbers "+a+" and "+b+"", ->
        expect(calculator.calc.multiply(a, b)).toEqual(a * b);
        return
    return
    
describe "Divide operation in calculator", ->
    a = Math.floor(Math.random()*10000);
    b = Math.floor(Math.random()*10000);
    it "Adds two numbers "+a+" and "+b+"", ->
        expect(calculator.calc.divide(a, b)).toEqual(a / b);
        return
    return