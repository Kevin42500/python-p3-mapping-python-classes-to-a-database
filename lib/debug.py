#!/usr/bin/env python3

from config import CONN, CURSOR
from song import Song


if __name__ == '__main__':
    import ipdb; ipdb.set_trace()

    Song.create_table()
    
    hello = Song("Hello", "25")
    hello.save()

    despacito = Song("Despacito", "Vida")
    despacito.save()

    print("hello.id:", hello.id)
    print("despacito.id:", despacito.id)
