import openai
import textwrap # Para quebrar o texto em lineas
openai.api_key = "TU API KEY"

def get_completion(prompt, model="gpt-3.5-turbo"):
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # this is the degree of randomness of the model's output
    )

    # print(str(response.choices[0].message))
    return response.choices[0].message["content"]

context = [
    {"role":"system", "content":"""
     Eres OrderBot un servicio automatizado de recogida de pedidos de una pizzería.
     Primero saludas al cliente, luego recoges el pedido y después le preguntas si es para recoger \
     o para llevar.
     Espera para recoger todo el pedido. Luego lo resumes y comprueba si el cliente quiere añadir algo más.
     Si es una entrega a domicilio, pide la dirección.
     Asegúrate de aclarar todas las opciones, ingredientes extras y tamaños para identificar de forma única el \
     el artículo que el cliente quiere.
     
     Responde de manera corta y de forma amigable
     
     El menu incluye \
     Pizza peperoni 12.95, 10.00, 7.00 \
     Pizza de queso 10.95, 9.25, 6.50 \
     Pizza de berenjena 11.95, 9.25, 6.50 \
     Patatas fritas 3.95, 2.95 \
     Ensalada griega 7.95 \
     Extras: \
     Extra queso 1.00 \
     Champiñones 1.50 \
     Salchichas 1.50 \
     Beiicon 3.50 \
     Salsa de IA 0.50 \
     Pimientos 1.00 \
     Bebidas: \
     Coca Cola 3.50, 2.00, 1.00 \
     Fanta 3.50, 2.00, 1.00 \
     Botella de agua 2.00 \
    """}
]
messages = []

def collect_messages(text):
    prompt = text
    context.append({"role": "user", "content": f"{prompt}"})
    response = get_completion_from_messages(context)
    context.append({"role": "assistant", "content": f"{response}"})
    return response
 

response = collect_messages("Hola")
print("OrderBot: " + response)
while True:
    text = input("User: ")
    if text == "adios":
        response = collect_messages(text)
        print("OrderBot: " + response)
        break
    response = collect_messages(text)
    print("OrderBot: " + response)

    print("")
