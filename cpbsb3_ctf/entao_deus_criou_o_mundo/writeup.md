# CPBSB3-CTF Writeup

### Challenge: Entao Deus criou o Mundo

> No princípio criou Deus o céu e a terra.
> E a terra era sem forma e vazia; e havia trevas sobre a face do abismo;
> E o espírito de Deus se movia sobre a face das águas.
> E disse Deus: Haja luz; e houve luz. E viu Deus que era boa a luz; e fez Deus separação entre a luz e as trevas.

> O hash do segredo é a flag!

>Hint: Decred.org

- **Passos:**
	- Pesquisando esse versículo, descobri que faz parte de __Genesis 1__
	- O primeiro bloco de toda blockchain, é chamado de **Bloco Genesis**, e é isso que eu encontrei:
		- Pesquisando __Decred Genesis Block__, encontrei que a data do 1° bloco da chain da Decred foi dia **08/02/2016**;
		
	- Entrando na [Lista de blocos](https://mainnet.decred.org/blocks) e alterando a data para **08/02/2016**, dá pra ver o primeiro bloco da chain;
		- No link do [Bloco Genesis, ou Bloco #0](https://mainnet.decred.org/block/298e5cc3d985bfe7f81dc135f360abe089edd4396b86d2de66b0cef42b21d980), este é o hash do bloco, e também a flag:
		```
		 298e5cc3d985bfe7f81dc135f360abe089edd4396b86d2de66b0cef42b21d980
		```

#### Flag: ** 298e5cc3d985bfe7f81dc135f360abe089edd4396b86d2de66b0cef42b21d980**
