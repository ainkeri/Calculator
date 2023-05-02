# Arkkitehtuurikuvaus

## Rakenne

Koodin pakkausrakenne:

```mermaid
flowchart LR
    application-->calc

```

Pakkaus application sisältää laskimen käyttöliittymän ja pakkaus calc laskimen sovelluslogiikan.


## Sovelluslogiikka

Laskin muodostuu kahdesta luokasta [Calculator](calculator/src/calc/calculator.py) ja [CalculatorApp](calculator/src/application/calculator_app.py):

```mermaid
sequenceDiagram
    participant User
    participant Calculator
    participant CalculatorApp
    User ->> CalculatorApp: open CalculatorApp
    CalculatorApp ->> Calculator: new Calculator()
    CalculatorApp ->> CalculatorApp: create button
    User ->> CalculatorApp: button click
    CalculatorApp ->> Calculator: does wanted method, (add, substract, multiply, divide, clear or get_result) 
    Calculator ->> CalculatorApp: updates display
  
```

