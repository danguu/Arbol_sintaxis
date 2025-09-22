from tree import tokenize, Parser, draw_tree


archivo = input("Dame el archivo: ")

try:
    with open(archivo, "r", encoding="utf-8") as f:
        expr = f.read().strip()
    print("Expresión leída:", expr)

    tokens = tokenize(expr)
    parser = Parser(tokens)

    root, graph = parser.parse()
    print("Cadena aceptada")
    draw_tree(graph, root)

except FileNotFoundError:
    print(f"Error: no se encontró el archivo {archivo}")
except Exception as e:
    print("Error:", e)
