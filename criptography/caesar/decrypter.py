"""
I was given a cyphertext file.
It contains the following content:

picoCTF{ynkooejcpdanqxeykjrbdofgkq}

I'm assumning it uses caesar cypher.
Caesar cypher changes n letters forward.

It means that 'hello' -> 'khoor'
"""

import string

decrypted = ""
encrypted = "ynkooejcpdanqxeykjrbdofgkq"

def decrypt(letter, n):
  global decrypted
  ascii = ord(letter)
  ascii = ascii - 97 # a is 97 in ascii
  ascii = ascii - n  # decrypting...
  ascii = ascii % 26 # wraping (xyz)
  decrypted = decrypted + string.ascii_lowercase[ascii]

print('encrypted: ' + encrypted)

for i in range(25):
  decrypted = ""
  for letter in range(len(encrypted)):
    decrypt(encrypted[letter], i)
  print(str(i) + ' decrypted: ' + decrypted)

"""
this program gave me this output:

encrypted: ynkooejcpdanqxeykjrbdofgkq
0 decrypted: ynkooejcpdanqxeykjrbdofgkq
1 decrypted: xmjnndiboczmpwdxjiqacnefjp
2 decrypted: wlimmchanbylovcwihpzbmdeio
3 decrypted: vkhllbgzmaxknubvhgoyalcdhn
4 decrypted: ujgkkafylzwjmtaugfnxzkbcgm
5 decrypted: tifjjzexkyvilsztfemwyjabfl
6 decrypted: sheiiydwjxuhkrysedlvxizaek
7 decrypted: rgdhhxcviwtgjqxrdckuwhyzdj
8 decrypted: qfcggwbuhvsfipwqcbjtvgxyci
9 decrypted: pebffvatgurehovpbaisufwxbh
10 decrypted: odaeeuzsftqdgnuoazhrtevwag
11 decrypted: nczddtyrespcfmtnzygqsduvzf
12 decrypted: mbyccsxqdrobelsmyxfprctuye
13 decrypted: laxbbrwpcqnadkrlxweoqbstxd
14 decrypted: kzwaaqvobpmzcjqkwvdnparswc
15 decrypted: jyvzzpunaolybipjvucmozqrvb
16 decrypted: ixuyyotmznkxahoiutblnypqua
17 decrypted: hwtxxnslymjwzgnhtsakmxoptz
18 decrypted: gvswwmrkxlivyfmgsrzjlwnosy
19 decrypted: furvvlqjwkhuxelfrqyikvmnrx
20 decrypted: etquukpivjgtwdkeqpxhjulmqw
21 decrypted: dspttjohuifsvcjdpowgitklpv
22 decrypted: crossingtherubiconvfhsjkou
23 decrypted: bqnrrhmfsgdqtahbnmuegrijnt
24 decrypted: apmqqglerfcpszgamltdfqhims

when the key is 22 - the message kind of makes sense...
the flag is picoCTF{crossingtherubiconvfhsjkou}
"""
