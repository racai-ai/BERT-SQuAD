import json

with open("data/covid-squad-v1.json", "r", encoding="utf-8") as json_file:
    data = json.load(json_file)

for p in data["data"][0]["paragraphs"]:
    for qa in p['qas']:
        qa['id'] = str(qa['id'])


with open("data/train-covid-squad-v1.json", "w", encoding="utf-8") as json_file:
    json.dump(
        {
            "version": "v2.0",
            "data": [
                {
                    "title": "COVID-19",
                    "paragraphs": data["data"][0]["paragraphs"][:-30]
                }
            ]
        },
        json_file,
        ensure_ascii=False
    )

with open("data/dev-covid-squad-v1.json", "w", encoding="utf-8") as json_file:
    json.dump(
        {
            "version": "v2.0",
            "data": [
                {
                    "title": "COVID-19",
                    "paragraphs": data["data"][0]["paragraphs"][-30:-15]
                }
            ]
        },
        json_file,
        ensure_ascii=False
    )

with open("data/test-covid-squad-v1.json", "w", encoding="utf-8") as json_file:
    json.dump(
        {
            "version": "v2.0",
            "data": [
                {
                    "title": "COVID-19",
                    "paragraphs": data["data"][0]["paragraphs"][-15:]
                }
            ]
        },
        json_file,
        ensure_ascii=False
    )