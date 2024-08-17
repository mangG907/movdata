import requests
import os
import time
import json
from tqdm import tqdm

API_KEY = os.getenv('MOVIE_API_KEY')

# url 불러오기
def gen_url(moviecode='20158561'):
    url_base = f"http://www.kobis.or.kr/kobisopenapi/webservice/rest/movie/searchMovieInfo.json?key={API_KEY}&movieCd={moviecode}"
    return url_base
    
# 상세정보 불러오기
def req(moviecode='20158561'):
    url = gen_url(moviecode)
    r = requests.get(url)
    j = r.json()
    return j

def save_json(data, file_path):
    # 파일저장 경로 MKDIR
    os.makedirs(os.path.dirname(file_path), exist_ok=True)
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

def read_data(year=2015, sleep_time=1):
    read_file = f'data/movies/year={year}/data.json'
    file_path = f'data/movies/movieinfo/year={year}/data.json'
    if os.path.isfile(file_path):
        print(f'데이터가 이미 존재합니다: {file_path}')
        return True
    with open(read_file, 'r') as f:
        data = json.load(f)
    all_data = []

    for p in tqdm(data):
        time.sleep(sleep_time)
        moviecd = p['movieCd']
        data = req(moviecd)
        ap_dt = data['movieInfoResult']['movieInfo']
        all_data.append(ap_dt)

    save_json(all_data, file_path)
    return True
