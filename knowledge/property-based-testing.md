# Property-Based Testing

Property-based testing (PBT) is a testing methodology where you define properties that should hold true for all inputs, and the framework generates random inputs to test those properties.

## Key Concepts

- **Properties over examples**: Instead of writing specific test cases, you define invariants that should always hold
- **Random generation**: The framework generates many random inputs to find edge cases
- **Shrinking**: When a failure is found, the framework minimizes the failing input to the simplest case

## When PBT Works Well

- Compiler testing
- Numerical/algorithmic code
- Serialization/deserialization (roundtrip property)
- Data structure invariants
- Any domain where properties are easier to express than expected outputs

## Major Tools

| Language | Library |
|----------|---------|
| Haskell | QuickCheck (original) |
| Python | Hypothesis |
| Clojure | test.check, spec |
| JavaScript | fast-check |
| Rust | proptest, quickcheck |

## Research: "Property-Based Testing for the People"

Dissertation by Harrison Goldstein (UPenn, advised by Benjamin C. Pierce) addressing practical PBT challenges:

**Key contributions:**
- Generators as free monads - enables multiple interpretations, potentially unifying different PBT frameworks
- Generator "derivatives" - avoids precondition failures without rejection sampling
- **Tyche** - tool for visualizing test data distribution

**Problem addressed:** Complex constraints are hard to generate for. Traditional approach uses rejection sampling (generate, check, discard if invalid) which can be inefficient.

Related work: Benjamin C. Pierce's "(When) Will Property-Based Testing Rule The World?" describes PBT as a "lightweight formal method."

## References

- [UPenn Publication](https://repository.upenn.edu/entities/publication/72ca3499-c5f6-4fc1-b5a3-9d66d8dd534e)
- [Hacker News Discussion](https://news.ycombinator.com/item?id=42612211)
- Haskell Interlude podcast, episode 59
