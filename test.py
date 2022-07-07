import spacy, json
from spacy.lang.en import English
from spacy.pipeline import EntityRuler
nlp = spacy.load('en_core_web_sm')
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

ipTest = ""
with open('hindi_keywords.txt', 'r') as f:
    ipTest = f.read().strip('\n')

# ipTest.split('\n')
ipTestList = ipTest.split('\n')
ipTestListTrans = []

with open('wordSetDict.json', 'r') as f:
    data = json.load(f)
    for i in ipTestList:
        # print(type(i.text))
        if i.strip().isdigit():
            ipTestListTrans.append(data[i.strip()])
            continue
        if i.strip() in data:
            ipTestListTrans.append(data[i.strip()])

# print(ipTestListTrans)

doc = nlp(ipTxtTrans)
# for ent in doc.ents:
#     print(ent.text, ent.label_)

patterns = []
for item in ipTestListTrans:
    pattern = {"label": "PERSON", "pattern" : item}
    patterns.append(pattern)
# print(patterns)
nlp = English()
# ruler = EntityRuler(nlp)
ruler = nlp.add_pipe("entity_ruler")
ruler.add_patterns(patterns)
nlp.to_disk("tes_ner")
