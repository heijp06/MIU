from miu import produce

string = input("Enter string to produce: ")

for step in produce(string.upper()) or []:
    print(step)
