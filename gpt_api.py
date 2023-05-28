import requests

def generate_email_recommendations(email_name, email_content):
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer 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"
    }
    payload = {
        "model": "gpt-3.5-turbo",
        "messages": [
            {
                "role": "assistant",
                "content": f"Hjælp os med at skrive en god email baseret på følgende information:\n\nEmail Name: {email_name}\n\nEmail Content: {email_content}\n\Kom med forslag til følgende. 1) et emne 2) en preadheader and 3) en tekst of maximum 500 charachters. Forretningen er Philipson Wine er en dansk vinforhandler, der specialiserer sig i salg af vin fra forskellige dele af verden. De tilbyder et bredt udvalg af vine, herunder rødvin, hvidvin, rosévin, mousserende vin og dessertvin. Philipson Wine importerer vin fra mange forskellige vinproducenter og regioner og har et sortiment, der spænder fra kendte vine til mere eksklusive og sjældne vine. Det hele på dansk vær sød at levere dataen med emne på linje 1 preheader på linje 2 og hovedteksten på linje 3"
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        recommendations = data["choices"][0]["message"]["content"]
        print(data)
        # Split emne, preheader, and tekst
        lines = recommendations.split("\n")
        emne = lines[0].replace("Emne: ", "").strip()
        preheader = lines[1].replace("Preadheader: ", "").strip()
        tekst = lines[2].replace("Tekst: ", "").strip()
        
        return emne, preheader, tekst
    else:
        print("API request failed with status code:", response.status_code)
        print("Response:", response.text)
        return None, None, None
