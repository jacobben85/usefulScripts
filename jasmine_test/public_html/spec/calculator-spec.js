/* 
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */


/* global expect, Calculator */

var calculator = require("./../calculator");

describe("Add operation in calculator", function(){
    it ("Adds two numbers 10 and 5", function() {
        expect(calculator.calc.add(10, 5)).toEqual(15);
    });
});

describe("Add operation in calculator", function(){
    it ("Adds two numbers 15 and 5", function() {
        expect(calculator.calc.add(15, 5)).toEqual(20);
    });
});

describe("Sub operation in calculator", function(){
    it ("Subtract two numbers 10 and 5", function() {
        expect(calculator.calc.sub(10, 5)).toEqual(5);
    });
});

describe("Sub operation in calculator", function(){
    it ("Subtract two numbers 15 and 5", function() {
        expect(calculator.calc.sub(15, 5)).toEqual(10);
    });
});