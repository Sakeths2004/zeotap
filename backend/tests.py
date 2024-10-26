def test_rule_evaluation():
    ast = parse_rule("age > 30 AND salary > 50000")
    data = {"age": 35, "salary": 60000}
    assert evaluate_ast(ast, data) is True
