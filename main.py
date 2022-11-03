from igraph import *
import matplotlib.pyplot as plt

def main():
    graph = Graph.Read_Ncol("myGraph.ncol", directed=False)
    graph.es['color'] = None

    colors = ['red', 'green', 'blue', 'black', 'grey', 'yellow', 'purple']
    loop = 1


    while loop:
        group = []
        for edge in graph.es:
            append = 1
            if edge['color'] is None:
                for edge2 in group:
                    if edge2 != edge and edge.source == edge2.source or edge.source == edge2.target or\
                            edge.target == edge2.source or edge.target == edge2.target:
                        append = 0
                if append:
                    group.append(edge)

        for edge in group:
            if len(colors) >= 1:
                edge['color'] = colors[0]
            else:
                print('ERRO: Cores insuficientes')

        if len(colors) >= 1:
            colors.pop(0)
        loop = 0

        for e in graph.es:          # If there is any edge without color, run again
            if e['color'] is None:
                loop = 1

    print('*' * 30, '\n\tEDGES\t\t\tCOLORS')
    print('*' * 30)
    for e in graph.es:
        print(f'\tEdge[{graph.vs[e.source]["name"]}, {graph.vs[e.target]["name"]}]\t\t{e["color"]}')
    print('*' * 30)

    plot(graph, target=plt.axes())
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    main()
