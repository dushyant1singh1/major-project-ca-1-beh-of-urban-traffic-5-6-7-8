In this project user will enter the marks of different subjects and then we are predicting their stream in which he/she can start their carrer using fuzzy inference system.

## Fuzzy Logic

The term fuzzy refers to things which are not clear or are vague. In the real world many times we encounter a situation when we can’t determine whether the state is true or false, their fuzzy logic provides a very valuable flexibility for reasoning. In this way, we can consider the inaccuracies and uncertainties of any situation.

In boolean system truth value, 1.0 represents absolute truth value and 0.0 represents absolute false value. But in the fuzzy system, there is no logic for absolute truth and absolute false value. But in fuzzy logic, there is intermediate value too present which is partially true and partially false.


  ![fuzzy-logic_1](https://user-images.githubusercontent.com/42700950/68443217-4be4ed00-01f9-11ea-8d4f-dcdd6f629041.png)

## ARCHITECTURE

Its Architecture contains four parts :

##### 1) RULE BASE : 
It contains the set of rules and the IF-THEN conditions provided by the experts to govern the decision making system, on the basis of linguistic information. Recent developments in fuzzy theory offer several effective methods for the design and tuning of fuzzy controllers. Most of these developments reduce the number of fuzzy rules.

##### 2) FUZZIFICATION :
It is used to convert inputs i.e. crisp numbers into fuzzy sets. Crisp inputs are basically the exact inputs measured by sensors and passed into the control system for processing, such as temperature, pressure, rpm’s, etc.

##### 3) INFERENCE ENGINE :
It determines the matching degree of the current fuzzy input with respect to each rule and decides which rules are to be fired according to the input field. Next, the fired rules are combined to form the control actions.

##### 4) DEFUZZIFICATION :
It is used to convert the fuzzy sets obtained by inference engine into a crisp value. There are several defuzzification methods available and the best suited one is used with a specific expert system to reduce the error.
