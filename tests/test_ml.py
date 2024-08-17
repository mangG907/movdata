from movdata.ml import save_movies

def test_save_movies():
    #for i in range(2015, 2022):
        #r = save_movies(year=i, sleep_time=0.1)
        #assert r
    r = save_movies(year=2017, sleep_time=0.1)
    assert r
