#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
영화 추천 챗봇
고객에게 객관식 질문을 통해 영화를 추천해주는 터미널 기반 챗봇
"""

# 영화 데이터베이스
MOVIES = {
    "액션": {
        "미국": ["다이 하드", "매트릭스", "터미네이터", "존 윅", "인셉션"],
        "한국": ["베테랑", "극한직업", "신과함께", "도둑들", "암살"],
        "SF": ["매트릭스", "인셉션", "인터스텔라", "블레이드 러너", "그래비티"]
    },
    "코미디": {
        "미국": ["더 행오버", "슈퍼배드", "보랏", "에이스 벤츄라", "미트 더 페어런츠"],
        "한국": ["극한직업", "극한직업", "신과함께", "명량", "미션 임파서블"],
        "로맨틱": ["러브 액츄얼리", "사랑과 영혼", "노트북", "라라랜드", "브리짓 존스의 일기"]
    },
    "드라마": {
        "미국": ["포레스트 검프", "쇼생크 탈출", "다크 나이트", "인터스텔라", "그린 마일"],
        "한국": ["기생충", "올드보이", "신과함께", "극한직업", "도둑들"],
        "감동": ["포레스트 검프", "쇼생크 탈출", "그린 마일", "레옹", "이터널 선샤인"]
    },
    "공포": {
        "미국": ["그것", "컨저링", "엑소시스트", "링", "싸이코"],
        "한국": ["곡성", "콜", "곡성", "검은 사제들", "화차"],
        "스릴러": ["셔터 아일랜드", "세븐", "메멘토", "올드보이", "기생충"]
    },
    "로맨스": {
        "미국": ["타이타닉", "노트북", "사랑과 영혼", "라라랜드", "500일의 썸머"],
        "한국": ["건축학개론", "늑대와 춤을", "도둑들", "명량", "베테랑"],
        "코미디": ["러브 액츄얼리", "브리짓 존스의 일기", "500일의 썸머", "미트 더 페어런츠", "더 행오버"]
    },
    "SF": {
        "미국": ["매트릭스", "인터스텔라", "인셉션", "블레이드 러너", "어벤져스"],
        "한국": ["기생충", "올드보이", "곡성", "신과함께", "명량"],
        "액션": ["매트릭스", "인셉션", "터미네이터", "아이언맨", "어벤져스"]
    }
}


def print_welcome():
    """환영 메시지 출력"""
    print("\n" + "="*50)
    print("🎬 영화 추천 챗봇에 오신 것을 환영합니다! 🎬")
    print("="*50)
    print("여러분의 취향에 맞는 영화를 찾아드리겠습니다.")
    print("질문에 답하시면 맞춤형 영화를 추천해드립니다.")
    print("언제든지 '0'을 입력하시면 프로그램을 종료할 수 있습니다.")
    print("="*50 + "\n")


def ask_question(question, options):
    """
    객관식 질문을 물어보고 답변을 받는 함수
    
    Args:
        question: 질문 내용
        options: 선택지 딕셔너리 {번호: 선택지}
    
    Returns:
        선택한 번호 또는 0 (종료)
    """
    print(f"\n{question}")
    print("-" * 40)
    
    for key, value in options.items():
        print(f"  {key}. {value}")
    
    print("-" * 40)
    
    while True:
        try:
            choice = input("선택하세요 (0: 종료): ").strip()
            
            if choice == "0":
                return 0
            
            if choice in options:
                return choice
            else:
                print("⚠️  잘못된 입력입니다. 다시 선택해주세요.")
        except KeyboardInterrupt:
            print("\n\n프로그램이 중단되었습니다.")
            return 0
        except EOFError:
            print("\n\n프로그램이 종료되었습니다.")
            return 0


def get_movie_recommendations(responses):
    """
    사용자 응답을 기반으로 영화를 추천하는 함수
    
    Args:
        responses: 사용자 응답 딕셔너리
    
    Returns:
        추천 영화 리스트
    """
    genre = responses.get("genre")
    mood = responses.get("mood")
    time_preference = responses.get("time_preference")
    
    recommendations = []
    
    # 장르와 분위기를 기반으로 영화 추천
    if genre in MOVIES and mood in MOVIES[genre]:
        movies = MOVIES[genre][mood]
        recommendations.extend(movies[:3])  # 상위 3개
    
    # 시간대 선호도에 따라 추가 조정
    if not recommendations:
        # 기본 추천 (액션/미국)
        if "액션" in MOVIES and "미국" in MOVIES["액션"]:
            recommendations = MOVIES["액션"]["미국"][:3]
        else:
            recommendations = ["매트릭스", "인셉션", "터미네이터"]
    
    # 중복 제거 및 최대 5개까지
    recommendations = list(dict.fromkeys(recommendations))[:5]
    
    return recommendations if recommendations else ["포레스트 검프", "쇼생크 탈출", "인셉션"]


def main():
    """메인 함수"""
    print_welcome()
    
    responses = {}
    
    # 질문 1: 선호하는 장르
    genre_question = "어떤 장르의 영화를 좋아하시나요?"
    genre_options = {
        "1": "액션",
        "2": "코미디",
        "3": "드라마",
        "4": "공포",
        "5": "로맨스",
        "6": "SF"
    }
    
    choice = ask_question(genre_question, genre_options)
    if choice == 0:
        print("\n👋 프로그램을 종료합니다. 감사합니다!")
        return
    
    genre_map = {"1": "액션", "2": "코미디", "3": "드라마", 
                 "4": "공포", "5": "로맨스", "6": "SF"}
    responses["genre"] = genre_map[choice]
    
    # 질문 2: 선호하는 분위기/스타일
    mood_question = "어떤 분위기의 영화를 원하시나요?"
    
    # 장르에 따라 분위기 선택지 조정
    if responses["genre"] == "액션":
        mood_options = {
            "1": "미국",
            "2": "한국",
            "3": "SF"
        }
    elif responses["genre"] == "코미디":
        mood_options = {
            "1": "미국",
            "2": "한국",
            "3": "로맨틱"
        }
    elif responses["genre"] == "드라마":
        mood_options = {
            "1": "미국",
            "2": "한국",
            "3": "감동"
        }
    elif responses["genre"] == "공포":
        mood_options = {
            "1": "미국",
            "2": "한국",
            "3": "스릴러"
        }
    elif responses["genre"] == "로맨스":
        mood_options = {
            "1": "미국",
            "2": "한국",
            "3": "코미디"
        }
    else:  # SF
        mood_options = {
            "1": "미국",
            "2": "한국",
            "3": "액션"
        }
    
    choice = ask_question(mood_question, mood_options)
    if choice == 0:
        print("\n👋 프로그램을 종료합니다. 감사합니다!")
        return
    
    mood_map = {
        "1": mood_options["1"],
        "2": mood_options["2"],
        "3": mood_options["3"]
    }
    responses["mood"] = mood_map[choice]
    
    # 질문 3: 시청 시간대 선호도
    time_question = "언제 영화를 감상하고 싶으신가요?"
    time_options = {
        "1": "저녁 시간 (긴장감 있는 영화)",
        "2": "주말 오후 (편안한 영화)",
        "3": "밤 늦게 (집중도 높은 영화)"
    }
    
    choice = ask_question(time_question, time_options)
    if choice == 0:
        print("\n👋 프로그램을 종료합니다. 감사합니다!")
        return
    
    responses["time_preference"] = choice
    
    # 영화 추천
    print("\n" + "="*50)
    print("🎬 추천 영화 목록 🎬")
    print("="*50)
    
    recommendations = get_movie_recommendations(responses)
    
    for i, movie in enumerate(recommendations, 1):
        print(f"  {i}. {movie}")
    
    print("="*50)
    print("\n💡 추천된 영화를 즐겁게 감상하시길 바랍니다!")
    print("👋 프로그램을 종료합니다. 감사합니다!\n")


if __name__ == "__main__":
    main()
