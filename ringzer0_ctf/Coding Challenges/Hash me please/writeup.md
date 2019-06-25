# Hash me if you can!

### The challenge itself:

![Challenge](https://image.prntscr.com/image/Q7cuZfsdRtaGbR4Jx8rbAw.png)

## Main goals for the challenge:
1. Retrieve the challenge html source code using **requests.py**
2. Remember the session cookies, without them we won't get the challenge but a login prompt instead
3. Extract only the hash key from the source using **bs4.py**
4. Hash it using the sha512 algorithm from the **hashlib.py** library
5. Access the [...]/hashed_key url and retrieve the source
6. Extract only the Flag from it, again, using **bs4.py**
7. rekt

## The algorithm divided in 3 parts:

### 1.
> At this first function, we're already on the 3rd step on our goals.
![](https://image.prntscr.com/image/hGOGZC2HTa6ULWp5xVjoWA.png)
This __parse_key__ function does the following:
> * Retrieves the html file using the correct session cookies
> * Parses the challenge "password" and returns it

### 2.
> This second function takes the __parse_key__ output and hashes it using the sha512 algorithm
![](https://image.prntscr.com/image/QrPQt62TQgm4jdN7mr569w.png)

### 3.
> This last part takes the hashed key, retrieves the flag page html, parses it and returns only the flag.
![](https://image.prntscr.com/image/HW0DwIm6QpO59Ft0Qg1_tg.png)

## Done!
### At this point, you should have the flag on your terminal and it should also be copied to your clipboard. Lit!
