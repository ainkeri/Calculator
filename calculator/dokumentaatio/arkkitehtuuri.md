```mermaid
sequenceDiagram
    participant main
    participant Calculator
    participant CalculatorApp
    main ->> new CalculatorApp()
    CalculatorApp ->> new Calculator()
```