# Evidence Color Wheel - Visual Bayesian Reasoning Tool

A visual tool for weighing evidence using Bayes' theorem without doing math.

## How It Works

The Color Wheel uses color-coded probability ranges:
- **Red**: Very unlikely (≤5%)
- **Orange**: Unlikely (5-20%)
- **Yellow**: Fairly unlikely (20-40%)
- **Grey**: Uncertain (40-60%)
- **Cyan**: Fairly likely (60-80%)
- **Green**: Likely (80-95%)
- **Blue**: Very likely (≥95%)

## Usage Steps

1. **Prior Probability**: Start on outer ring - how likely was the claim before new evidence?
2. **Positive Conditional**: Second ring - how likely to see this evidence if claim is TRUE?
3. **Negative Conditional**: Third ring - how likely to see this evidence if claim is FALSE?
4. **Result**: Inner segment shows updated probability

## Example: Medical Diagnosis

- Prior: 2% chance patient has rare disease (Red)
- Test sensitivity: 90% true positive rate (Green)
- False positive rate: 10% (Orange)
- Result: Still unlikely patient has disease (Orange)

This demonstrates why even accurate tests can mislead with rare conditions - the base rate matters.

## Resources

- [Introductory Booklet](https://llee454-public-shared-files.s3.us-east-2.amazonaws.com/booklet.pdf)
- [Reference Card Front](https://llee454-public-shared-files.s3.us-east-2.amazonaws.com/card_front.png)
- [Reference Card Back](https://llee454-public-shared-files.s3.us-east-2.amazonaws.com/card_back.png)
- [Poster](https://llee454-public-shared-files.s3.us-east-2.amazonaws.com/rationality_colorwheel+5.png)

Source: [LessWrong](https://www.lesswrong.com/posts/XFTqKnwcPfrMAr2gE/introducing-the-evidence-color-wheel)
