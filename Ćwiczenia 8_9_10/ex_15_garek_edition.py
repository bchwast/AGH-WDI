def main():
    szach = [None]*8
    wiersz = [False]*8
    przek1 = [False]*15
    przek2 = [False]*15

    def hetman(w=0, k=0):
        if k == 8:
            print(szach)
            exit(0)

        if wiersz[w] or przek1[w + k] or przek2[7 + w - k]:
            return

        wiersz[w] = przek1[w + k] = przek2[7 + w - k] = True
        szach[k] = w

        for i in range(8):
            hetman(i, k+1)

        wiersz[w] = przek1[w + k] = przek2[7 + w - k] = False
    #end def


    hetman()
#end def


main()