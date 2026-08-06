import json


def parse_response(response):

    try:
        # Remove markdown if present
        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

        data = json.loads(response)

        return data

    except json.JSONDecodeError as e:

        print("JSON Error:", e)
        print(response)

        return None