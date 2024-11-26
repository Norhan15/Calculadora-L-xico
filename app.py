from flask import Flask, request, render_template
from lexer import analyze_expression, count_tokens
from expression_parser import evaluate_expression, draw_syntax_tree
from memory import ms_store, ms_recall


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    expression = ""
    tree_path = None
    tokens = []
    token_counts = {}
    memory_value = ms_recall()

    if request.method == "POST":
        expression = request.form.get("expression")
        try:
            tokens = analyze_expression(expression)
            token_counts = count_tokens(tokens)
            result = evaluate_expression(expression)
            tree_path = draw_syntax_tree(expression)

            # Si se presiona "MS", guardar el resultado en memoria
            if "ms_store" in request.form:
                ms_store(result)

        except Exception as e:
            result = f"Error: {e}"

    return render_template(
        "index.html",
        expression=expression,
        result=result,
        tree_path=tree_path,
        tokens=tokens,
        token_counts=token_counts,
        memory_value=memory_value,
    )

if __name__ == "__main__":
    app.run(debug=True)