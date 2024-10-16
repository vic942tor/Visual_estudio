#se lanzan dos dados, idicar todos ls posible valores distintos y representarlos de la siguiente manera, teniendo en cuenta que la laida debe verse así (x , y) siendo x e y el número según la cara del dado

# for dado1 in range(1, 7):
#     for dado2 in range(1, dado1 +1):
#         print(f"({dado1}, {dado2})", end = " ")
#     print() #saltar de línea para cada fila
print("\n".join(" ".join(f"({dado1}, {dado2})" for dado2 in range(1, dado1 + 1)) for dado1 in range(1, 7)))





