# Kelly Criterion: Zero-Variance Card Game

Source: [Win Vector LLC](https://win-vector.com/2024/12/19/kelly-cant-fail/) - Thomas Cover's problem via Peter Winkler's "Mathematical Puzzles"

## The Game ("Next Card Bet")

- Standard 52-card deck (26 red, 26 black), shuffled
- Start with $1 stake
- Cards exposed one at a time without replacement
- Bet any fraction of current stake on next card's color at 1:1 payoff
- Player can count cards seen to know remaining distribution

## The Kelly Strategy

Maximize expected log of stake. With `r` red and `b` black remaining:

- If r = b: no bet
- If r > b: bet `(r - b) / (r + b)` fraction on red
- If b > r: bet `(b - r) / (r + b)` fraction on black

## The Remarkable Result

**The Kelly strategy has ZERO variance** - always returns exactly ~9.08x initial stake.

This is unusual because Kelly strategies typically:
- Guarantee not to bust
- Maximize expected log growth rate
- But usually high variance, can lose money

## Why It Works: Portfolio Proof

1. There are C(52,26) = 495,918,532,948,104 possible arrangements
2. Create a "portfolio" with 1/C(52,26) allocated to each arrangement
3. Each sub-strategy bets its entire stake assuming its arrangement is correct
4. All but one sub-strategy goes bankrupt; the correct one experiences 52 doublings
5. Final return: `1/C(52,26) * 2^52 ≈ $9.08`

**Key insight**: The Kelly strategy IS the portfolio strategy - they produce identical payoffs.

## Intuition

When betting on majority color:
- Every time we lose, the deck becomes MORE unbalanced (more favorable)
- Kelly sizes the bet so that the gain in edge on a wrong bet offsets the loss of capital
- This is "pricing uncertainty" perfectly

## Connection to Other Problems

- Similar to exploration vs exploitation tradeoffs (like A/B testing)
- Thomas Cover later invented the "universal portfolio" investment strategy

## Python Implementation

```python
def run_bets(is_red) -> float:
    """Run the Kelly betting strategy"""
    stake = 1.0
    n_red_remaining = int(np.sum(is_red))
    n_black_remaining = len(is_red) - n_red_remaining
    for i in range(len(is_red)):
        fraction = abs(n_red_remaining - n_black_remaining) / (n_red_remaining + n_black_remaining)
        bet_red = stake * fraction if n_red_remaining > n_black_remaining else 0
        bet_black = stake * fraction if n_black_remaining > n_red_remaining else 0

        stake = stake - (bet_red + bet_black)
        if is_red[i]:
            stake = stake + 2 * bet_red
            n_red_remaining -= 1
        else:
            stake = stake + 2 * bet_black
            n_black_remaining -= 1
    return stake
```

## Book Reference

Peter Winkler, "Mathematical Puzzles" - highly recommended for this and other problems.
