# Unicode and UTF-8 Essentials

## Core Concepts

**Unicode** = A standard that assigns unique numbers (code points) to characters from all human languages
- Code points written as U+XXXX (hexadecimal)
- ~1.1 million possible code points (0x10FFFF max)
- ~170,000 (15%) currently defined
- Updates annually with new characters and rules

**UTF-8** = Variable-length encoding (1-4 bytes per code point)
- 98% of web content in 2023
- Backward compatible with ASCII (0-127 = 1 byte, same as ASCII)
- Space-efficient for Latin text
- Built-in error detection and recovery

## Critical Distinctions

### Three Layers of Text

1. **Bytes** - How data is stored (UTF-8, UTF-16, UTF-32)
2. **Code Points** - Unicode's assigned numbers (U+1F4A9 = 💩)
3. **Grapheme Clusters** - What users perceive as single characters ⭐

**The Key Insight**: Code points ≠ characters. Extended Grapheme Clusters = actual characters.

### Extended Grapheme Clusters

A grapheme = minimally distinctive unit of writing (what users see as "one character")

Examples of single graphemes made from multiple code points:
- `é` = U+0065 (e) + U+0301 (combining acute accent)
- `🤦🏼‍♂️` = 5 code points but 1 grapheme
- `👨‍🏭` = U+1F468 + U+200D + U+1F3ED
- `각` (Korean) = U+1100 + U+1161 + U+11A8

**Consequences**:
- Can't determine string length by counting bytes OR code points
- Can't jump to arbitrary positions in strings
- Can't substring by cutting at byte/code point boundaries
- Must iterate over grapheme clusters, not code points

## UTF-8 Technical Details

### Byte Structure
- 1 byte: `0xxxxxxx` (ASCII compatible, 0-127)
- 2 bytes: `110xxxxx 10xxxxxx`
- 3 bytes: `1110xxxx 10xxxxxx 10xxxxxx`
- 4 bytes: `11110xxx 10xxxxxx 10xxxxxx 10xxxxxx`

### Language Efficiency
- English: 1 byte per character
- Cyrillic, Hebrew, Arabic: 2 bytes
- Chinese, Japanese, Korean, Emoji: 3-4 bytes

### Error Handling
- U+FFFD (�) = Replacement Character
- Appears when Unicode is corrupted/malformed
- Can recover by finding valid byte sequence boundaries

## UTF-16 and Surrogate Pairs

**History**: UTF-16 was supposed to be fixed-width (16-bit), but Unicode outgrew 65,536 characters.

**Surrogate Pairs**: Two 16-bit units encoding one code point
- High surrogate: D800-DBFF
- Low surrogate: DC00-DFFF
- Example: D83D DCA9 (two units) = U+1F4A9 (💩)

**Still Used In**: Windows, Java, JavaScript, C#, .NET, Objective-C

## String Operations - The Right Way

### Don't Trust Built-In Length
```javascript
// JavaScript (UTF-16 units)
"🤦🏼‍♂️".length  // => 7 ❌

// Python (code points)
len("🤦🏼‍♂️")     // => 5 ❌

// Rust (UTF-8 bytes)
"🤦🏼‍♂️".len()   // => 17 ❌

// Swift (grapheme clusters)
"🤦🏼‍♂️".count   // => 1 ✅

// Elixir (grapheme clusters)
String.length("🤦🏼‍♂️")  // => 1 ✅
```

### Use Proper Unicode Libraries

**Recommended**:
- C/C++/Java: **ICU** (International Components for Unicode)
- C#: `TextElementEnumerator`
- Swift: stdlib (does it right by default)
- Elixir/Erlang: stdlib
- Others: Find ICU bindings

**Don't use**:
- Raw byte/char iteration
- Java's `java.text.BreakIterator` (outdated Unicode version)
- Any library not updated to recent Unicode (15.1+ as of 2023)

## Normalization (Critical for Comparison)

Same character, different byte representations:

### Composed vs Decomposed
- `Å` = U+00C5 (single code point)
- `Å` = U+0041 + U+030A (A + combining ring)
- These look identical but `"Å" === "Å"` is FALSE

### Four Normal Forms

1. **NFD** (Decomposed): Explodes to smallest pieces, canonical order
2. **NFC** (Composed): Combines into pre-composed forms
3. **NFKD** (Compatibility Decomposed): Also replaces visual variants (① → 1, ﬁ → fi)
4. **NFKC** (Compatibility Composed): Combines + replaces variants

**Rule**: Always normalize before comparing or searching strings!

## Locale Dependence (The Bad News)

### Same Code Point, Different Rendering
- Russian vs Bulgarian Cyrillic: Same code points, different glyphs
- U+8FD4: Different in Chinese/Japanese/Korean
- Locale metadata required but often lost

### Case Conversion Depends on Language
```java
"I".toLowerCase(Locale.US)  // => "i"
"I".toLowerCase(Locale.TR)  // => "ı" (Turkish dotless i)

"i".toUpperCase(Locale.US)  // => "I"
"i".toUpperCase(Locale.TR)  // => "İ" (Turkish dotted I)
```

## Yearly Updates = Breaking Changes

- Unicode releases major version every year (new emojis, etc.)
- **Grapheme cluster rules change annually**
- What's 2 graphemes today might become 1 tomorrow
- Different app versions may report different string lengths
- Must update Unicode libraries regularly

## ASCII Is Not Enough (Even for English)

Non-ASCII characters in English text:
- Quotation marks: " " ' '
- Apostrophe: '
- Dashes: – —
- Currency: € ¢ £
- Math: − × (minus and multiply, not hyphen and x)
- Symbols: © ™ § † ¶
- Foreign words: café, piñata, naïve

## Best Practices Summary

✅ **Do**:
- Use UTF-8 for storage and transfer (it won)
- Iterate over grapheme clusters, not bytes or code points
- Use Unicode libraries for strlen, indexOf, substring, etc.
- Normalize before comparing strings
- Update Unicode libraries yearly
- Pass locale to case conversion when needed

❌ **Don't**:
- Count bytes/code points and call it "length"
- Substring by byte/code point offset
- Compare strings without normalization
- Iterate code points as if they were characters
- Use outdated Unicode libraries

## Key Takeaway

> There's such a thing as plain text, and it's encoded with UTF-8.

The miracle: One encoding covers all languages, the entire world agrees to use it, and we can mostly forget about encoding conversions—if we use it correctly.

## Resources

- Original article: https://tonsky.me/blog/unicode/
- ICU Project: https://icu.unicode.org/
- Unicode Standard: https://www.unicode.org/versions/latest/
