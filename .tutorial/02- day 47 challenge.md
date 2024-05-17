# 👉 Day 47 Challenge

Alright Top Trumpers. Your program should work like this.

1. Pick a category. Something popular. You know like 'most handsome computer science teachers'. 😆
2. Store the information of **two** different objects in a 2D dictionary.
3. The key field should be **name**.
4. The data in the sub dictionary should be some stats about the object. For example:
   1. Intelligence
   2. Handsomeness
   3. L33t c0ding skillz
   4. Baldness level
   
5. Use an infinite loop to get the user to pick one of the two cards, then pick a stat from that card.
6. Display the chosen stat for both cards and output which has won.

🥳 Extra points for:
- Making the dictionary dynamic so you can add your own cards.
- Using a loop to play the game in a 2 player format, keeping track of points scored.

Example:

```
🌟Top Trumps🌟

Welcome to the Top Trumps 'Most Handsome Computing Teachers' Simulator

Choose your card: 1 - Mr. Morgan  2 - Mr.Colley 

> 1

Choose your stat:
1. Intelligence
2. Handsomeness
3. L33t c0ding skillz
4. Baldness level

> 4

Mr. Morgan has a baldness stat of 99
Mr. Colley has a baldness stat of -68

************* Mr Morgan wins! ********

Again? y/n > n
```

<details> <summary> 💡 Hints </summary>
  
- If you're adding your own cards dynamically, try using the `random.choice()` function  to 'draw' two cards from the deck.
</details>