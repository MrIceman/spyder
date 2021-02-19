### What is Spyder
Spyder is a little tool written in Python that analyses the source code of your project
and calculates a stability-index for each component. This could help you to improve your software architecture
or give you an indicator of which classes should be refactored, for example,
a class with a high instability rating should not contain a lot of logic since it depends
a lot on other classes and might break easier. The formula for calculating the stability was proposed by Robert C. Martin
in his book "Clean Architecture" where he describes it as follows:<br/>
<code>S = |d_out| / |d_in| + |d_out|</code> <br/>where <b>S</b> is the stability of a component, <b>d_out</b> the outgoing dependencies 
and <b>d_in</b> the incoming dependencies. Basically, a value <b>S</b> is assigned to each of your components (classes).<br/><br/>
Let's have an example. We imply we have two components, <b>A</b> and <b>B</b>, with the following dependency flow<br/><br/>
<i><b>A</b> ---> <b>B</b></i> <br/><br/>
<b>A</b> has 1 outgoing dependency (to B) and 0 incoming dependencies. B has 1 incoming dependency (from A) and 0 outgoing dependencies.
The stability index for <b>A</b> would be 1, means it is unstable and will be effected by changes within its dependencies.
Component <b>B</b> in this case has a stability index of 0, which means it is stable and resistant towards changes within the system.<br/>
So naturally, if Component <b>B</b> breaks then you'll have to refactor <b>A</b>.<br/>What does this tell us? <br/>
Well, we could conclude following:
<ol>
<li>
<b>A</b> breaks if <b>B</b> changes</li>
<li>
<b>B</b> is more stable than <b>A</b></li>
<li>Placing logic in <b>A</b> might be bad due to its instability. It's probably worth to have a second look at that component and maybe refactor a bit</li>
</ol>
Additionally, the dependencies of your component should have a lower instability rating then the component itself. Spyder analyses this case and tells you which components
in your project depend on components that are less stable. Consider adding an abstraction in this case to have more robustness
towards changes within your system.

##TODO
<ul>
<li>
Right now only Source Code written in Kotlin is supported. Adding new language support is trivial, it requires a regex rule for the language that specifies
the import syntax.</li></ul>
<ul>
<li>
Add reporting and some diagrams or something</li>
</ul>