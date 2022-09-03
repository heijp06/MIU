from miu import produce

# MIUIUIUI: 0:00:00.578415
# MIUIUIUIUI: Takes forever.
# MUIUIUIUIUIU: Takes forever.

string = input("Enter string to produce: ")

for step in produce(string.upper()) or []:
    print(step)
