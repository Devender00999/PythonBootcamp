# OOP
from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmender"], "l")
table.add_column("Type", ["Electric", "Water", "Fire"])
table.add_row(["Bulbasour", "Water"])

print(table)
