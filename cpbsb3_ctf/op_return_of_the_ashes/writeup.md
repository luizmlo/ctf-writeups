# CPBSB3-CTF Writeup

### Challenge: OP_RETURN OF THE ASHES

> I want to burn bitcoins, fuck the system, the banks are invincible, cryptography? decentralized system? Fuck your mind, your gray matter is a shit!

- **Passos:**
	- **burn.txt**
		```
		"minus[minus]>[minus]plusplusplusplusplusplusplusplusplusplus[<plusplusplusplusplusplusplusplusplusplus>minus]<plusplusplusplusplusplusplusplusplusplus.
		>plusplusplusplusplusplusplusplus[<minusminusminusminusminusminusminusminus>minus]<plusplusplusplusplusplus.
		>plusplusplusplusplus[<plusplusplusplusplus>minus]<minus.
		>plusplusplusplusplus[<minusminusminusminusminus>minus]<minusminus.
		>plusplusplusplusplusplusplus[<plusplusplusplusplusplusplus>minus]<plusplus."
		[...]
		```

	- Com um simples código em python, transformamos o arquivo em um código em BrainFuck
	```python
	palavra = palavra.replace('plus', '+')
	palavra = palavra.replace('minus', '-')

	print(palavra)
	```
	- Depois, usando um [Interpretador de Brainfuck](https://www.dcode.fr/brainfuck-language), temos como output do programa a string:
	``` n4L1dDuXVoVowuqzXYU3bM7gze3kPSubtr ```

	- Essa string é uma wallet de bitcoin, e pelo [Bitcoin Cash Explorer](http://testnet.imaginary.cash/block/000000006e0d32ba8de73207795d211dbd825afa57e97d2c0662068acc99664b) conseguimos acessar as transações dessa wallet
		- Entre essas transações, uma tem a seguinte string:
			``` CTF-BR{p450u_p3r70_c0n71nu3_73n74nd0} ```

		- Com essa dica, vendo as transações dessa wallet, está a flag em uma OP_RETURN mais antiga.

#### Flag: **CTF-BR{wh3r3 4r3 my b17c01n5?}**
