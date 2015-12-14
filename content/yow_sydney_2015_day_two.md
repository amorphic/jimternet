Title: YOW! 2015 Sydney Day Two 
Date: 2015-12-14 15:00
Author: James 
Category: Musings 
Tags: YOW, development
Slug: yow_2015_sydney_day_two
Status: published

After an interesting and informative [Day One][yow 2015 day one], YOW! 2015 Sydney day two got off to a geektastic start with Anita Sengupta and Kamal Oudrhiri talking about their fascinating work on the [Curiosity Rover][Curiosity Rover]. It was quite humbling to be in the presence of engineers involved in such a groundbreaking project and we heard about interesting problems the team had to solve including how to slow an entry vehicle from 30,000 mph to 0 mph in 7 mins and the infamous [Sol 200][Sol 200] anomaly.

<!--more-->

_Below are references to my notes from specific talks. You can check them out collectively in a github repo [here][notes]._

Dean Wampler talked about [Big Data and the JVM in relation to his work with the Spark Project][Scala and the JVM as a Big Data Platform: Lessons from the Spark Project]. I've not had a lot of exposure to Big Data problems and infrastructure but Spark does seem like a huge improvement over previous tools such as MapReduce. His stories of JVM tuning did remind me of a previous life configuring Garbage Collection parameters for [Apache Flume][flume example plugins] - the thought of it still makes me shudder. Interestingly one of Dean's closing comments was that "Spark + Mesosphere is the platform of the future"...

Matt Ranney showed us a history of Uber's tech stack and made us feel better by demonstrating how along the way [they'd broken just about everything][Desiging for Failure: Scaling Uber's Backend by Breaking Everything]. He made the interesting point that outages for Uber represent real money as it's not a service people linger on like social media etc - if Uber's not there to provide a ride the user goes elsewhere. He also didn't mention Microservices hardly at all...

<center>![say microservices one more time][say microservices one more time]</center>

We all know that we should be striving for agile organisation and practice. But Don Reinersten's fanastic talk [Thriving in a Stochastic World][Thriving in a Stochastic World] did an outstanding job of explaining why against a backdrop of solid theory. His description of older up-front planning methods as squandering the gifts of new information and his examples of similar decision-making processes on the modern battlefield were a real revelation. 

[Writing a Writer][Writing a Writer] was a refreshingly different talk. Richard P. Gabriel took us through Inkwell - his labour of love for the past 3 years and his own attempt to answer the quesiton "Can a program write like a writer?". A lot of technical detail of the architecture of both the Inkwell source and the prose it produced led me to ask the question "How does one find bugs in code with an output as non-deterministic as poetry?". "With great difficulty" apparently. I loved one audience member's observation that this is the kind of "fun" and "real" programming a lot of us enjoy. Richard concurred by remarking that in recent decades "Software Development" has largely become "Product Development". Indeed.

Finally to round things out we had the long-awaited DevOps track!

First up, Alexandra Spillane (Ops) and Matt Callanan (Dev) talked about how they [Made Easy Right][DevOps at Wotif - Making Easy Right] when implementing DevOps practices at Wotif. They described how they tackled a painfully slow and labourious deployment process and brought together Dev and Ops with the blessing of Management to work together on a replacement. Interesting was their approach of building a new, fast pipeline to prodcution and allowed any teams to use it provided they adhered to documented interface standards and levels of testing. Make something better and help people migrate - use the carrot not the stick!

And to conclude, the much-discussed topic of [Using Docker Safely][Using Docker Safely] presented by Adrian Mouat. Adrian literally wrote the book on this topic and presented us with a container security philospohy ('Defence in Depth - a castle has a moat, walls, several keeps) along with common attack vectors and finally en extensive list of tips for combatting them. Top tip: run your containers in VMs, then you still get the underlying 'Gold Standard' of VM security.

<center>![closing speech][closing speech]</center>

All that was left was to toast the organisers of another fun and insightful edition of YOW! - see you at #YOW16!

[yow 2015 day one]: /yow_2015_sydney_day_one
[notes]:https://github.com/amorphic/yow_2015
[Engineering and Exploring the Red Planet]: https://github.com/amorphic/yow_2015/blob/master/engineering_and_exploring_the_red_planet.md
[Scala and the JVM as a Big Data Platform: Lessons from the Spark Project]: https://github.com/amorphic/yow_2015/blob/master/lessons_from_the_spark_project.md
[Desiging for Failure: Scaling Uber's Backend by Breaking Everything]: https://github.com/amorphic/yow_2015/blob/master/scaling_uber_by_breaking_everything.md
[Thriving in a Stochastic World]: https://github.com/amorphic/yow_2015/blob/master/thriving_in_a_stochastic_world.md
[Writing a Writer]: https://github.com/amorphic/yow_2015/blob/master/writing_a_writer.md
[DevOps at Wotif - Making Easy Right]: https://github.com/amorphic/yow_2015/blob/master/devops_at_wotif.md
[Using Docker Safely]: https://github.com/amorphic/yow_2015/blob/master/using_docker_safely.md
[Curiosity Rover]: http://mars.nasa.gov/msl/
[Sol 200]: http://llis.nasa.gov/lesson/11201 
[flume example plugins]: /installing-flume-0-9-4-example-plugins
[say microservices one more time]: https://farm6.staticflickr.com/5718/23736946965_e2c9425f67_z.jpg 
[closing speech]: https://farm6.staticflickr.com/5676/23629304412_81056eb80a_z.jpg 
