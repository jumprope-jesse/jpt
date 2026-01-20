---
type: link
source: notion
url: https://www.lesswrong.com/posts/XFTqKnwcPfrMAr2gE/introducing-the-evidence-color-wheel
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-12-15T04:44:00.000Z
---

# Introducing the Evidence Color Wheel — LessWrong

## Overview (from Notion)
- The Evidence Color Wheel offers a structured way to evaluate claims and make decisions, which can enhance critical thinking in both personal and professional life.
- As a software engineer and founder, using a systematic approach to weigh evidence can improve problem-solving and decision-making in project management and product development.
- Understanding biases can help in navigating the tech industry, where subjective opinions often cloud judgment.
- The tool can assist you in making informed decisions regarding family health, education, and financial investments by quantifying uncertainty.
- Unique ideas include visualizing probabilities through colors, which can simplify complex concepts and make them more accessible.
- Alternate views might argue that reliance on such tools can lead to overthinking or paralysis by analysis, particularly in fast-paced environments.
- The emphasis on Bayes' theorem connects to data-driven decision-making, which is crucial in technology and entrepreneurship.
- This approach could inspire discussions with peers about rationality and evidence-based practices in both personal and business contexts.

## AI Summary (from Notion)
The Evidence Color Wheel is a tool for assessing the likelihood of claims based on new evidence, using color segments to represent probability ranges. It simplifies the application of Bayes' theorem, helping users weigh evidence quickly and effectively. Practice is encouraged for mastery, supported by additional resources like booklets and reference cards.

## Content (from Notion)

- Version 5.1.0
- December 12, 2024
# Introduction

Weighing evidence is hard. Intuition is liable to a myriad of biases and relies on flawed heuristics. Bayes theory provides a rigorous mathematical basis, but applying Bayes theory in practice is too difficult for most people. Yet, what is more central to thinking critically than being able to weigh evidence correctly?

The Evidence Color Wheel is a tool for weighing evidence. When presented with evidence for a claim, simply move your finger from one color region to the next to determine how likely the claim is given the evidence. The probability that a claim is true is represented by a segment with three colors. The outer color gives the maximum possible probability that the claim is true. The central color gives the probability that the claim is true when the colors values equal those in the legend. The inner color gives the smallest possible probability that the claim is true. These bounds are necessary because each color represents a range of possible values.

A poster describing the Evidence Color Wheel. Feel free to download an print out a copy. The Color Wheel is under an Attribution Creative Commons license!

# Using the Evidence Color Wheel

To use the Evidence color wheel you need to have a claim. A claim is some statement that may or may not be true. For instance, imagine that you are a doctor diagnosing a patient who may or may not have a rare disease. A claim may be that the patient has the given disease.

Next, you must have some new piece of evidence. For example, you may send the patient in for a diagnostic test and get back a positive test result. Before you see this new evidence, you must have some estimate of how likely the claim was to be true. To continue our running example, you may know that the disease is rare. The color wheel tells you how likely the claim is to be true given the new evidence.

## Prior Probability

Start by placing your finger in a colored segment in the outermost ring. If the claim was very unlikely to be true (<= 5% probability) before you saw the new evidence, place your finger in the red segment. If the claim was unlikely to be true (> 5% and < 20% probability) place your finger in the yellow segment. The following table shows how each color segment maps onto probability ranges:

Let's imagine that given our patients symptoms we initially believe that they have a 2% probability of having the disease. Thus, we should start by placing our finger in the outermost ring's red segment.

## Conditional Probability - Positive Case

Next, ask yourself how likely were you to have seen the new evidence if the claim was true. Slide your finger onto the corresponding color segment on the second ring.

To continue, let's imagine that, when our patient has the disease, the test returns a positive result 90% of the time. Thus, when our patient has the disease, we are very likely to see the new evidence (a positive test result). So, we slide our finger to the inner green segment.

## Conditional Probability - Negative Case

Now, ask yourself how likely you were to have seen the new evidence if the claim was false. Slide your finger onto the corresponding color segment in the third ring.

To continue, imagine that the test has a 10% false positive rate. Hence, when a patient does not have the disease, they have a 10% chance of getting a positive test result. Therefore, we slide our finger to the orange segment in the the third ring.

## Reading the Result

To read the result, simply slide your finger into the adjacent inner-most segment. This segment uses colors to communicate the probability that the claim is true given the new evidence. The middle color represents the probability that the claim is true when all of the colors exactly equal the probability in the middle of their respective ranges. The upper color represents the greatest possible probability given that all of the input probabilities fell within their color ranges. Lastly, the lower color represents the minimum possible probability.

Returning to our running example, we slide our finger inward to discover that our patient is unlikely to have the disease. We know this because we land on an orange segment.

In this example, the middle segment gives the correct answer even though our input probabilities did not exactly equal the color middle values. However, we may ask what would happen if all we knew was that the input probabilities fell somewhere within the color ranges. We can easily see the upper and lower bounds on our calculations. Based on our inputs, our patient is at most fairly likely to have the disease.

## The Theory Behind It

The Evidence Color Wheel is based on Bayes’ formula. Given a hypothesis H

and some new evidence E, we can compute the probability that H is true using

the facts that were available before E. We express this probability as P (H). We

then compute the probability that we would have E given that H is true. We

write this probability as P (E|H). Likewise, we compute the probability that we

have E given that H is not true, which we write as P (E|¬H). Bayes formula

tells us how to combine these probabilities to compute the probability that H is

true given E, which we write as P (H|E). Bayes’ formula can be written as

P(H|E)=P(E|H)P(H)=P(E|H)P(H)+P(E|¬H)(1−P(H))

## Learning More

Once mastered, the Evidence Color Wheel allows you to weigh evidence and assess claims within seconds. However, to master the Evidence Color Wheel most people need practice. The Evidence Color Wheel poster includes a booklet that includes additional worked sample problems.

- [Introductory Booklet](https://llee454-public-shared-files.s3.us-east-2.amazonaws.com/booklet.pdf)
- [Reference Card (Front)](https://llee454-public-shared-files.s3.us-east-2.amazonaws.com/card_front.png)
- [Reference Card (Back)](https://llee454-public-shared-files.s3.us-east-2.amazonaws.com/card_back.png)
- [Poster](https://llee454-public-shared-files.s3.us-east-2.amazonaws.com/rationality_colorwheel+5.png)

