# Multi-View Machine Learning Predictor
## Objective
- To experiment with Taylor Series representation of Sine(x). 
- Applies naive ML model with cost minimization.
- Applies MVC design pattern for separation of concern.
- Applies sub patterns such as Observer, factory, and Strategy.

## Learning Outcome
- Leveraged OO concepts and implements them with design patterns.
- Dived into the foundational architecture of Web development (MVC).
- Explored ways to implement naive machine learning modelling technique.
- Practiced XP implementation from Agile. 

## Class UML

## Model Training

## Installation
- You would need to ensure all required modules are installed before running the codes.
    + $pip install -r requirements.txt
- After installation, run the following command:
    + $python Client.py

## Questions to be Addressed
1. The production codes shall be translated to C/C++ due to performance considerations and libraries limitation on the ecosystems of embedded devices. C/C++ allows fine-tuning over memory management, where reduced memory usage and improved speed can be achieved. On the contrary, Python is naturally slower due to its interpreted nature, and C#/Java run on JVM and CLR respectively, which add overhead compared to C/C++.

2. The MVC design pattern is exericsed in this project (along with observer and strategy). MVC can also be used in various GUI apps such as image editors and CAD software. Additionally, the MVC pattern is found in many embedded systems and IoT apps. The strength of MVC allows developers to create modular sub-systems concurrently by different teams due to separation of concerns, and thus accelerating production releases.

3. In debug builds, extra checks (validations, etc.), and the lack of optimized codes can slow the program down, which may unintentionally prevent race conditions from happening (if multi-threaded). This is especially a valid concern on an embedded device due to its computational limitations. Release builds, on the other hand, are faster due to many stages of revisoins and optimizations, so we are potentially exposing timing-related bugs that don't really appear in slower debug builds previously.

4. If you go through the codes, you may notice every component is programmed to an interface. The rationale behind this design is mainly utilizing the behaviours of _Dependency Inversoin Principle_, which conveys concrete implementations should always be programmed to an interface for decoupling. <br></br>

## Reference (Hyperlink-only)
- https://zevolving.com/2008/10/abap-objects-design-patterns-model-view-controller-mvc-part-1/
- https://github-pages.senecapolytechnic.ca/sed505/Assignments/Assignment4/TaylorSeries.pdf
- https://www.mathsisfun.com/algebra/taylor-series.html
- https://refactoring.guru/design-patterns