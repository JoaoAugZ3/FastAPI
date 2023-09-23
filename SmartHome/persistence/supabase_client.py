import os
from supabase import create_client, client

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")

if url is not None and key is not None:
    supabase: client = create_client(url, key)
    data = supabase.table("ambiente").insert({"descricao": "Casa", "icone": "TV", "dispositivos": "..." }).execute()
else:
    print("Certifique-se de definir as variáveis de ambiente SUPABASE_URL e SUPABASE_KEY.")

print("url:", url)
print("key:", key)
