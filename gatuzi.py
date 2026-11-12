import os
import requests

def run_automation():
    # Kiungo cha faili lenye orodha ya anwani mtandaoni 
    # (Unaweza kuweka link sahihi ya faili lako hapa kati ya mabano)
    url_ya_orodha = "https://raw.githubusercontent.com/username/repository/main/orodha_ya_anwani.txt"
    
    print("Inachukua faili la anwani kutoka mtandaoni...")
    try:
        response = requests.get(url_ya_orodha)
        if response.status_code == 200:
            # Kusoma anwani na kuzichuja zisiwe na nafasi zilizo wazi
            anwani_zote = [line.strip() for line in response.text.splitlines() if line.strip()]
            print(f"Jumla ya anwani zilizopatikana: {len(anwani_zote)}")
        else:
            print(f"Imeshindikana kupata faili. Status code: {response.status_code}")
            return
    except Exception as e:
        print(f"Hitilafu ya mtandao: {e}")
        return

    # Idadi ya wallet zako na ugawanyaji
    idadi_ya_wallet = 100
    mafaili_kwa_kila_wallet = 5
    ukubwa_wa_faili = 100  # Anwani 100 kila faili

    index = 0
    print("Inaanza kugawanya kwenye folda za wallet...")
    
    for w in range(1, idadi_ya_wallet + 1):
        wallet_folder = f"wallet_{w}"
        os.makedirs(wallet_folder, exist_ok=True)
        
        for f_num in range(1, mafaili_kwa_kila_wallet + 1):
            chunk = anwani_zote[index: index + ukubwa_wa_faili]
            index += ukubwa_wa_faili
            
            if not chunk:
                break
                
            faili_jina = os.path.join(wallet_folder, f"kundi_{f_num}.txt")
            with open(faili_jina, "w", encoding="utf-8") as out:
                out.write("\n".join(chunk))

    print("Kila kitu kimekamilika! Folda na mafaili yote yametengenezwa kwa usahihi.")

if __name__ == "__main__":
    run_automation()
