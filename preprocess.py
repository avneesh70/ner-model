import spacy, pandas
from spacy.tokens import DocBin
raw = pandas.read_csv(
    "Training-phrases-generation/detergent_training_phrases_index.csv")
# print(raw.columns)
# print(raw.duplicated().sum())
# print(raw.loc[raw.duplicated(), :])
# print(len(s))
raw.drop_duplicates(subset=None, inplace=True, ignore_index=True)
# print(raw2.count())
# print(raw2.duplicated().sum())
# print(raw2.loc[raw.duplicated(), :])
# t = raw['Size']
# k = t[0].strip('[').strip(']').split(',')
# print(int(k[0]))
# l = raw['Training Phrase'].to_list()
# print(l[:417])
# print(raw['Training Phrase'][417])
trainingData = []
index = 0
label = ["Product", "Quantity", "Size"]
for i in raw['Training Phrase']:
    l = []
    for j in label:
        k = raw[j][index].strip('[').strip(']').split(',')
        l.append((int(k[0]), int(k[1]), j.upper()))
        # print(i, j.upper(), int(k[0]), int(k[1]))
    trainingData.append((i, l))
    index += 1

# for i in trainingData:
#     print(i)

nlp = spacy.blank('en')
db = DocBin()
for text, annotation in trainingData:
    doc = nlp(text)
    ents = []
    for start, end, label in annotation:
        span = doc.char_span(start, end, label=label)
        ents.append(span)
    doc.ents = ents
    db.add(doc)
db.to_disk('training/train.spacy')