from structured import extract_contact


golden = [
    {
        "text": "Dana from Acme, dana@acme.co",
        "expect": {
            "name": "Dana",
            "email": "dana@acme.co",
            "company": "Acme"
        }
    },
    {
        "text": "Mike works at Globex, mike@globex.com",
        "expect": {
            "name": "Mike",
            "email": "mike@globex.com",
            "company": "Globex"
        }
    },
    {
        "text": "Sarah - BetaCorp - sarah@beta.com",
        "expect": {
            "name": "Sarah",
            "email": "sarah@beta.com",
            "company": "BetaCorp"
        }
    },
    {
        "text": "John from Acme Labs, john@acme.io",
        "expect": {
            "name": "John",
            "email": "john@acme.io",
            "company": "Acme Labs"
        }
    },
    {
        "text": "Lisa at Foo Inc, lisa@foo.com",
        "expect": {
            "name": "Lisa",
            "email": "lisa@foo.com",
            "company": "Foo Inc"
        }
    }
]

def score(extract_fn):
    hits = 0

    for case in golden:
        out = extract_fn(case["text"]).model_dump()

        if all(out.get(k) == v for k, v in case["expect"].items()):
            hits += 1

    return hits / len(golden)


print("accuracy:", score(extract_contact)*100)