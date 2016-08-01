Title: Boost Your USB WiFi Signal Strength for Next to Nothing 
Date: 2014-02-22 18:00
Author: James 
Category: Projects
Tags: Making, Wifi
Slug: boost-your-wifi-signal-strength-for-next-to-nothing
Header_Cover: https://farm8.staticflickr.com/7059/13949198132_48ccd0f392_c.jpg
Status: published 

In my workshop I have a [Raspberry Pi][raspberry pi] whose primary function is to control the temperature of my home brew using [Braubuddy][braubuddy].

Said workshop is part of a detached garage, so I planned to employ a USB WiFi adapter to connect the Pi to my home wireless network. This would allow me to:

* Update software on the Pi without unplugging and taking it inside.
* Monitor the temperature of my home brew remotely.
* Stream music while I make beer and build things.

But as it turned out, the WiFi adapter's tiny internal aerial wasn't capable of maintaining a reliable connection to my Wireless Access Point. On the rare occasions that it did manage to connect, data transfer was hideously slow due to packet loss. Inevitably the link would drop out altogether as Linux' WiFi connection manager gave up in utter despair.

I had resigned myself to buying a USB module with an external aerial until I stumbled across [this article][wooden dish] in my Twitter feed. The author describes a similar predicament to my own as well as his solution: a home-made, foil-covered dish mounted behind his Wifi adapter.

<!-- PELICAN_END_SUMMARY -->

This reminded me of a blog post I read many years ago in which the author utilised a deconstructed Coke can to similar effect. That article is now one of a slew of results returned by a search for '[coke can wifi dish][can dish]'. So it seemed that plenty of people have successfully boosted their Wifi signal strength using these fantastically ghetto [parabolic antennae]. Such a solution would cost me next to nothing, so I set about testing it for myself.

With a wireless connection established, I began sending [pings][ping] from the Raspi to my Wireless Access Point. Round-trip times hovered around ~15ms, spiking to 25-100ms and occassionally timing out due to packet loss. Eventually the connection dropped out altogether.

Could a simple reflector improve the situation?

Just as my fingers grasped the ring-pull of a fresh can of Coke, I remembered a roll of aluminium sarking left over after some roof repairs:

![sarking roll][sarking roll]

This sarking was ideal for the job, being far stronger than foil and more malleable than a Coke can.

With a square of sarking in one hand...

![sarking square][sarking square]

...and my wifi adapter in the other, I adjusted position and distance while keeping an eye on the Raspi's pings. I wasn't overly confident and so was pleasantly surprised to see pings holding steady at ~10ms with no dropped packets. It worked!

To make a more permanent parabolic antenna I folded my square of sarking over itself...

![sarking folded][sarking folded]

...and then rolled it around a paint can for a vaguely parabolic shape:

![sarking rolling][sarking rolling]

![sarking rolled][sarking rolled]

Finally I mounted my creation on one of my workshop's roof beams using a pair of clouts. These also serve to hold the USB cable and wifi adapter in place:

![finished reflector][finished reflector]

The finished 'dish' performs even better than in testing with pings of ~6ms and no dropped packets after several days of uptime.

A simple, practical and inexpensive solution!

[raspberry pi]: http://raspberrypi.org
[braubuddy]: https://github.com/amorphic/braubuddy
[wooden dish]: https://woodgears.ca/misc/wifi_dish.html
[can dish]: https://www.google.com.au/search?q=coke+can+wifi+dish
[parabolic antennae]: http://en.wikipedia.org/wiki/Parabolic_antenna
[ping]: http://en.wikipedia.org/wiki/Ping
[sarking]: http://en.wikipedia.org/wiki/Sarking
[sarking roll]: https://farm8.staticflickr.com/7305/13949159192_6853019766_c.jpg
[sarking square]: https://farm6.staticflickr.com/5022/13949169292_bf8f18f9ea_c.jpg
[sarking folded]: https://farm8.staticflickr.com/7375/13949155161_3cbf6296f1_c.jpg
[sarking rolling]: https://farm3.staticflickr.com/2939/13949184341_26a378ff27_c.jpg
[sarking rolled]: https://farm8.staticflickr.com/7095/13949194161_074668ebc5_c.jpg
[finished reflector]: https://farm8.staticflickr.com/7059/13949198132_48ccd0f392_c.jpg
