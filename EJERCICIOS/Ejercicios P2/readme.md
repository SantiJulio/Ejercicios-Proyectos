# Unit 2: Advanced Object-Oriented Programming (OOP) Exercises

This subfolder contains the core practical assignments and modular architectures developed during **Unit 2 (2026)** for the Technical Degree in Web Programming at **UNSJ**. 

All exercises strictly follow academic guidelines: **no use of search loops with `for` flags, no forbidden `break` or `continue` commands**, and absolute decoupling of data inputs from the internal logic components.

## 📂 Academic Codebase Architecture

### 💳 Ejercicio 1 & 2: Billetera_Virtual & Controller System
* **Domain Model (`Billetera_Virtual`):** Python implementation tracking user attributes like balances, aliases, and cell numbers using strict modular principles. Features custom ledger handling where purchases balance verification throws negative codes for transactional failures.
* **Controller Framework (`Controlador`):** Decoupled business logic wrapper using programmatic validation to guarantee object integrity within storage lists, implementing custom iterator workflows to track negative-balance users without data leaks.
* **Sequence Diagram Tracking:** Fully compliant sequence tracking interface simulating multi-entity money transfer operations between clients, handlers, and the financial backend nodes.

### 📐 Ejercicio 3: Fractional Calculus Model (`Fraccion`)
* **Operator Overloading Engine:** Advanced modular class designed to allow native arithmetic operations between fractions and core integer types.
* Overloaded dunder methods implemented for mathematical interactions (`__add__`, `__sub__`, `__mul__`, `__truediv__`) as well as logical comparison matrices (`__gt__`, `__lt__`, `__eq__`, `__ne__`).

## ⚙️ Core Paradigms Applied
* **Decoupled Architecture:** Input streams (`input()`) are strictly managed outside domain models and logical handlers.
* **Strict Control Flows:** Algorithmic resolution relying purely on structured conditions and loop parameters without early jump statements.
* **Native Types Extensions:** Overriding operational operators to simulate enterprise-grade mathematical types natively in Python.
