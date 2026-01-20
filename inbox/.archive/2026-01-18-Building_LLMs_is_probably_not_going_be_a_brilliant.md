---
type: link
source: notion
url: https://calpaterson.com/porter.html
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-11-27T02:08:00.000Z
---

# Building LLMs is probably not going be a brilliant business

## Content (from Notion)

The Netscapes of AI

   Railways improved the lives of millions - but investors were rewarded with a dramatic bust

Large language models (LLMs) like Chat-GPT and Claude.ai are whizzy and cool. A lot of people think that they are going to be The Future. Maybe they are — but that doesn't mean that building them is going to be a profitable business.

In the 1960s, airlines were The Future. That is why old films have so many swish shots of airports in them. Airlines though, turned out to be an unavoidably rubbish business. I've flown on loads of airlines that have gone bust: Monarch, WOW Air, Thomas Cook, Flybmi, Zoom. And those are all busts from before coronavirus - times change but being an airline is always a bad idea.

That's odd, because other businesses, even ones which seem really stupid, are much more profitable. Selling fizzy drinks is, surprisingly, an amazing business. Perhaps the best. Coca-cola's return on equity has rarely fallen below 30% in any given year. That seems very unfair because being an airline is hard work but making coke is pretty easy. It's even more galling because Coca-cola don't actually make the coke themselves - that is outsourced to "bottling companies". They literally just sell it.

## Industry structure - what makes a business good

If you were to believe LinkedIn you would think a great business is made with efficiency, hard work, innovation or some other intrinsic reason to do with how hardworking, or clever, the people in the business are. That simply is not the case.

What makes a good business is industry structure.

### Airlines - unfavourable industry structure

To be an airline is to be in an almost uniquely terrible market position. For starters, there are only two makers of aeroplanes (Airbus and Boeing). For reasons of training and staff efficiency, you have to commit to one or the other, which gives the aeroplane makers very strong pricing power.

And buyers of airline tickets are incredibly fickle and have no loyalty. They will switch from one "carrier" to another over even small differences in price. Annoyingly, there are loads of other airlines and they're all running the same routes as you!

Worse yet, starting a new airline is surprisingly easy. Aircraft hold their value so banks will happily lend against them. There are loads of staff available that new entrants can hire. So randos will continually enter your market, often selling tickets below cost for quite a while before they go bust. And to top it off, there are plenty of substitutes for air travel - from government-subsidised high speed trains to Zoom calls.

Airlines that get more efficient, work harder or come up with innovations aren't going to be able to "capture" the value of what they've done. If you make more than the bare minimum to survive Airbus will notice that you're being undercharged and you'll find that the next renewal on your service contract eats up the difference.

### Fizzy-drinks - very favourable industry structure

Being the Coca-cola company is pretty great though.

Coke is just water, colourant, flavouring, caffeine and sweetner. Those are all widely available and really cheap. And as I said, you don't even have to combine them yourselves - bottling companies will do that for you for almost nothing.

Handily, consumers are really picky about what goes in their mouth. The unofficial motto of your main competitor is "Is Pepsi ok?". This is despite the fact that they are identical in both taste and colour. And a significant minority of people actually say no!

And it isn't easy for new competitors to enter the market. They can't call their new drink "coke" due to trademarks. They have to call it something else. And consumers will generally refuse it because drinking an alternative is considered some kind of weird statement.

## What is industry structure?

Classically, there are five basic parts ("forces") to a company's position:

1. The power of their suppliers to increase their prices
1. The power of their buyers to reduce your prices
1. The strength of direct competitors
1. The threat of any new entrants
1. The threat of substitutes
It's industry structure that makes a business profitable or not. Not efficiency, not hard work and not innovation.

If none of the forces are very much against you, your business will do ok. If they are all against you, you'll be in the position of the airlines. And if they're all in your favour: brill, you're Coca-cola.

## The industry structure of LLM makers: OpenAI/Anthropic/Gemini/etc

So is the position of LLM makers any good? I'm afraid it's not good news.

LLM makers sometimes imply that their suppliers are cloud companies like Amazon Web Services, Google Cloud, etc. That wouldn't be so bad because you could shop around and make them compete to cut the huge cost of model training.

Really though, LLM makers have only one true supplier: NVIDIA. NVIDIA make the chips that all models are trained on - regardless of cloud vendor. And that gives NVIDIA colossal, near total pricing power. NVIDIA are more powerful relative to Anthropic or OpenAI than Airbus or Boeing could ever dream of being.

How much power do buyers have over LLM token prices? So far, it seems fairly high. Most LLM users seem willing to change from Chat-GPT to Claude, for example. It doesn't seem like brand loyalty is being built up. And companies that build AI into their businesses are starting to do so via abstraction layers that allows them to switch model easily. That makes LLMs interchangeable - which is bad for those who sell them.

What's the strength of direct competitors? Again, it is considerable. There are loads of LLM vendors and pricing appears competitive. Worst of all, Facebook basically dump their model on the market for no cost. It's reminiscent of Internet Explorer - not exactly a great portent.

And it seems fairly easy for new entrants to build brand new models. That is why there are so many LLM makers. Most of the techniques for making LLMs are openly published in papers. Even bad models can gain customers if they are cheap, which allows new entrants to gain a foothold.

The situation on substitutes is mixed. Instead of having Chat-GPT write some text you could pay a person to do it instead. That is likely to be much more expensive but also less likely to hallucinate, which might be important for some usecases (law is the field least likely to use LLMs). And then there is the trend that metadata tends to displace artificial intelligence once particular application has been proved out.

But a single mildly positive point does not make a profitable business. LLM makers look a lot more like Netscape - who invented graphical web browsers, then went bust - than Google, who made something good that ran on top of the the web browsers.

## How are they raising so much money?

If LLM makers seem cursed to an airline-style business destiny, how come they are able to raise so much money? OpenAI raised $6.6 billion at a valuation of $157 billion less than two months ago. That might be the biggest VC round of all ime.

What do they know that I don't? It is a mystery - but let's consider the options.

Perhaps they are hoping to develop their own chips to reduce their dependance on NVIDIA. $6.6 billion is not enough to build a new fab but it might be enough to get a new chip designed which allows them to migrate off NVIDIA. That would save them paying so much money for GPU time. But, NVIDIA are actually one of the investors in the round (although only a fairly small amount) - so it's unlikely "develop an NVIDIA competitor" was on any of the pitch deck slides.

Perhaps OpenAI are hoping to build a strong brand so that customers won't switch so easily. It's not impossible, there is proof the branding and lock-in can work in technology - but it seems difficult to manage given that LLMs themselves generically have a textual interface - meaning that there is no real API as such - you just send text, and it sends text back.

Can they do anything about new entrants? Possibly. If investing $6.6bn allows them to develop a major improvement in their model then that would raise everyone else's costs considerably and probably force some of them smaller competitors out of the market. The trouble is the money is the most fungible of all goods (that is the point, after all) and that $6.6bn is not all that much of it. So this round wouldn't, by itself, be enough to dissuate others. I used to work at a bank and I can tell you that individual bond raises can be a lot more than $6.6bn.

It's worth saying that even companies that raise huge sums of money sometimes can turn out to have no viable business. WeWork ultimately raised over $10bn at a valuation of $47bn before it was realised that their business simply did not work. WeWork were valued at $0.56bn in their most recent financial restructuring - having lost well over 95% of what was invested.

## Not all AI companies are doomed

If LLM makers aren't going to be good businesses, does that bode ill for The Future?

Firstly, it does not mean the technology will be bad. Whether the technology ends up being good or not is mostly unrelated to whether Open AI/Anthropic/Mistral/whoever makes any money off it. Container virtualisation technology is pretty well developed even though Docker made almost nothing out of it. Web browsers are extremely advanced pieces of software even though making a browser is such a bad business that most don't even count it as a business at all. And CRMs are terrible despite the fact that Salesforce is tremendously successful. Technology success and business success are mostly unrelated.

And then: not all AI businesses are building models. Ideally, if I were running an AI business I would avoid building a model at all costs. Building your own models looks like a undifferentiated schlep. Using a tiny bit of some expensively trained model that Anthropic has produced could be very cost effective and might make some business idea work that wouldn't have 5 years ago.

## Beware software companies that aren't software companies

Software companies are really good businesses. You have no real suppliers, your software is often unique so there are no competitors andd the substitute is just doing it yourself. For this reason, software companies generally have really great margins.

The problem is that not all technology companies are software companies. If you have a hugely powerful single supplier like NVIDIA then the economics of your company are going to less like Microsoft Office and more like Pan-Am.

## Contact/etc

Write to me at cal@calpaterson.com about this article, especially if you disagreed with it.

See other things I've written or learn more about be on my about page.

Get an alert when I write something new, by email or RSS .

I am on:

- Mastodon
- Twitter
- Github
- and Linkedin.
## Other notes

The AI safety movement is a fantastic hypeman for LLMs as a technology. Implying (pretty dubiously) that we are 10 minutes from midnight in some kind of Ghost-in-The-Shell style AI crisis is in fact an extremely effective form of product marketing. Perhaps that is why OpenAI and others employ so many AI safety specialists.

The Coca-cola company mainly sit back and rake in the megabucks - but they do spend a little bit of their earnings on research. And a little bit of a lot is still significant. It's interesting that that cokes market research has discovered that coke works better as a gender segregated product: Coke Zero is Diet Coke, for men.

If you want to read more about industry structure and market strategy, the place to start is with Michael Porter. He reworked his famous essay The Five Forces that Shape Corporate Strategy in 2008. It's not the last word, but it probably should be the first word you read if you want to learn more.


