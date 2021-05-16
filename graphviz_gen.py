# This Python file uses the following encoding: utf-8


from graphviz import Digraph
import ip_extract


def gengraph(hostname_g):
    l_ip_valid_a = ip_extract.extract_ip()
    g_v = Digraph("ip_graph", format='svg')
    for i in range(1, len(l_ip_valid_a) - 1):
        g_v.edge(l_ip_valid_a[i], l_ip_valid_a[i + 1])
    g_v.render(filename="final_graph" + str(hostname_g), format='svg')


if __name__ == "__main__":
    gengraph("google")
