import json
from openai import OpenAI
from memory_manager import MemoryManager
from functions import calcular_idade, converter_temperatura

client = OpenAI()

memory = MemoryManager()

system_message = {
    "role": "system",
    "content": "Você é um assistente educado, claro e objetivo. Responda de forma amigável e útil."
}

memory.add_message(system_message["role"], system_message["content"])

print("Assistente iniciado. Digite /limpar para apagar memória ou /sair para encerrar.\n")

while True:

    user_input = input("Você: ")

    if user_input == "/sair":
        break

    if user_input == "/limpar":
        memory.clear()
        memory.add_message(system_message["role"], system_message["content"])
        print("Assistente: Memória da conversa apagada.")
        continue

    if "idade" in user_input.lower():
        try:
            ano = int(input("Digite seu ano de nascimento: "))
            resultado = calcular_idade(ano)
            print(f"Assistente: Sua idade aproximada é {resultado} anos.")
            continue
        except:
            pass

    if "temperatura" in user_input.lower():
        try:
            valor = float(input("Digite o valor da temperatura: "))
            origem = input("Converter de (C/F): ").upper()
            resultado = converter_temperatura(valor, origem)
            print(f"Assistente: Temperatura convertida: {resultado}")
            continue
        except:
            pass

    memory.add_message("user", user_input)

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=memory.get_messages()
    )

    reply = response.choices[0].message.content

    print(f"Assistente: {reply}")

    memory.add_message("assistant", reply)

    memory.save()