# bad idea...

The objective of this code is to demonstrate why doing a hash(salt+credit_card) is a bad idea.

Instruction:
* Step 1: set your salt in at the head of the code.
* Step 2: Then run the code.
* Step 3: Query the rainbow.db for a desired credit card

> sqlite3 rainbow.db "SELECT 4012012301230123 FROM rainbow"

On my laptop, it takes 1m04s to generate 1M valid credit card numbers.

Generating all valid card numbers will take some time and the database will take few GB, but it is in the reach of anyone with some patience.
