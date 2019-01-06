Title: YOW! 2015 Sydney Day One 
Date: 2015-12-11 08:00
Author: James 
Category: Musings 
Tags: YOW, development
Slug: yow_2015_sydney_day_one
cover: https://farm1.staticflickr.com/591/23033818884_79c503ae1d_z.jpg
Status: published

[YOW! Sydney][yow sydney] 2015 got off to a great start yesterday. The timing of Australia's leading Software Development conference could not have been more apt given our Government's recent focus on technology and innovation. Likewise the setting of the [Australian Technology Park][australian technology park] evoked the sense of possiblity inherent in Engineering disciplines, Software comfortably juxtaposed against *real* Hardware...

![atp entry][atp entry]

<!-- PELICAN_END_SUMMARY -->

_Below are references to my notes from specific talks. You can check them out collectively in a github repo [here][notes]._

It was great to be able to chat with likeminded hackers and listen as some masters of their craft shared their knowledge, experiences and more than a few of their secrets. Opening the day was keynote speaker Adrian Cockroft who touched upon the [complicated][It's Complicated] nature of software and how best to organise (or not) the engineers who build it. Of course things are often only complicated to us right up until they're not and often they don't have to be - anybody who's seen a 2-yr-old use an iPhone inherently understands this.

![keynote][keynote]

Adrian also touched upon Microservices - a hot topic at YOW! 2014 and once again this year. His sentiments that the architecture must follow the organisation (he wouldn't be the last speaker to mention [Conway's Law][conways law]) and the importance of service ownership would be elaborated upon in Randy Shoup's [Pragmatic Microservices][Pragmatic Microservices]. Randy covered just about every question one might have regarding How, Why and When to move to a Microservice architecture and reminded us the importance of using the Right Tool at the Right Time.

Sam Newman's excellent [Deploying and Scaling Microservices][Deploying and Scaling Microservices] delved deeper into how best to package software in a microservice architecture and came to the pleasing conclusion that the answer is Docker Containers. Pleasing because I've just spent the past couple of weeks finally getting to grips with containerisation myself. He noted that Docker is only really feasible as a production system when containers may be managed across a fleet of hosts and then discussed the relative merits of the various platforms for doing so: Docker Swarm, Mesos and Kubernetes. It certainly saved me a lot of reading.

Another tennant of Cockroft's keynote was the importance of imposing Purpose rather than Process ("Teach them to yearn for the vast and endless sea") and this was the central theme of [A Day in the Life of a Netflix Engineer][A Day in the Life of a Netflix Engineer] by Dave Hahn. This engaging and entertaining talk gave insight into how Netflix builds and maintains the systems that account for up to 37%(!) of Internet traffic in the US. The engineer-focussed culture that they have created sounds truly inspirational.  

![netflix flux][netflix flux]

Adan Wolff's [Facebook Product Infrastructure][Facebook Product Infrastructure] provided a peek inside the sausage factory that services over 1 billion(!) users daily. Particularly interesting was the way in which developers are able to deploy new or updated features to specific customers by way of Feature Gating. Adan also discussed the importance of questioning established paradigms as Facebook did when developing platforms such as React and GraphQL

Kathleen Fisher's talk on [Formal Methods][Using Formal Methods To Eliminate Exploitable Bugs] highlighted the insecurity still inherent in modern software. Unfortunately this isn't an easy problem to solve and while formal methods offer a means of mitigating security issues they still require a prohibitive amount of time and knowledge to implement. However the [SMACCMCopter][SMACCMCopter] project demonstrated that this is no excuse to ignore security in a rush to market, particularly in the fast-moving world of the Internet of Things. 

Finally Reid Draper disucssed his experience with [Production Haskell][Production Haskell]. Reid demonstrated recent improvements in the build process courtesy of [Stack][Stack] and the possibility of running interpreted for developing in Haskell's REPL. He also showed how to simply test and deploy Haskell applications as well as a few advantages of the Haskell/functional approach.

A wonderful day during which I learned a great deal. Looking forward to day two!

![loco workshop][loco workshop]

[yow sydney]:http://sydney.yowconference.com.au
[conways law]:https://en.wikipedia.org/wiki/Conway's_law
[australian technology park]:http://www.atp.com.au
[A Day in the Life of a Netflix Engineer]:https://github.com/amorphic/yow_2015/blob/master/a_day_in_the_life_of_a_netflix_engineer.md
[Deploying and Scaling Microservices]:https://github.com/amorphic/yow_2015/blob/master/deploying_and_scaling_microservices.md
[Facebook Product Infrastructure]:https://github.com/amorphic/yow_2015/blob/master/facebook_product_infrastructure.md
[It's Complicated]:https://github.com/amorphic/yow_2015/blob/master/its_complicated.md
[Pragmatic Microservices]:https://github.com/amorphic/yow_2015/blob/master/pragmatic_microservices.md
[Production Haskell]:https://github.com/amorphic/yow_2015/blob/master/production_haskell.md
[Using Formal Methods To Eliminate Exploitable Bugs]:https://github.com/amorphic/yow_2015/blob/master/using_formal_methods_to_eliminate_exploitable_bugs.md 
[SMACCMCopter]:http://smaccmpilot.org
[Stack]:http://docs.haskellstack.org/en/stable/README.html
[notes]:https://github.com/amorphic/yow_2015
[atp entry]:https://farm6.staticflickr.com/5650/23366336260_1de435eba3_z.jpg
[keynote]:https://farm1.staticflickr.com/591/23033818884_79c503ae1d_z.jpg
[netflix flux]:https://farm6.staticflickr.com/5709/23294050109_f4d269fc44_z.jpg
[loco workshop]:https://farm1.staticflickr.com/622/23661993845_7320faaaae_z.jpg
