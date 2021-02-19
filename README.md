### What is Spyder
Spyder is a little tool written in Python that analyses the source code of your project
and calculates a stability-index for each component. This could help you to improve your software architecture
or give you an indicator of which classes should be refactored, for example,
a class with a high instability rating should not contain a lot of logic since it depends
a lot on other classes and might break easier. The formula for calculating the stability was proposed by Robert C. Martin
in his book "Clean Architecture" where he mentions it as following:
S = |d_out| / |d_in| + |d_out| where S is the stability of a component, d_out the outgoing dependencies and d_in the incoming dependencies.

## TODO
Right now only Source Code written in Kotlin is supported. Adding new language support is trivial, it requires a regex rule for the language that specifies
the import syntax.
