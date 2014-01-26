#!/usr/bin/env python
# -*- coding: utf-8 -*-.
"""
Creates a test database with a couple articles in it.
"""

import db_util



if __name__ == '__main__':
    db_util.build_db('test.db')
    db_util.insert_single('author', ['John', 'Broder'])
    body_1 = u"""
    WASHINGTON — Having established a fast-charging foothold in California for its electric cars, Tesla Motors has brought its formula east, opening two ultrafast charging stations in December that would, in theory, allow a speedy electric-car road trip between here and Boston.

But as I discovered on a recent test drive of the company’s high-performance Model S sedan, theory can be trumped by reality, especially when Northeast temperatures plunge.

Tesla, the electric-car manufacturer run by Elon Musk, the billionaire behind PayPal and SpaceX, offered a high-performance Model S sedan for a trip along the newly electrified stretch of Interstate 95. It seemed an ideal bookend to The Times’s encouraging test drive last September on the West Coast.

The new charging points, at service plazas in Newark, Del., and Milford, Conn., are some 200 miles apart. That is well within the Model S’s 265-mile estimated range, as rated by the Environmental Protection Agency, for the version with an 85 kilowatt-hour battery that I drove — and even more comfortably within Tesla’s claim of 300 miles of range under ideal conditions. Of course, mileage may vary.

The 480-volt Supercharger stations deliver enough power for 150 miles of travel in 30 minutes, and a full charge in about an hour, for the 85 kilowatt-hour Model S. (Adding the fast-charge option to cars with the midlevel 60 kilowatt-hour battery costs $2,000.) That’s quite a bit longer than it takes to pump 15 gallons of gasoline, but at Supercharger stations Tesla pays for the electricity, which seems a reasonable trade for fast, silent and emissions-free driving. Besides, what’s Sbarro for?

The car is a technological wonder, with luminous paint on aluminum bodywork, a spacious and ultrahip cabin, a 17-inch touch screen to control functions from suspension height to the Google-driven navigation system. Feeding the 416 horsepower motor of the top-of-the-line Model S Performance edition is a half-ton lithium-ion battery pack slung beneath the cockpit; that combination is capable of flinging this $101,000 luxury car through the quarter mile as quickly as vaunted sport sedans like the Cadillac CTS-V.

The Model S has won multiple car-of-the-year awards and is, many reviews would have you believe, the coolest car on the planet.

What fun, no? Well, no.

Setting out on a sunny 30-degree day two weeks ago, my trip started well enough. A Tesla agent brought the car to me in suburban Washington with a full charge, and driving at normal highway speeds I reached the Delaware charging dock with the battery still having roughly half its energy remaining. I went off for lunch at the service plaza, checking occasionally on the car’s progress. After 49 minutes, the display read “charge complete,” and the estimated available driving distance was 242 miles.

Fat city; no attendant and no cost.

As I crossed into New Jersey some 15 miles later, I noticed that the estimated range was falling faster than miles were accumulating. At 68 miles since recharging, the range had dropped by 85 miles, and a little mental math told me that reaching Milford would be a stretch.

I began following Tesla’s range-maximization guidelines, which meant dispensing with such battery-draining amenities as warming the cabin and keeping up with traffic. I turned the climate control to low — the temperature was still in the 30s — and planted myself in the far right lane with the cruise control set at 54 miles per hour (the speed limit is 65). Buicks and 18-wheelers flew past, their drivers staring at the nail-polish-red wondercar with California dealer plates.

Nearing New York, I made the first of several calls to Tesla officials about my creeping range anxiety. The woman who had delivered the car told me to turn off the cruise control; company executives later told me that advice was wrong. All the while, my feet were freezing and my knuckles were turning white.

After a short break in Manhattan, the range readout said 79 miles; the Milford charging station was 73 miles away. About 20 miles from Milford, less than 10 miles of range remained. I called Tesla again, and Ted Merendino, a product planner, told me that even when the display reached zero there would still be a few miles of cushion.

At that point, the car informed me it was shutting off the heater, and it ordered me, in vivid red letters, to “Recharge Now.”

I drove into the service plaza, hooked up the Supercharger and warmed my hands on a cup of Dunkin’ Donuts coffee.

If this is Tesla’s vision of long-distance travel in America’s future, I thought, and the solution to what the company calls the “road trip problem,” it needs some work.

The federal government has invested in the effort to find a solution. Three years ago, Steven Chu, the Nobel Prize-winning physicist and secretary of energy, proudly announced a $465 million loan to Tesla as part of an advanced vehicles program intended to cut fossil fuel use and address global warming.

The loan to Tesla would “begin laying the foundation for American leadership in the growing electric vehicles industry,” Dr. Chu said.

At the time, Tesla set a target of producing 20,000 Model S cars by the end of 2013. Some 13,000 eager buyers have reserved 2013 models at prices from about $61,000 to more than $100,000. To give those cars family-vacation capability, the company plans to have 90 Supercharger stations built across the country by the end of 2013.

At the Washington Auto Show last month, Dr. Chu, who has since announced his plan to leave office in the next few weeks, discussed the Energy Department’s goal of making electric vehicles and plug-in hybrids as cheap and convenient as comparable gasoline-powered cars.

He continued: “We can’t say this everywhere in America yet, but driving by a gasoline station and smiling is something everyone should experience.”

I drove a state-of-the-art electric vehicle past a lot of gas stations. I wasn’t smiling.

Instead, I spent nearly an hour at the Milford service plaza as the Tesla sucked electrons from the hitching post. When I continued my drive, the display read 185 miles, well beyond the distance I intended to cover before returning to the station the next morning for a recharge and returning to Manhattan.

I drove, slowly, to Stonington, Conn., for dinner and spent the night in Groton, a total distance of 79 miles. When I parked the car, its computer said I had 90 miles of range, twice the 46 miles back to Milford. It was a different story at 8:30 the next morning. The thermometer read 10 degrees and the display showed 25 miles of remaining range — the electrical equivalent of someone having siphoned off more than two-thirds of the fuel that was in the tank when I parked.

I called Tesla in California, and the official I woke up said I needed to “condition” the battery pack to restore the lost energy. That meant sitting in the car for half an hour with the heat on a low setting. (There is now a mobile application for warming the battery remotely; it was not available at the time of my test drive.)

After completing the battery conditioning process, the estimated range reading was 19 miles; no way would I make it back to Milford.

The Tesla people found an E.V. charging facility that Norwich Public Utilities had recently installed. Norwich, an old mill town on the Thames River, was only 11 miles away, though in the opposite direction from Milford.

After making arrangements to recharge at the Norwich station, I located the proper adapter in the trunk, plugged in and walked to the only warm place nearby, Butch’s Luncheonette and Breakfast Club, an establishment (smoking allowed) where only members can buy a cup of coffee or a plate of eggs. But the owners let me wait there while the Model S drank its juice. Tesla’s experts said that pumping in a little energy would help restore the power lost overnight as a result of the cold weather, and after an hour they cleared me to resume the trip to Milford.

Looking back, I should have bought a membership to Butch’s and spent a few hours there while the car charged. The displayed range never reached the number of miles remaining to Milford, and as I limped along at about 45 miles per hour I saw increasingly dire dashboard warnings to recharge immediately. Mr. Merendino, the product planner, found an E.V. charging station about five miles away.

But the Model S had other ideas. “Car is shutting down,” the computer informed me. I was able to coast down an exit ramp in Branford, Conn., before the car made good on its threat.

Tesla’s New York service manager, Adam Williams, found a towing service in Milford that sent a skilled and very patient driver, Rick Ibsen, to rescue me with a flatbed truck. Not so quick: the car’s electrically actuated parking brake would not release without battery power, and hooking the car’s 12-volt charging post behind the front grille to the tow truck’s portable charger would not release the brake. So he had to drag it onto the flatbed, a painstaking process that took 45 minutes. Fortunately, the cab of the tow truck was toasty.

At 2:40 p.m., we pulled into the Milford rest stop, five hours after I had left Groton on a trip that should have taken less than an hour. Mr. Ibsen carefully maneuvered the flatbed close to the charging kiosk, and 25 minutes later, with the battery sufficiently charged to release the parking brake and drive off the truck, the car was back on the ground. A Model S owner who had taken delivery the previous day watched with interest.

Tesla’s chief technology officer, J B Straubel, acknowledged that the two East Coast charging stations were at the mileage limit of the Model S’s real-world range. Making matters worse, cold weather inflicts about a 10 percent range penalty, he said, and running the heater draws yet more energy. He added that some range-related software problems still needed to be sorted out.

“It’s disappointing to me when things don’t work smoothly,” Mr. Straubel said in a post-mortem of my test drive. “It takes more planning than a typical gasoline car, no way around it.

“Hopefully you’ll give us a little slack in that we put in the East Coast stations just a month ago,” he said. “It’s a good lesson.”

After 80 minutes of charging in Milford, the battery registered an estimated 216 miles of range. The trip to the Tesla dealership in Manhattan was an uneventful 71 miles. When I pulled in, the battery had an estimated 124 miles remaining.

I trust that the next driver savored those miles — and dressed warmly, just in case.
    """
    db_util.insert_single('article', [u'Stalled Out on Tesla’s Electric Highway', body_1, 1])
    body_2 = u"""
    Elon Musk, the chief executive of Tesla Motors, has now responded in detail to the account of my test drive of his Model S electric car, using the company’s new East Coast Superchargers, that was published in The Times on Feb. 10. His broadest charge is that I consciously set out to sabotage the test. That is not so. I was delighted to receive the assignment to try out the company’s new East Coast Supercharger network and as I previously noted in no way anticipated – or deliberately caused – the troubles I encountered.

The test was initially proposed by Tesla to Times editors, and the company arranged the timing, which came during a cold snap on the East Coast. It is fair to say that when I set out I did not fully appreciate how much of an effect the freezing temperatures would have on the travel range of the car.

Since 2009, I have been the Washington bureau reporter responsible for coverage of energy, environment and climate change. I have written numerous articles about the auto industry and several vehicle reviews for the Automobiles pages. (In my 16 years at The Times I have served as White House correspondent, Washington editor, Los Angeles bureau chief and a political correspondent.)

Before I set out in the Model S, I did speak with the company’s chief technology officer, J B Straubel, about the charging network and some of the car’s features and peculiarities. Neither he nor the Tesla representative who delivered the car to me provided detailed instructions on maximizing the driving range, the impact of cold weather on battery strength or how to get the most out of the Superchargers or the publicly available lower-power charging ports along the route.

About three hours into the trip, I placed the first of about a dozen calls to Tesla personnel expressing concern about the car’s declining range and asking how to reach the Supercharger station in Milford, Conn. I was given battery-conservation advice at that time (turn off the cruise control; alternately slow down and speed up to take advantage of regenerative braking) that was later contradicted by other Tesla personnel. I was on the phone with a Tesla engineer in California when I arrived, with zero miles showing on the range meter, at the Milford Supercharger.

A Google Maps screenshot of the Milford, Conn., service plaza with the Tesla Supercharger indicated with a blue marker.A Google Maps screenshot of the Milford, Conn., service plaza with the Tesla Supercharger indicated with a blue marker.
Beginning early in the morning of my second day with the car, after the projected range had dropped precipitously while parked overnight, I spoke numerous times with Christina Ra, Tesla’s spokeswoman at the time, and Ted Merendino, a Tesla product planner at the company’s headquarters in California. They told me that the loss of battery power when parked overnight could be restored by properly “conditioning” the battery, a half-hour process, which I undertook by sitting in the car with the heat on low, as they instructed. That proved ineffective; the conditioning process actually reduced the range by 24 percent (to 19 miles, from 25 miles).

It was also Tesla that told me that an hour of charging (at a lower power level) at a public utility in Norwich, Conn., would give me adequate range to reach the Supercharger 61 miles away, even though the car’s range estimator read 32 miles – because, again, I was told that moderate-speed driving would “restore” the battery power lost overnight. That also proved overly optimistic, as I ran out of power about 14 miles shy of the Milford Supercharger and about five miles from the public charging station in East Haven that I was trying to reach.

To reiterate: Tesla personnel told me over the phone that they were able to monitor the state of the battery. It was they who cleared me to leave Norwich after an hour of charging. I spoke at some length with Mr. Straubel and Ms. Ra six days after the trip, and asked for the data they had collected from my drive, to compare against my notes and recollections. Mr. Straubel said they were able to monitor “certain things” remotely and that the company could store and retrieve “typical diagnostic information on the powertrain.”

Mr. Straubel said Tesla did not store data on exact locations where their cars were driven because of privacy concerns, although Tesla seemed to know that I had driven six-tenths of a mile “in a tiny 100-space parking lot.” While Mr. Musk has accused me of doing this to drain the battery, I was in fact driving around the Milford service plaza on Interstate 95, in the dark, trying to find the unlighted and poorly marked Tesla Supercharger. He did not share that data, which Tesla has now posted online, with me at the time.

Here are point-by-point responses to specific assertions Mr. Musk has made:

• “As the State of Charge log shows, the Model S battery never ran out of energy at any time, including when Broder called the flatbed truck.”

The car’s display screen said the car was shutting down, and it did. The car did not have enough power to move, or even enough to release the electrically operated parking brake. The tow truck driver was on the phone with Tesla’s New York service manager, Adam Williams, for 15 or 20 minutes as he was trying to move the car onto a flatbed truck.

• “The final leg of his trip was 61 miles and yet he disconnected the charge cable when the range display stated 32 miles. He did so expressly against the advice of Tesla personnel and in obvious violation of common sense.”

The Tesla personnel whom I consulted over the phone – Ms. Ra and Mr. Merendino – told me to leave it connected for an hour, and after that the lost range would be restored. I did not ignore their advice.

• “In his article, Broder claims that ‘the car fell short of its projected range on the final leg.’ Then he bizarrely states that the screen showed ‘Est. remaining range: 32 miles’ and the car traveled ‘51 miles’ contradicting his own statement (see images below). The car actually did an admirable job exceeding its projected range. Had he not insisted on doing a nonstop 61-mile trip while staring at a screen that estimated half that range, all would have been well. He constructed a no-win scenario for any vehicle, electric or gasoline.”

The phrase “the car fell short of its projected range” appeared in a caption with an accompanying map; it was not in the article. What that referred to (and admittedly could have been more precise) was that the car fell short of the projected range, 90 miles, that it showed when I parked it overnight at a hotel in Groton, Conn.

Tesla is correct that the car did exceed the projected range of 32 miles when I left Norwich, as I was driving slowly, and it gave me hope that the Tesla employee I’d consulted was correct that the mileage lost overnight was being restored. It wasn’t enough, however, to get to Milford.

• “On that leg, he drove right past a public charge station while the car repeatedly warned him that it was very low on range.”

If there was a public charging station nearby, no one made me aware of it. The Tesla person with whom I was in contact located on the Internet a public charging station in East Haven, Conn., and that is the one I was trying to reach when the car stalled in Branford, about five miles shy of East Haven.

• “Cruise control was never set to 54 m.p.h. as claimed in the article, nor did he limp along at 45 m.p.h. Broder in fact drove at speeds from 65 m.p.h. to 81 m.p.h. for a majority of the trip, and at an average cabin temperature setting of 72 F.”

I drove normally (at the speed limit or with prevailing traffic) when I thought it was prudent to do so. I do recall setting the cruise control to about 54 m.p.h., as I wrote. The log shows the car traveling about 60 m.p.h. for a nearly 100-mile stretch on the New Jersey Turnpike. I cannot account for the discrepancy, nor for a later stretch in Connecticut where I recall driving about 45 m.p.h., but it may be the result of the car being delivered with 19-inch wheels and all-season tires, not the specified 21-inch wheels and summer tires. That just might have affected the recorded speed, range, rate of battery depletion or any number of other parameters. Tesla’s data suggests I was doing slightly more than 50 over a stretch where the speed limit was 65. The traffic was heavy in that part of Connecticut, so cruise control was not usable, and I tried to keep the speed at 50 or below without impeding traffic.

Certainly, and as Tesla’s logs clearly show, much of my driving was at or well below the 65 m.p.h. speed limit, with only a single momentary spike above 80. Most drivers are aware that cars can speed up, even sometimes when cruise control is engaged, on downhill stretches.

• “At the point in time that he claims to have turned the temperature down, he in fact turned the temperature up to 74 F.”

I raised and lowered the cabin heat in an effort to strike a balance between saving energy and staying somewhat comfortable. (It was 30 degrees outside when I began the trip, and the temperature plunged that night to 10 degrees.) Tesla jumped to the conclusion that I claimed to have lowered the cabin temperature “at 182 miles,” but I never wrote that. The data clearly indicates that I sharply lowered the temperature setting – twice – a little over 200 miles into the trip. After the battery was charged I tried to warm the cabin.

• “The charge time on his second stop was 47 minutes, going from —5 miles (reserve power) to 209 miles of Ideal or 185 miles of E.P.A. Rated Range, not 58 minutes as stated in the graphic attached to his article. Had Broder not deliberately turned off the Supercharger at 47 mins and actually spent 58 mins Supercharging, it would have been virtually impossible to run out of energy for the remainder of his stated journey.”

According to my notes, I plugged into the Milford Supercharger at 5:45 p.m. and disconnected at 6:43 p.m. The range reading was 185 miles.

• “For his first recharge, he charged the car to 90%. During the second Supercharge, despite almost running out of energy on the prior leg, he deliberately stopped charging at 72%. On the third leg, where he claimed the car ran out of energy, he stopped charging at 28%. Despite narrowly making each leg, he charged less and less each time. Why would anyone do that?”

I stopped at 72 percent because I had replenished more than enough energy for the miles I intended to drive the next day before fully recharging on my way back to New York. In Norwich, I charged for an hour on the lower-power charger, expressly on the instructions of Tesla personnel, to get enough range to reach the Supercharger station in Milford.

• “The above helps explain a unique peculiarity at the end of the second leg of Broder’s trip. When he first reached our Milford, Conn., Supercharger, having driven the car hard and after taking an unplanned detour through downtown Manhattan to give his brother a ride, the display said “0 miles remaining.” Instead of plugging in the car, he drove in circles for over half a mile in a tiny, 100-space parking lot. When the Model S valiantly refused to die, he eventually plugged it in. On the later legs, it is clear Broder was determined not to be foiled again.”

I drove around the Milford service plaza in the dark looking for the Supercharger, which is not prominently marked. I was not trying to drain the battery. (It was already on reserve power.) As soon as I found the Supercharger, I plugged the car in.

The stop in Manhattan was planned from the beginning and known to Tesla personnel all along. According to Google Maps, taking the Lincoln Tunnel into Manhattan (instead of crossing at the George Washington Bridge) and driving up the West Side Highway added only two miles to the overall distance from Newark, Del., to Milford, Conn.

Neither I nor the Model S ever visited “downtown Manhattan.”

• “When I first heard about what could at best be described as irregularities in Broder’s behavior during the test drive, I called to apologize for any inconvenience that he may have suffered and sought to put my concerns to rest, hoping that he had simply made honest mistakes. That was not the case.”

Mr. Musk not only apologized, he said the charging stations should be 60 miles closer together and offered me a second test drive when additional stations were built.
"""
    db_util.insert_single('article', [u'That Tesla Data: What It Says and What It Doesn’t', body_2, 1])
    print db_util.get_table_contents('article')
    print "*****************"
    print db_util.get_table_contents('author')
