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