# Operators

## Arithmetic operators

| Operator | Description          | Example           | Result  |
|----------|----------------------|-------------------|---------|
| `+`      | Addition             | `5 + 3`           | `8`     |
| `-`      | Subtraction          | `7 - 4`           | `3`     |
| `*`      | Multiplication       | `2 * 6`           | `12`    |
| `/`      | Division             | `10 / 2`          | `5.0`   |
| `//`     | Floor Division       | `10 // 3`         | `3`     |
| `%`      | Modulus (Remainder)  | `15 % 7`          | `1`     |
| `**`     | Exponentiation       | `2 ** 3`          | `8`     |

---

## Assignment operators

| Operator   | Description                   | Example          | Equivalent to          |
|------------|-------------------------------|------------------|------------------------|
| `=`        | Assignment                    | `x = 5`          | -                      |
| `+=`       | Addition Assignment           | `x += 3`         | `x = x + 3`            |
| `-=`       | Subtraction Assignment        | `x -= 2`         | `x = x - 2`            |
| `*=`       | Multiplication Assignment     | `y *= 4`         | `y = y * 4`            |
| `/=`       | Division Assignment           | `z /= 2`         | `z = z / 2`            |
| `//=`      | Floor Division Assignment     | `a //= 3`        | `a = a // 3`           |
| `%=`       | Modulus Assignment            | `b %= 7`         | `b = b % 7`            |
| `**=`      | Exponentiation Assignment     | `c **= 2`        | `c = c ** 2`           |
| `&=`       | Bitwise AND Assignment        | `num &= 3`       | `num = num & 3`        |
| `|=`       | Bitwise OR Assignment         | `mask |= 8`      | `mask = mask | 8`      |
| `^=`       | Bitwise XOR Assignment        | `flag ^= 1`      | `flag = flag ^ 1`      |
| `<<=`      | Left Shift Assignment         | `shift <<= 2`    | `shift = shift << 2`   |
| `>>=`      | Right Shift Assignment        | `shift >>= 1`    | `shift = shift >> 1`   |

---

## Comparison Operators



| Operator   | Description                     | Example         | Result  |
|------------|---------------------------------|-----------------|---------|
| `==`       | Equal to                        | `5 == 5`        | `True`  |
| `!=`       | Not equal to                    | `5 != 3`        | `True`  |
| `<`        | Less than                       | `7 < 10`        | `True`  |
| `>`        | Greater than                    | `7 > 5`         | `True`  |
| `<=`       | Less than or equal to           | `4 <= 4`        | `True`  |
| `>=`       | Greater than or equal to        | `6 >= 5`        | `True`  |


---

## Logical Operators

| Operator   | Description                     | Example           | Result  |
|------------|---------------------------------|-------------------|---------|
| `and`      | Logical AND                     | `True and False`  | `False` |
| `or`       | Logical OR                      | `True or False`   | `True`  |
| `not`      | Logical NOT                     | `not True`        | `False` |


---

## Identity Operators

| Operator   | Description                     | Example             | Result  |
|------------|---------------------------------|---------------------|---------|
| `is`       | True if the operands are         | `x is y`           | `True`  |
|            | identical objects               |                     |         |
| `is not`   | True if the operands are not     | `x is not y`       | `True`  |
|            | identical objects               |                     |         |


---

## Membership Operators

| Operator   | Description                           | Example               | Result  |
|------------|---------------------------------------|-----------------------|---------|
| `in`       | True if value/variable is found        | `5 in [1, 2, 3, 4, 5]` | `True`  |
|            | in the sequence                        |                       |         |
| `not in`   | True if value/variable is not found    | `7 not in [1, 2, 3, 4]`| `True`  |
|            | in the sequence                        |                       |         |


---

## Bitwise Operators

| Operator   | Description                           | Example               | Result  |
|------------|---------------------------------------|-----------------------|---------|
| `&`        | Bitwise AND                           | `5 & 3`               | `1`     |
| `|`        | Bitwise OR                            | `5 | 3`               | `7`     |
| `^`        | Bitwise XOR                           | `5 ^ 3`               | `6`     |
| `~`        | Bitwise NOT (complement)              | `~5`                  | `-6`    |
| `<<`       | Left shift                            | `5 << 2`              | `20`    |
| `>>`       | Right shift                           | `5 >> 1`              | `2`     |


