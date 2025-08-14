# 🏆 Secret Auction Program  
**My 9th Project of the Python Bootcamp 🎓🐍**  

This project is a **Secret Auction Program** where multiple bidders can place their bids without knowing each other's offers 💰.  
At the end, the program determines **who placed the highest bid** and declares them the winner 🥇.

---

## 📜 How It Works

### 1️⃣ Program Start
- The program **imports a logo** 🎨 from the `art` module and displays it at the start.  
- Prints a **welcome message** for the auction participants.

```python
from art import logo
print(logo)
```
---
## 2️⃣ Function to Find Winner

The `find_highest_bidder()` function loops through all bids in the `bidders` dictionary.

It keeps track of:

- **Highest bid amount** 💵
- **Winner's name** 🏅

Once the loop ends, it **prints the winner and their bid**.

```python
def find_highest_bidder(bidding_record):
    highest_bid = 0
    winner = ""
    for bidder, bid_amount in bidding_record.items():
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The winner is {winner} with the bid of ${highest_bid}")
```
## 3️⃣ Collecting Bids

An empty dictionary `bidders` stores data in this format:

```python
{"Name": Bid}
```
### The program runs a loop (while auction_ongoing:) asking each participant:

- `Their name` 🧑

- `Their bid` 💲

It then adds the information into the bidders dictionary.

--- 
## 4️⃣ Asking for More Bidders

After each bid, the program asks:

- If `"yes"` → clears the screen (by printing blank lines) so the next bidder can't see previous bids 🕵️‍♂️.
- If `"no"` → ends the auction and calls `find_highest_bidder()` to announce the winner 🎉.

--- 
## 🖥 Example Run

``` python 
🏆 Welcome to the Secret Auction Program! 🏆
What is your name?: Alice
What's your bid?: $ 150
Are there any more bidders? Type 'yes' or 'no': yes

(20 lines cleared)

What is your name?: Bob
What's your bid?: $ 200
Are there any more bidders? Type 'yes' or 'no': no

The winner is Bob with the bid of $200

```
---
## 🧠 What I Learned

- Working with **dictionaries** in Python 📖.
- Using **loops** to handle multiple inputs 🔁.
- Creating and calling **functions** to process data 🛠.
- Clearing the console (in a simple way) to hide information during execution 🔒.
