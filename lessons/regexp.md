# Regular expressions

[Offical re module documentation](https://docs.python.org/3/library/re.html)
[Official regexp HOWTO documentation](https://docs.python.org/3/howto/regex.html)
[Oficcial greedy non greedy documentation](https://docs.python.org/3/howto/regex.html#greedy-versus-non-greedy)

A regular expression (regex or regexp) is a search query for text that's expressed by string pattern.

Import the re module to use regular expressions.

## .findall()

Examples:

```python
import re

print(re.findall(r"[a|A]", "This is an example"))
```

## .search()

Examples:

```python
# Without regexp
string = "This is a string example with [brackets]"
index = string.index("[")
print(string[index+1:index+9])

# With regexp module "re" and .search() function
import re
string = "This is a string example with [brackets]"
regex = r"\[(\w+)\]"
result = re.search(regex,string)
print(result[1])

# More examples
result = re.search(r"example", "This is an example")
result = re.search(r"xam", "This is an example")
result = re.search(r"is", "This is an example")
result = re.search(r"^e", "This is an example")
```

## grep

Is possible to do regexp on Linux terminal using the `grep` command.

grep string_to_find file_path

Examples:

```bash
grep string /usr/share/dict/words
```

Using the `-i` parameter will match a string regardless of case.

Examples:

```bash
grep -i string /usr/share/dict/words
```

## Reserved or special characters

- Dot character (`.`): Matches any character.

Examples:

```bash
grep st.ing /usr/share/dict/words
```

- Caret character or circumflex (`^`): Indicates the beginning of the line pattern.

Examples:

```bash
grep ^string /usr/share/dict/words
```

- Dollar sign (`$`): Indicates the end of the line pattern.

Examples:

```bash
grep string$ /usr/share/dict/words
```

## re.IGNORECASE

Case insesitive match.

Examples

```python
import re

print(re.search(r"s.ring", "String", re.IGNORECASE))
```

## Wildcard

Symbols or expressions to represent or replace on or more characters. i.e. the dot character (`.`)

### Brackets

Examples:

```python
import re

print(re.search(r"[Ee]xample", "This is an example"))
```

Use `[a-z]` to find any lowercase letter:

Examples:

```python
import re

print(re.search(r"[a-z]xample", "This is an example"))
```

Use `[0-9]` to find any number:

Examples:

```python
import re

print(re.search(r"[0-9]", "This is an example, the number 1"))
```

Is possible to combine different patterns:

Examples:

```python
import re

print(re.search(r"[a-zA-Z0-9]xample", "This is an example"))
```

Use `[^]` to match any characters that aren't in a group.

Examples:

```python
import re

print(re.search(r"[^a-zA-Z]xample", "This is an example"))
```

### Pipe

Use `|` to match either expression, the first one or the second one.

Examples:

```python
import re

print(re.search(r"[e|E]xample", "This is an example"))
```

## Repetition Qualifiers

Examples:

```python
import re

print(re.search(r"e.*e", "This is an example"))
print(re.search(r"e[a-z]*e", "This is an example"))
```

The `+` matches one or more occurences of the character that comes before it.

Examples:

```python
import re

print(re.search(r"e+x+", "This is an example"))
```

The `?` matches either 0 or one occurence of the character before it.

Examples:

```python
import re

print(re.search(r"e?ample", "This is an example"))
```

## Escaping characters

Using `\` character to escape.

Examples:

```python
import re

print(re.search(r"\.hi", "This is an example"))
```

Using `\w` matches any alphanumeric character including letters, numbers and underscores.

Examples:

```python
import re

print(re.search(r"\w*", "This is an example"))
print(re.search(r"\w*", "This_is_an_example"))
```

Use `\d` for match digits.

Use `\s` for match whitespace characters like whitespace, tabs or new lines.

Use `\b` for word boundaries and few others.
