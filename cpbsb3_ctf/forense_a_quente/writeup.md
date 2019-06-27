# CPBSB3-CTF Writeup

### Challenge: Forense a quente 

> Qual o nome do arquivo apagado?
> Formato da Flag: F0RS3NS3{}


- **Passos:**
	- Primeiro, temos que extrair o arquivo zipado:
	```
	$ tar xjf caso_01.dd.bz2
	```
	- E então, eu fui tentando várias palavras chaves no seguinte comando:
	```
	$ dd if=caso_01.dd | strings | grep "palavra_chave"
	```
		- Entre essas palavras, eu tentei
			- flag
			- senha
			- forense
			- quente
			- e apagado
	- Com a palavra ___apagado___, o output foi o seguinte:
	```
	$ dd if=arq.dd | strings | grep "apagado"
	arquivo_odt_apagado.odt
	arquivo_odt_apagado.odt
	arquivo_odt_apagado.odt
	arquivo_odt_apagado.odt
	20480+0 records in
	20480+0 records out
	10485760 bytes (10 MB, 10 MiB) copied, 0,270669 s, 38,7 MB/s

	```


#### Flag: **F0RS3NS3{arquivo_odt_apagado.odt}**
