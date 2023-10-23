from konlpy.tag import Okt


okt = Okt()

text = "재밌는 한글 토크나이징 하는 방법!"
print(okt.morphs(text))
print(okt.morphs(text, stem=True))
print(okt.phrases(text))
print(okt.nouns(text))
print(okt.pos(text))