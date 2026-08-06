# Developer Hints

This file contains useful tips for anyone modifying or learning from this project.

## Reveal the Random Number

While testing the game, you may want to see the randomly generated number.

Simply add the following line after generating the random number:

```python
print(f"psst, the correct answer is {answer}")
```

Example:

```python
answer = randint(1, 100)
print(f"psst, the correct answer is {answer}")
```

> This line is intended **only for debugging**. Remove or comment it out before sharing the game with players.
