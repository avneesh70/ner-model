import spacy, json, pandas
from spacy.lang.en import English
from spacy.pipeline import EntityRuler
from spacy.tokens import DocBin


nlp = spacy.load('training/model-best')
ipTxt = ""
with open('extract_transcription_json/6412548b294e8ad5/contenturl_0.json', 'r')  as f:
    data = json.load(f)
    for i in range(len(data['recognizedPhrases'])):
        ipTxt += data['recognizedPhrases'][i]['nBest'][0]['itn'] + ' '
# print(ipTxt)
ipTxtTrans = ""
l = ipTxt.split(' ')
with open('wordSetDict.json', 'r') as f:
    data = json.load(f)
    for i in l:
        # print(type(i.text))
        if i.isdigit():
            ipTxtTrans += i + " "
            continue
        if i in data:
            ipTxtTrans += data[i] + " "


"""write trigger words in hinglish"""
# ipTest = ""

# with open('hindi_keywords.txt', 'r') as f:
#     ipTest = f.read().strip('\n')

# # ipTest.split('\n')
# ipTestList = ipTest.split('\n')
# ipTestListTrans = []

# with open('wordSetDict.json', 'r') as f:
#     data = json.load(f)
#     for i in ipTestList:
#         # print(type(i.text))
#         if i.strip().isdigit():
#             ipTestListTrans.append(data[i.strip()] + '\n')
#             continue
#         if i.strip() in data:
#             ipTestListTrans.append(data[i.strip()] + '\n')

# print(ipTestListTrans)
# with open("inputWords.txt", 'w') as f:
#     f.writelines(ipTestListTrans)

doc = nlp(ipTxtTrans)
testData = []
# for token in doc:
#     print(token.text, token.pos_, token.dep_, token.has_vector)
for ent in doc.ents:
    print(ent.text, ent.label_, ent.start_char, ent.end_char)

# results = createTraining(doc)

"""take hinglish data into list"""
# patterns = []
# for item in ipTestListTrans:
#     pattern = {"label": "PERSON", "pattern" : item}
#     patterns.append(pattern)
# print(patterns)
