# bad idea...

The objective of this code is to demonstrate why doing a hash(salt+credit_card) is a bad idea.

The issue here is not sha1, or any hash algorithm. The issue is the shared salt that needs to be used by multiple customers to ensure that there are collisions when doing credit card correlation.

Instruction:
* Step 1: Set your salt in at the head of the code (for now, it is set to "bacon").
* Step 2: Run the build_rainbow.py.
* Step 3: ... be patient, or don't be and spread the load across multiple computers.
* Step 4: Query the rainbow.db for a desired hash

```
$ sqlite3 rainbow.db "SELECT number FROM rainbow WHERE hash = '200a4b388339588ff82ae821500f6347375e93ed'"
4000000000999997
```


On my laptop, it takes 1m04s to generate 1M valid credit card numbers.

Generating all valid card numbers will take some time and the database will take few GB, but it is in the reach of anyone with some means and patience.

How to accelerate the creation of the rainbow table:
* Use GPUs
* Use threads to exploit all cores/cpus
* Spread the load on multiple computers by computing different ranges
* Reduce the number of card generated to targeted issuers by refining the first 4-6 digits.
