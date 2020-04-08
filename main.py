from antlr_ast.ast import parse as parse_ast, process_tree
import grammar

import networkx as nx
from networkx import DiGraph


def main():
    with open('sample.pl') as f:
        src = f.read()

    antlr_tree = parse_ast(grammar, src, start="p_text")
    ast = process_tree(antlr_tree)
    call_graph = {}

    def walkTerms(rule, terms):
        if rule is None:
            return

        for chunk in terms:
            if chunk.atom:
                name = str(chunk.atom)
                call_graph[rule].append(name)
            if chunk.term:
                walkTerms(rule, chunk.term)

    for clause in ast.clause:
        if clause.operator and clause.operator.children == [':-']:
            if clause.term and len(clause.term) != 0:
                left = str(clause.term[0].atom)
                call_graph.setdefault(left, [])
                for chunk in clause.term[1:]:
                    if chunk.atom:
                        name = str(chunk.atom)
                        call_graph[left].append(name)
                    if chunk.term:
                        walkTerms(left, chunk.term)

    call_graph = DiGraph(call_graph)
    for cycle in nx.simple_cycles(call_graph):
        if len(cycle) == 1:
            print(f"{', '.join(cycle)} is recursive.")
        else:
            print(f"{', '.join(cycle)} are mutually recursive.")


if __name__ == "__main__":
    main()
