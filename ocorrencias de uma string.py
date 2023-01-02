print("""\nOlá! Seja bem vindo!\n
Esse programa lê uma frase e mostra as seguintes características:
- Quantas vezes aparece a letra 'A'.
- Em que posição ela aparece a primeira vez.
- Em que posição ela aparece a última vez.""")

from time import sleep

sleep(1.0)
frase = str(input("\nDigite uma frase: ")).strip().capitalize()
sleep(0.5)
print(f"\n(Analisando frase...)")
sleep(1.2)

a = frase.lower().count("a")
b = frase.lower().find("a")+1
c = frase.lower().rfind("a")+1

if a == 0:
    print("\nA frase não contém nenhuma letra 'a'.")

else:
    print(f"\n{frase}")
    print(f"\nVezes em que o 'a' aparece na frase: {a}.")
    print(f"Primeira posição na qual o 'a' aparece: {b}.")
    print(f"Última posição na qual o 'a' aparece: {c}.\n")
