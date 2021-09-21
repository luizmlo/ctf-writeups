# CTF Writeups - Luiz Mlo
### Este é um repositório criado para mostrar CTF's que já participei, além das minhas soluções e métodos para resolução dos desafios

## CPBSB3 Decred CTF
  #### Este foi um CTF realizado durante a Campus Party de 2019 em Brasília pela equipe de desenvolvimento da criptomoeda Decred (DCR)
  ![Foto da final](https://i.imgur.com/SCWxJXy.png)
  #### Fiquei em 2º lugar no placar final, faltando somente um desafio para resolver, que teve apenas uma resolução
  #### Quase todos os desafios resolvidos tem um Writeup próprio detalhando o desafio e o meu método de solução neste repositório.
  #### Temas abordados nos desafios:
  - Engenharia Reversa
  - Forensics
  - Buffer overflows e Binary Exploitation
  - Web Application Exploitation
  - Crypto

#
## CPBSB3 RNP CTF (Rede Nacional de Ensino e Pesquisa)
  #### Este CTF foi realizado também durante a Campus Party 2019, no estande da RNP.
  ![Foto da final](https://i.imgur.com/BpOR6Kl.png)
  #### Os desafios foram passados no formato de uma máquina virtual de sistema Linux, onde diversas vulnerabilidades poderiam ser aproveitadas para ir resolvendo os desafios, que se não me engano eram 10.
  #### Durante a fase inicial de reconhecimento, eu percebi que a versão do Kernel da máquina alvo era vulnerável a um Exploit muito conhecido e abusado na época, o [DirtyCow (CVE-2016-5195)](https://dirtycow.ninja/).
  #### A vulnerabilidade se aproveita de uma Race Condition durante o mapeamento de memória no momento em que um arquivo é aberto para leitura e possibilita que um usuário sem permissão sobrescreva arquivos que não deveria, abrindo assim possibilidades de escalonamento de privilégios e implantação de backdoors.
  #### Na prática a utilização deste exploit é simples, e para conseguir privilégios elevados logo de cara no início do CTF, eu baixei e compilei um PoC (Proof-of-concept) em que você sobrescrevia o arquivo alvo com uma string, então eu sobrescrevi o arquivo /etc/passwd criando um novo usuário com privilégios de root, que levaram eu e minha equipe ao 1º lugar no CTF.


#
## PicoCTF 2019
  #### Este é um CTF online que inclui desde desafios para iniciantes e de introdução a CTF's até desafios complexos de áreas específicas do conhecimento de segurança
  #### Infelizmente não tenho os writeups individuais de cada desafio, mas encontrei screenshots da plataforma mostrando os desafios que resolvi, divididos por área.

  - General Skills
    - ![](PicoCTF%202019/General%20Skills/Solved.png)

  - Web Exploitation
    - ![](PicoCTF%202019/Web%20Exploitation/Solved.png)

  - Reverse Engineering
    - ![](PicoCTF%202019/Reverse%20Engineering/Solved.png)

  - Binary Exploitation
    - ![](PicoCTF%202019/Binary%20Exploitation/Solved.png)

  - Cryptography
    - ![](PicoCTF%202019/Cryptography/Solved.png)

  - Forensics
    - ![](PicoCTF%202019/Forensics/Solved.png)

## Ringzer0 CTF
  #### Este é um CTF online muito conhecido e que abrange de forma realista uma enorme gama áreas de segurança da informação
  #### Infelizmente eu escrevi um único Writeup na época em que participei deste CTF, detalhando o desafio e um walkthrough completo do script em python que fiz para a resolução do desafio

  [Ringzer0 Writeup](https://github.com/luizmlo/ctf-writeups/blob/master/ringzer0_ctf/Coding%20Challenges/Hash%20me%20please/writeup.md)
