---
type: link
source: notion
url: https://win-vector.com/2024/12/19/kelly-cant-fail/
notion_type: Tech Deep Dive
tags: ['Running']
created: 2024-12-20T02:15:00.000Z
---

# Kelly Can’t Fail – Win Vector LLC

## Content (from Notion)

## Introduction

You may have heard of the Kelly bet allocation strategy. It is a system for correctly exploiting information or bias in a gambling situation. It is also known as a maximally aggressive or high variance strategy, in that betting more than the Kelly selection can be quite ruinous.

I recently ran into a strange card game where the Kelly strategy is risk free with zero variance. Peter Winkler calls the game “Next Card Bet” in his remarkable book Mathematical Puzzles. The problem and solution appear to come from Thomas Cover. I find this betting game and its analysis amazing, and want to share them with you here.

## The Game

The game is played as follows. A standard 52 card deck consisting of 26 red cards and 26 black cards is shuffled and the player start with a stake of $1. Each card is exposed one at a time, without being replaced in the deck. The player is allowed to bet any fraction of their current stake on whether the next card is black or red at a one to one payoff.

The player clearly has advantageous strategies involving counting the number of black and red cards seen. Counting cards seen lets them know how many cards of each color remain in the unseen portion of the deck. For example they can safely double their stake by not betting on any card other than the last. This allows them to safely bet their entire stake on the now inferable color of the final unseen card.

## The Kelly strategy

The Kelly strategy is to pick a bet that maximizes the expected logarithm of the stake. We can derive it as follows.

Let r be the number red cards remaining in the deck and b black cards remaining. Without loss of generality assume r > b. We then want to maximize P[draw red] * log(1 + bet_fraction) + P[draw black] * log(1 - bet_fraction) as a function of bet_fraction. This expression is maximized where its derivative is zero. The probability of drawing red next is r/(r + b). So we need to solve (r/(r + b)) / (1 + bet_fraction) - (b/(r + b)) / (1 - bet_fraction) = 0. Some algebra tells us bet_fraction = (r - b) / (r + b).

The entire Kelly betting strategy is then:

- If r = b, then no bet
- If r > b bet a |r - b| / (r + b) fraction of your stake on “red”
- If b > r bet a |r - b| / (r + b) fraction of your stake on “black.”
## Trying the strategy

You really should see this strategy in action. It is a strong claim that it is in fact zero variance, so we really should insist on that being confirmed. We will work the example in Python.

In[1]:

```plain text
# import tools
import numpy as np

```

In[2]:

```plain text
# set up our pseudo-random number generator to produce shuffled decks
rng = np.random.default_rng(2024)

```

In[3]:

```plain text
# define our deck shuffling tool
def k_array_with_t_true(k: int, t: int):
    """Create a length-k boolean array with t-True values"""
    is_true = np.array([False] * k, dtype=bool)
    is_true[rng.choice(k, size=t, replace=False)] = True
    return is_true

```

In[4]:

```plain text
# implement our betting strategy
def run_bets(is_red) -> float:
    """Run the Kelly betting strategy"""
    stake = 1.0
    n_red_remaining = int(np.sum(is_red))
    n_black_remaining = len(is_red) - n_red_remaining
    for i in range(len(is_red)):
        # form bet
        bet_red = 0
        bet_black = 0
        fraction = np.abs(n_red_remaining - n_black_remaining) / (n_red_remaining + n_black_remaining)
        if n_red_remaining > n_black_remaining:
            bet_red = stake * fraction
        elif n_black_remaining > n_red_remaining:
            bet_black = stake * fraction
        # derive outcome
        stake = stake - (bet_red + bet_black)
        if is_red[i]:
            stake = stake + 2 * bet_red
            n_red_remaining = n_red_remaining - 1
        else:
            stake = stake + 2 * bet_black
            n_black_remaining = n_black_remaining - 1
    return stake

```

In[5]:

```plain text
# play the game 10000 times
payoffs = [
    run_bets(k_array_with_t_true(52, 26)) for _ in range(10000)
]
assert np.max(payoffs) - 1e-8 < np.min(payoffs)

(np.min(payoffs), np.max(payoffs))

```

Out[5]:

```plain text
(9.081329549427776, 9.081329549427803)
```

For each run we made a return of 9.08 times our starting stake. It is remarkable that there was no variation or variance in the outcomes. Notice this 9.08 times return is much larger than the 2 times return of the simple “wait to the end” strategy.

This result is very unusual for a Kelly strategy. Kelly strategies guarantee to not “bust” (lose all of the money) and to maximize the expected growth rate of the logarithm of the stake. But they usually guarantee little else, can in fact lose money, and are usually high variance. How is it that in this case Kelly can’t fail?

## An explanation

There is a remarkable proof that the strategy is zero variance.

There are (52 choose 26) = 495,918,532,948,104 possible arrangements of red versus black cards. It is a standard result (not proven here) that each of these arrangements is in fact equally likely in a properly shuffled deck.

We define a new “portfolio” strategy as follows.

- Each of the (52 choose 26) possible red/black arrangements is assigned as a sub-strategy in our portfolio.
- We allocate a 1/(52 choose 26) fraction of our initial stake to each sub-strategy. We allow each sub-strategy to keep its own money and do not re-allocate money between sub-strategies.
- Each sub-strategy assumes its assigned red/black arrangement is what is going to happen in the actual deck. The sub-strategy bets its entire stake on each card, betting the card exposed will match the corresponding one it its own defining arrangement.
All but one of the portfolio sub-strategies will lose all of their money- as they eventually bet all their stake on a wrong guess. The single strategy that correctly guesses the entire deck ends experiences 52 doublings and no losses. Thus this strategy multiplies its starting stake by 2^(52). So our portfolio strategy itself always experiences a total aggregate return of $1/(52 choose 26) * 2^(52) ~ $9.08 on an initial $1 stake. This ending portfolio return is independent of the order of the cards.

The claim to finish the argument is: the new portfolio strategy is in fact identical to the earlier Kelly strategy.

Consider what happens to the portfolio when we draw a red card. In our portfolio strategy a r / (r + b) fraction of the non-bankrupt sub-strategies expect the next card to be “red”, and a b / (r + b) fraction of the non-bankrupt sub-strategies expect the next card to be “black”. The next draw bankrupts one of these families, and doubles the other (depending on the drawn color). Some though shows the portfolio strategy evolves its combined stake as follows:

- Aggregate stake goes to stake * 2 * b / (r + b) on drawing “red”
- Aggregate stake goes to stake * 2 * r / (r + b) on drawing “black.”
It is a matter of algebra to confirm this portfolio payoff is exactly the payoff pattern for our earlier Kelly strategy of putting |r - b| / (r + b) on the most common color remaining. The Kelly strategy has exactly the same payoffs as the portfolio strategy, and we have our result that the two strategies are one and the same.

The Kelly strategy is zero variance because it is identical to the portfolio strategy that is itself zero variance.

## Commentary

An idea I like to take away is as follows. As we are betting on majority color, every time we lose a bet the deck becomes more unbalanced and more favorable to us. If we make the bet small enough then the gain in edge on a wrong bet offsets the loss of capital. In this case the Kelly strategy is pricing information or pricing uncertainty just right. This is similar to considerations of “exploration versus exploitation phases” in problems such as A/B testing.

The proof given is from Winkler Mathematical Puzzles. I strongly recommend picking up the book to see his writeup on this and many other problems. The proof itself is very much the style of Cover. This is the Cover who later goes on to invent the universal portfolio investment strategy.


