import re
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")

def evaluate_expression(expression):
    """
    Evalúa una expresión matemática.
    """
    if not re.match(r"^[0-9+\-*/().\s]+$", expression):
        raise ValueError("La expresión contiene caracteres no permitidos.")
    return eval(expression)

def draw_syntax_tree(expression):
    """
    Genera un árbol sintáctico de la expresión y lo guarda como imagen.
    """
    G = nx.DiGraph()

    def add_nodes(sub_expr, parent_name):
        if sub_expr.isdigit():
            G.add_node(sub_expr)
            G.add_edge(parent_name, sub_expr)
        elif sub_expr.startswith("(") and sub_expr.endswith(")"):
            add_nodes(sub_expr[1:-1], parent_name)
        else:
            for op in ["+", "-", "*", "/"]:
                if op in sub_expr:
                    left, right = sub_expr.rsplit(op, 1)
                    op_node = f"{parent_name}_{op}"
                    G.add_node(op_node)
                    G.add_edge(parent_name, op_node)
                    add_nodes(left.strip(), op_node)
                    add_nodes(right.strip(), op_node)
                    return

    root = "E"
    G.add_node(root)
    add_nodes(expression, root)

    plt.figure(figsize=(12, 8))
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, arrows=True, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold")
    file_name = "static/syntax_tree.png"
    plt.savefig(file_name)
    plt.close()
    return file_name
