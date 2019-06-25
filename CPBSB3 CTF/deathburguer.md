# CPBSB3-CTF Writeup

### Challenge: Deathburguer

>Uma imagem, mil palavras.
>Formato da Flag: F0RS3NS3{}

- **Passos:**
	- Primeiramente, usei o https://futureboy.us/stegano/decinput.html como decodificador na _image-forensiscs.jpg_ para obter a seguinte string: **S0EF3AF3{Fnyir_fhn_fraun_rz_ybpny_frtheb}**

	- Pelo formato da string __S0EF3AF3__, dá pra saber que é uma simples cifra de substituição. De cara eu pensei em ROT13, ou Cifra de César

		- Jogando a string no site https://www.rot13.com/, temos a Flag


#### Flag: **F0RS3NS3{Salve_sua_senha_em_local_seguro}**
