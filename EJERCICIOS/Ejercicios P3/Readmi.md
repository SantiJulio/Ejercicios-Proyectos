# Unit 3: Advanced OOP Paradigms, Interfaces, and Enterprise Architecture

This subfolder contains core enterprise-level software architectures, structural modeling, and testing patterns developed during **Unit 3 (2026)** for the Technical Degree in Web Programming at **UNSJ**.

The codebase demonstrates absolute mastery over structural entity dependencies, complex data parsing, runtime polymorphism, and defensive programming using custom exception states.

## 📂 Architecture & Enterprise Design Patterns

### 🏥 1. High-Dependency Association (Composition Pattern)
* **Medical Space Simulation (`Clínica` & `Consultorio`):** Implementation of a strict lifecycle composition where `Consultorio` instances belong exclusively to a single parent `Clínica` node.
* **Algorithmic Requirements:** Implements multi-attribute filtering sorted by floor levels and office indices through the overloading of the operational `__lt__` dunder method. Parsed through sequential file handling via delimited data sources.

### 🎟️ 2. Independent Lifecycle Association (Aggregation Pattern)
* **Event Platform Lifecycle (`EventosYA`):** Modeling structural aggregation matrices mapping decouple bounds between events and individual independent guests. Memory allocation isolates entity lifecycles to allow cross-event attendee mappings.

### 🏦 3. Relational Associative Entity Model (Class Association)
* **Banking Operations Backbone (`SJExpress SRL`):** Implementation of transaction management tables linking distinct operational domain entities (`SucursalBanco` and `Trabajador`) through an autonomous transaction layer (`CuentaSueldo`).
* **Industrial Validation Matrix:** Integrates test-driven methodologies using the **`unittest` library** to enforce operational verification over balance operations and custom linear tracking wrappers.

### 🚌 4. Dynamic Binding & Multi-Source Pipelines (Polymorphism & JSON Integration)
* **Runtime Polymorphism:** Architecture built on dynamic method overriding to compute tailored operation models natively (e.g., specific tourism cost functions and multiple payroll architectures).
* **Data Interchange Layers:** End-to-end processing mapping system schemas to nested hierarchical structures using **JSON file persistence** (`eventos.json` / `personal.json`).
* **Multiple Inheritance Engine:** Advanced class hierarchy integration resolving data structures from multiple base parents (`Docente`, `Investigador` $\rightarrow$ `Docente Investigador`) using strict MRO practices.

## 🛡️ Enterprise Quality Standards Applied
* **Formal Interfaces:** Abstract contract decoupling specifying operational permissions across system endpoints (e.g., separate roles for accounting and directory tracking).
* **Defensive Exception Matrix:** System error containment implementing boundary protections (`IndexError`, `TypeError`) thrown deep within linear collections and managed natively at the presentation level.
* **Maximum Reusability Compliance:** Generalized structural methods abstractions maximizing logic factoring directly across polymorphic base layers.
