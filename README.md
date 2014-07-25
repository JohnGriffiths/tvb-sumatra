#tvb-sumatra

simulation and tracking and management functionality for tvb using the Sumatra python library. 


## What's this then?

The [package documentation](http://pythonhosted.org/Sumatra) describes Sumatra as
    *"...a tool for managing and tracking projects based on numerical simulation and/or analysis, with the aim of supporting reproducible research. It can be thought of as an automated electronic lab notebook for computational projects."


More specifically, Sumatra uses software version control systems such as git to compile a systematic set of metadata for every run of a simulation. This provides two very useful functionalities. Firstly, it automatically logs parameter sets used and results produced for a given simulation run, which can be queried in a convenient database-oriented fashion. Second, it records (using version control systems) when there are differences in the execution code that may go undetected if only the parameters themselves are documented. This is extremeley useful when returning to projects that used earlier software versions, or when carrying out ones that span multiple software updates. 





## Why?

If all this sounds a bit techy or abstract, consider the following motivations given in the documentation linked to above:


     *"I thought I used the same parameters but I'm getting different results"*  

     *"I can't remember which version of the code I used to generate figure 6"*

     *"The new student wants to reuse that model I published three years ago but he can't reproduce the figures"*

     *"It worked yesterday"*

     *"Why did I do that?"*


These scenarios will be familiar to many research scientists. They will most likely have been caused by some combination of a hectic work pace (with a corrsponding variability in the adequacy of documentation), and by the fact that computational research environments are rarely stable for long periods of time. The chief contribution of Sumatra, and of tvb-sumatra, is to leverage the power of version control systems to avoid such situations. 

For a far more comprehensive and informative exposition of Sumatra's rationale and approach, see the package documentation and associated research papers. 


## Usage

- examples in folder
- ..tvb examples
- screenshots...





