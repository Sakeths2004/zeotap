from flask import Flask, request, jsonify
from ast_engine import parse_rule, evaluate_ast

app = Flask(__name__)

@app.route('/create_rule', methods=['POST'])
def create_rule():
    rule_str = request.json['rule']
    ast = parse_rule(rule_str)
    # Save AST to the database (not implemented here)
    return jsonify({'message': 'Rule created', 'ast': str(ast)})

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule():
    ast = request.json['ast']
    data = request.json['data']
    result = evaluate_ast(ast, data)
    return jsonify({'result': result})
