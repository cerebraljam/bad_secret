import hashlib
import sqlite3

### SET THE SALT HERE
salt = b'bacon'


def validator(n):
    validatelist=[]
    for i in n:
        validatelist.append(int(i))

    for i in range(0,len(n),2):
        validatelist[i] = validatelist[i]*2
        if validatelist[i] >= 10:
            validatelist[i] = validatelist[i]//10 + validatelist[i]%10

    if sum(validatelist)%10 == 0:
        return True
    else:
        return False


def main(salt):
    first = 4000000000000000
    last = 4999999999999999
    count = 0
    valid_count = 0
    conn = sqlite3.connect('rainbow.db')
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS rainbow (number INTEGER UNIQUE, hash TEXT, PRIMARY KEY (number))")
    c.execute("CREATE INDEX hash_index ON rainbow (hash);")

    while first + count < last:
        h = hashlib.new('sha1')
        current = first + count
        if validator(str(current)):
            valid_count +=1
            h.update(salt + str(current).encode())
            digest = h.hexdigest()
            c.execute("INSERT INTO rainbow VALUES ((?),(?))", (current, digest))
            if valid_count % 100000 == 0:
                print(current, digest)
                conn.commit()
        count+=1

    conn.commit()
    conn.close()
    print("{} valid cc number generated".format(valid_count))


if __name__ == '__main__':
    main(salt)
