# CPBSB3-CTF Writeup

### Challenge: Terminator

>Que assembly é esse?
>A flag estará na memória ao fim da execução, do endereço $0000 ao $0013.

- **Passos:**
	- Primeiramente, temos que descobrir de qual arquitetura é esse assembly:
	```asm
	  lda #$ff
	  sta $00
	  lda #$01
	  sta $01
	  ldx #$01
	  ldy #$0a
	loop:
	  inx
	  sta $02, x
	  adc #$12
	  cpy $12
	  bne loop
	  sta $13
	  brk
	```
	- Pesquisando as instruções individualmente, pelo visto é de uma arquitetura chamada **MOS 6502**
		- Agora sabendo a arquitetura, é só encontrar uma maneira de compilar e rodar as instruções
	- Depois de procurar um compilador que preste, encontrei esse [Easy 6502 by Skilldrick](https://skilldrick.github.io/easy6502/)
		- Jogando o código nesse compiler e removendo a instrução __brk__, temos o seguinte dump:
			- ``` ff 01 00 00 01 13 26 39 4c 5f 72 85 98 ab be d1 e4 f7 0a 1d ```

	- Para remover os espaços, um simples código em python serve:
		```python
		key = "ff 01 00 00 01 13 26 39 4c 5f 72 85 98 ab be d1 e4 f7 0a 1d"
		flag = key.replace(' ', '')
		print(flag)
		```


#### Flag: **ff010000011326394c5f728598abbed1e4f70a1d**
