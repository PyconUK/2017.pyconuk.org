original_id: E71B
title: "The Modular Mission Planner"
subtitle: "A tool for generating military plans developed by the Ministry of Defence"
speaker: rick-ansell
track: 
video: https://www.youtube.com/watch?v=u9cNjnjomDA
---
The Modular Mission Planner (MMP) is a set of Python libraries that enable the automated production of military plans for use within analytical models.

Mission planning is a major part of setting up a military simulation model, taking significant effort. The time to carry out this process usually dwarfs the time required to carry out the runs. The Mission Planner algorithm employs Genetic Programming to automatically generate suitable plans with minimal human intervention.

The MMP, produced as part of the GAMOV project, builds upon previous work in this area, reimplementing the code in Python and significantly extending the methodology. Key changes include the removal of the need to build model specific versions of the optimiser code, separation of the implementation of plans from their generation and planning against multiple opposing courses of action.

The talk will lightly cover the need that the MMP meets before explaining the method used and its implementation. It will cover how the use of Python has enabled a modular design to be achieved and the advantages this design provides. Reasons for design choices will be covered together with how the Genetic Programming approach employed differs from usual practise.

Whilst some basic knowledge of Genetic Algorithms will be assumed members of the audience who lack this will be able to follow and understand the talk. No mathematics will be required.