# DiscardLastN returns generator that reads and produces all values from the g generator discarding the last n items.
def DiscardLastN(g, n):
    for i in g:
        # TODO
        yield i

my_list = [1, 3, 6, 10]

discarded = DiscardLastN(g = (x for x in my_list), n = 2)

for i in discarded:
    print(i)