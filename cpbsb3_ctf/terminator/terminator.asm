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


ff010000011326394c5f728598abbed1e4f70a1d


ff 01 00 00 01 13 26 39 4c 5f 72 85 98 ab be d1 
0010: e4 f7 0a 1d



a8ec7f28be192280afd98525f879a960ab875247590bb491dffc283e00386b5f