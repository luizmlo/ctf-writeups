# CPBSB3-CTF Writeup

### Challenge: Adeus cartorios, ola timestamp

> Alguem registra esse meme porque é mt bom.
> Hint: A Decred tem um servico web de prova de existencia com ancoragem na blockchain.
> Encontre o digest do meme.

- **Passos:**
	- Esse challenge foi meio na sorte, eu pesquisei o mecanismo de hashing da Decred, que é __BLAKE-256__, mas não achei nenhuma implementação online

	- No aleatório, eu peguei o arquivo __memectf.pdf__ e joguei em algoritmo de [Sha-256](https://emn178.github.io/online-tools/sha256_checksum.html)
		- __Digest__, é o nome dado à saída de um algoritmo de hash, nesse caso, o Digest do arquivo foi:
		- ``` 6a942a32dc2ab64da3a515f542ab7fb333172d2fe099c74a0c8b125f92ac91a7 ```
		- Eu coloquei o digest no campo de submit e foi, mesmo não seguindo o padrão das Flags (?)


#### Flag: **6a942a32dc2ab64da3a515f542ab7fb333172d2fe099c74a0c8b125f92ac91a7**
