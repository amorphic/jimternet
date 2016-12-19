Title: YOW! 2016 Sydney Day Two
Date: 2016-17-09 01:00
Author: James 
Category: Musings 
Tags: YOW, development
Slug: yow_2016_sydney_day_two
Header_Cover: https://c3.staticflickr.com/1/303/30812145474_66436245a6_c.jpg
Status: published

After all the fun of [day one][yowpythonic-staff/ 2016 day one] I was a little late arriving at day two of YOW! Sydney 2016 and unfortuantely missed the opening keynote (booooo...). But I eventually arrived back at the old Redfern train workshop, this time brandishing the [Pythonic Staff of Enlightenment][pythonic staff]...

![james pythonic][james pythonic]

...and all set for anther day of interesting Software Development talks.

<!-- PELICAN_END_SUMMARY -->

_Below are references to my notes from specific talks. You can check them out collectively in a github repo [here][notes]._

First up Sean Chittenden from leading Open-Source tooling company Hashicorp espoused the virtues of _Incrementalism: A Strategy For Adopting Modern Automation_. His metaphor of the environment as a factory made a lot of sense... 

![devops factory][devops factory]

...particularly as a fellow Ops Guy who spent many years in an "awful almost-static CMDB universe". He sensibly recommended moving to dynamic secrets management using Hasicorp's own [Vault][vault] as well as DNS-based service discovery and of course [Terraform][terraform] for provisioning. His take home points:

1. Codify Everything
2. Pre-plan outcomes at build-time
3. Create reproducible artifacts
4. Idempotent APIs and Tooling
5. Developer-centric Operations
6. Make small, well-understood changes
7. Start where it makes sense for your organisation

Continuing the DevOps track was Dave Farley presenting _The Rationale for Continuous Delivery_. He discussed CD as the logical extension of CI and the difference that an improved cycle time can make to an organisation. Having practiced CI I honestly didn't require much convincing of its virtues but Dave reinforced some good practices such as bringing painful parts of the process forward to demonstrate to all concerned the value of working towards CI adoption. He also noted some of the common excuses for _not_ adopting CI and some useful counters: if somebody at your organisation says it's not possible to release so quickly/regularly kindly inform them that Amazon release to >10k hosts every 11.6 seconds.

After a short break to imbibe the Dark Brown Liquid of Concentration, Uncle Bob Martin was up on stage once again. This time he was discussing a thorny topic that is of great interest to me: estimation. Bob presented a helpful formula for estimation which attempts to account for unknowns and re-iterates one of his key points: estimates should be ranges rather than fixed dates:

![uncle bob estimation][uncle bob estimation]

A key point was something that I learned many years ago: we must be willing to say "No" to the impossible rather than saying "Yes" and then underdelivering. When asked what to do in the case of an "absolute" deadline Bob's advice was to trim features. Adding people is another option but it is important to remember that for the first few months those new people are likely to slow produtivity before they increase it. An organisation needs the scale to be able to absorb that.

I really didn't know what to expect from Jon Manning in his talk _How Do I Game Design? Design Games, Understand People!_. But I was an avid gamer for many years and always had an interest in the industry so I figured it would be interesting. I was right!

Jon (fittingly dressed in a lab coat) discussed the core idea of "fun": what it actually means, how it differs in games as opposed to other mediums and how the design of a game ultimately evokes fun in the player. I found this truly fascinating, particularly his discussion of game mechanics (set by the designer) which in turn create dynamics (things which happen when the player interacts with the dynamics) and ultimately create aesthetics (the emotions experienced by the gamer that are the "fun"). The example of Half-Life 2's infamous _Ravenholm_ brought back great memories: the complete shift in game mechanics (from abundant ammo to scarce ammo and poisoned head-crabs that immediately sap your heath to 1) made for interesting new dynamics and ultimately terror, fear and fun for the player!

While we're not all game developers Jon pointed out that we can apply similar methodologies to user interface design. Beginning with the _aesthetics_ we wish to evoke in our users we can work back through the _dynamics_ which might bring forth those aesthetics and finally build the interface _mechanics_ required to allow those dynamics to emerge. Awesome stuff. 

![aesthetics dynamics mechanics][aesthetics dynamics mechanics] 

Emily Webber's _Communities of Practice: The Missing Piece of your Agile Organisation_ was another talk which resonated with me. Having previously worked at a large-ish organisation who attempted (reasonably successfully) to apply the [agile scaling practices of Spotify][scaling agile at spotify] I recognised the similarities between a _Community of Practice_ and Spotify's _Guilds_. I remember voluntarily joining the _Python_ Guild/CoP and finding enoromous value in being part of such a community existing outside of my regular team.

![scaling agile at spotify][scaling agile at spotify]

Emily recommendations for starting a CoP were also _remarkably_ similar to my own experience starting our makerspace [SparkCC][sparkcc]. The process of forming a loosely-knit group of like-minded individuals into a more formal community, helping that community to mature and encountering some of the more common pitfalls along the way were all stages we experienced over the past 1.5 years as we grew SparkCC into the established 'space that it is today. The various "levels" of member were also familiar to me not only through the SparkCC community but also through my involvement in Open Source projects. Members exist on these various levels and move between them over time:

1. Core (you need at least a couple of these)
2. Active
3. Occasional
4. Peripheral (lurkers who watch but don't take part)
5. Outsider (not a member but might be involved in some way)

Rounding out the conference was SafeStack co-founder and all-round Security Sorceress Laura Bell talking _Simplicity, Complexity and Security_. Laura discussed the particular challenges of building secure systems in an agile world characterised by a high rate of change and an increasingly complex stack of emergent technologies. In many (most?) cases security is generally considered an afterthought, something to be applied after an application is "mature". This was a bad approach to building Monoliths in which we had one big, hard-to-rationalise ball-of-code but it utterly falls apart when applied to a Microservices architecture comprised of lots of small, hard-to-rationalise balls of code. Laura asked the pertient question: _If you can't draw your architecture on one page how will you find the gaps?_

Some of the key suggestions for mitigating this emergent security shortfall were to by all means Automate All The Things but also take time to understand the way in which this automation works so as to identify potential security holes. Start by documenting your infrastructure! With the vast increase in tooling required to achieve this automation this advice went hand-in-hand with the directive to only run code from trusted sources and to get involved in the Open Source projects which make this all happen. There's no excuse to not be improving the tools you use and pushing those contributions upstream. Ultimately while it's exciting to be a Pioneer, it's in all of our interests to strive to become Settlers as soon as possible.

With that all that was left was for Dave Thomas to thank all concerned and officially declare it beer o'clock...

![farewell][farewell]

Another interesting, insightful and thoroughly enjoyable ediiton of YOW! See you next year!

[yow 2016 day one]:/yow_2016_sydney_day_one
[pythonic staff]:/pythonic-staff/
[james pythonic]:https://c1.staticflickr.com/1/487/31280958680_d126a831df_c.jpg
[notes]:https://github.com/amorphic/yow_2016
[yow topper]:https://www.flickr.com/photos/22253037@N00/31616917106/in/album-72157675872735022/
[devops factory]:https://www.flickr.com/photos/22253037@N00/30812155444/in/album-72157675872735022/
[vault]:https://www.hashicorp.com/vault.html
[terraform]:https://www.hashicorp.com/terraform.html
[uncle bob estimation]: https://c2.staticflickr.com/1/436/31653479545_378bdc9c56_c.jpg
[aesthetics dynamics mechanics]:https://c4.staticflickr.com/1/67/31653478835_7797ddc09d_c.jpg
[community maturity stages]:https://c5.staticflickr.com/6/5556/30812147164_34edb9a276_c.jpg
[scaling agile at spotify]:https://dl.dropboxusercontent.com/u/1018963/Articles/SpotifyScaling.pdf
[sparkcc]:http://sparkcc.org
[farewell]:https://c3.staticflickr.com/1/303/30812145474_66436245a6_c.jpg
