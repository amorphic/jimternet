Title: YOW! 2016 Sydney Day One 
Date: 2016-12-09 12:00
Author: James 
Category: Musings 
Tags: YOW, development
Slug: yow_2016_sydney_day_one
Header_Cover: https://c1.staticflickr.com/1/515/30678714704_e62d0fecf8_c.jpg
Status: published

It doesn't seem like a year since the Sydney software develoment community last gathered at the [ATP][australian technology park] [2015][yow 2015 day one] [edition][yow 2015 day two] of [YOW!][yow sydney]. But time flies when yu're having fun and hopefully you've spent 2016 having as much fun as I have making software and other cool stuff...

![spark staff train][spark staff train]

<!-- PELICAN_END_SUMMARY -->

_Below are references to my notes from specific talks. You can check them out collectively in a github repo [here][notes]._

This year's opening keynote was delivered by none other than long-time coder, author and all-round software development sage [Robert Martin][uncle bob]. In _The Scribe's Oath_ Uncle Bob compared software developers to the scribes of ancient times and the parallels were surprisingly numerous: scribes used checksums, source control, formatting guidelines and even (code) review. They also wrote in languages that were essential for society to function but most people had no interest in learning. Sadly the analogy falls down at the part where scribes paid no taxes...  

![uncle bob presenting][uncle bob presenting]

Uncle Bob then took us through an abridged history of the software development industry and made the interesting point that the number of software developers in existence _doubles roughly every 5 years_. This is an astonishing number which points to the perpetual lack of experience in the field. Bob drew attention to the risks this poses as software becomes ever more necessary to our daily lives and presented the beginnings of a set of guidelines that might be used by developers to self-regulate. If one day a software bug causes the deaths of a large number of people, there will be no excuses...

As we're continuing down the path of Containerising All The Things in my day job I wasn't going to miss Ian Crosby's _Going Cloud Native with Docker_. As a consultant who helps organisations transition to cloud-based, containerised solutions I was relieved to hear that they too struggled to keep pace with the various tools and technologies in this field. Ian highlighted the advantages of containerisation for build and deployment pipelines but also noted a few areas where containers are still not the most appropriate solution - specifically traditional databases that aren't necessarily designed to scale horizontally. I revisited this and the subject of persistent storage in question time and while there are no silver bullets, Ian did recommend [Flocker][flocker] as a reliable and FOSS solution.

I've heard quite a bit about [LLVM][llvm] of late. While it's not something that I'll likely need to do any time soon, I was very glad to have attended Erik Corry's _Building Your Own Compiler The Slightly Easier Way With LLVM_. Erik was a core developer of Google's V8 Javascript engine and is now working on the Dart language so he's about as qualified as one could be to present such a talk. Erik's light-hearted and entertaining presentation style coupled with some really great live(ish)-coded examples really helped to demystify what is a reasonably complex subject. I was interested to know whether there are any cases where one would _not_ use LLVM and Erik helpfully clarified that LLVM is great for most situations its JIT compilation is perhaps not fast enough for production... yet...

![erik llvm][erik llvm]

I haven't done much work with Big Data but for something completely different I dropped in on _Linking Open Government Data at Scale_ by Bernadette Hyland and was very glad to have done so! Bernadette introduced the concept of [linked data][linked data] and explained how it is used by most of world's biggest organisations both commercial (Facebook, Google etc) and non-commercial such as NASA and Bernadette's own employer the US EPA. In hindsight the idea of a _lingua franca_ for modelling data makes perfect sense and it's great to be aware that these data sets exist and how they might be employed!

Next Josh Duck from Facebook talked about _Designing Infra For Big Teams_. He made the point that sharing infrastructure such as frameworks between teams in large organisations makes sense for a great many reasons - from shared tooling and knowledge transfer to allowing product teams to focus on products and framework teams to chase the long tail of framework optimisations. This was all presented through the lens of framework evolution at Facebook culminating in the now wildly popular React and Relay. Very interesting stuff.

![fb evolution][fb evolution]

The last couple of talks I attended on day one were less technical, focussing more on people and processes. In _Engineering You_ Martin Thompson talked about the practice of being a good developer. He touched on the history of engineering and the evolution of the various disciplines and then talked about how we can continue to improve in a field that is evolving so rapidly. As always it pays to spend more time learning fundamentals and good general practices rather than trying to be an expert in every new Javascript framework that comes along. The fundamentals haven't changed much in half a century of computing, but that framework you're using will likely be old hat in a year or two.

Rounding out the day was the outstanding Prof/Dr Brian Little with _Personalities at Work_ - a highly engaging study of the differences between introverts and extraverts. Brian is an acclaimed speaker and his talk was as riveting and poignant as it was hilarious - take a look at his [media page][brian little videos] for an idea of how great a speaker he really is. One very noteable point was made late in the talk when Brain talked about Fixed Traits vs Free Traits. We can avoid our inherent character traits as introverts or extravert for periods of time int he name of love or professionalism. But protractively acting out of character can be harmful in many ways. It's important to find a Restorative Niche - Brian happens to find his in the toilet.

To cap off such an entertaining talk we were left with this thought-provoking slide: the average number of times 1980's German introverted and extravert men and women had sexual intercourse in a given month:

![average intercourse][average intercourse]

You may drawa your own conclusions. Looking forward to Day Two! 

[yow 2015 day one]:/yow_2015_sydney_day_one
[yow 2015 day two]:/yow_2015_sydney_day_two
[yow sydney]:http://sydney.yowconference.com.au
[notes]:https://github.com/amorphic/yow_2016
[australian technology park]:http://www.atp.com.au
[sparkcc]:http://sparkcc.org

[spark staff yow]: https://c1.staticflickr.com/1/515/30678714704_e62d0fecf8_c.jpg
[spark staff train]: https://c6.staticflickr.com/1/716/30710372533_b098ffb3f2_c.jpg
[uncle bob presenting]: https://c6.staticflickr.com/1/507/31519507285_db42883ef7_c.jpg
[uncle bob]: https://en.wikipedia.org/wiki/Robert_Cecil_Martin
[flocker]: https://clusterhq.com/flocker/introduction
[llvm]: http://llvm.org
[linked data]: https://en.wikipedia.org/wiki/Linked_data
[epa]: https://www.epa.gov
[erik llvm]: https://c7.staticflickr.com/1/654/30678780974_c8c54f63fb_c.jpg
[fb evolution]: https://c7.staticflickr.com/6/5585/31148222590_e83d80e250_c.jpg
[brian little videos]: http://www.brianrlittle.com/Topics/media/
[average intercourse]: https://c7.staticflickr.com/1/112/31482337686_3ef30cc721_c.jpg
