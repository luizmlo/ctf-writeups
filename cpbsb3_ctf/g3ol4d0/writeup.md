# CPBSB3-CTF Writeup

### Challenge: g3ol4d0.html

> Se vira filhão.
> (?)

- **Passos:**
	- Olhando no código, dá pra ver que é um código obfuscado com as mágicas de javascript.

	- Eu cheguei a procurar um prettier que voltasse pra código legível, mas não achei.

	- A solução foi fazer um hook no __eval()__, adicionando o seguinte snippet antes do programa obfuscado executar:
	```
	window.eval = valor => console.log(valor);
	```

	- No console, o output foi o seguinte:
	```javascript
	var flag = prompt("flag:") ;

	if (flag == "muitobemvce%6undefinedte%6undefineddedejavascript") {
	alert("Boa!")

	} else {
	alert("%4undefinedope :(")
	}
	```
		- Tirando os __%6undefined, temos a flag.
	
#### Flag: **muitobemvcentendedejavascript**
