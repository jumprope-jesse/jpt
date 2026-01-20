# Calculus Fundamentals

From "Calculus Made Easy" by Silvanus P. Thompson - a classic approach to demystifying calculus.

## Core Symbols

**d** - means "a little bit of" (or "an element of")
- `dx` = a little bit of x
- `dy` = a little bit of y

**∫** - means "the sum of" (or "the integral of")
- `∫dx` = the sum of all the little bits of x = the whole of x
- The word "integral" simply means "the whole"

## Small Quantities and Orders of Smallness

**Key insight**: Everything depends on *relative* minuteness.

- If `dx` is a small quantity (first order), then `(dx)²` is a small quantity of the *second order* of smallness
- Second-order quantities are negligible compared to first-order quantities
- Example: If dx = 1/60 of x, then (dx)² = 1/3600 of x²

**Geometric example**: A square of side x growing by dx:
- New area = x² + 2x·dx + (dx)²
- The term 2x·dx is first-order (significant)
- The term (dx)² is second-order (negligible if dx is small enough)

## Differentiation

**The fundamental question**: What is the ratio dy/dx when both are indefinitely small?

**The process**:
1. Let x grow to x + dx
2. Let y grow to y + dy
3. Find the relationship between dy and dx
4. Discard second-order small quantities

**The power rule**: For y = xⁿ
- dy/dx = n·xⁿ⁻¹
- Works for positive, negative, and fractional powers

Examples:
- y = x² → dy/dx = 2x
- y = x³ → dy/dx = 3x²
- y = x⁻¹ → dy/dx = -x⁻²
- y = x^(1/2) → dy/dx = (1/2)x^(-1/2)

## Constants in Differentiation

**Added constants vanish**:
- y = x³ + 5 → dy/dx = 3x²
- The constant 5 doesn't affect the rate of growth

**Multiplied constants remain**:
- y = 7x² → dy/dx = 14x
- The constant 7 multiplies the result

## Sums, Products, and Quotients

**Sum rule**: d(u+v)/dx = du/dx + dv/dx

**Product rule**: d(u·v)/dx = u·(dv/dx) + v·(du/dx)
- "Treat u as constant while differentiating v, then vice versa, and add"

**Quotient rule**: d(u/v)/dx = [v·(du/dx) - u·(dv/dx)] / v²

## Chain Rule

For composite functions, use substitution:
- If y = f(u) and u = g(x), then dy/dx = (dy/du) × (du/dx)

Example: y = (x² + a²)^(3/2)
1. Let u = x² + a²
2. Then y = u^(3/2), so dy/du = (3/2)u^(1/2)
3. And du/dx = 2x
4. Therefore dy/dx = (3/2)(x² + a²)^(1/2) × 2x = 3x√(x² + a²)

## Time as the Independent Variable

**Velocity**: v = dy/dt (rate of change of distance with time)

**Acceleration**: a = dv/dt = d²y/dt² (rate of change of velocity)

**Newton's fluxional notation** (historical):
- ẏ means dy/dt
- ẍ means d²x/dt²

**Force and motion**:
- F = m·a = m·(d²y/dt²)
- Force = mass × acceleration

## Second Derivatives

Differentiating twice gives the second derivative:
- d²y/dx² (or f''(x))
- Represents the rate of change of the rate of change

For y = x⁵:
- dy/dx = 5x⁴
- d²y/dx² = 20x³
- d³y/dx³ = 60x²
- ... and so on

## Source

[Calculus Made Easy](https://calculusmadeeasy.org/1.html) - Full text available online.

A book originally published in 1910, famous for its accessible approach. Opening line: "The preliminary terror, which chokes off most fifth-form boys from even attempting to learn how to calculate, can be abolished once for all."
