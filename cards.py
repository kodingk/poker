# 카드, 덱, 핸드 관련 모듈 (학생용)
# 수업용 버전: 핵심 로직은 TODO 로 비워두었습니다.
# 타입 어노테이션은 사용하지 않습니다. 주석은 한국어로 간단히 달았습니다.

import random

# 랭크와 무늬 정의
RANKS = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']
SUITS = ['♣','♦','♥','♠']

RANK_TO_VALUE = {r: i for i, r in enumerate(RANKS, start=2)}  # 2=2, ..., A=14

class Card:
    # 한 장의 카드를 표현
    def __init__(self, suit, rank):
        self.suit = suit   # 무늬
        self.rank = rank   # 랭크
    
    def value(self):
        # 비교용 숫자값
        return RANK_TO_VALUE[self.rank]
    
    def __str__(self):
        return f"{self.suit}{self.rank}"

class Deck:
    # 52장 덱
    def __init__(self):
        self.cards = [Card(s, r) for s in SUITS for r in RANKS]
        self.shuffle()
    
    def shuffle(self):
        # 덱 섞기
        random.shuffle(self.cards)
    
    def draw(self, n=1):
        # n장 뽑기
        drawn = self.cards[:n]
        self.cards = self.cards[n:]
        return drawn

class Hand:
    # 플레이어 손패 (5장 기준)
    def __init__(self):
        self.cards = []
    
    def add(self, cards):
        # 카드 추가
        self.cards.extend(cards)
    
    def replace_with_indices(self, indices, deck):
        # indices 에 있는 위치의 카드를 버리고 덱에서 같은 수만큼 새로 받기
        kept = [c for i, c in enumerate(self.cards) if i not in indices]
        need = len(indices)
        kept.extend(deck.draw(need))
        self.cards = kept
    
    def values_sorted(self):
        # 랭크를 숫자로 변환해 내림차순 정렬
        return sorted([c.value() for c in self.cards], reverse=True)
    
    def suits(self):
        return [c.suit for c in self.cards]
    
    def ranks(self):
        return [c.rank for c in self.cards]
    
    # ====== 여기부터 족보 판정 영역 (학생 과제) ======
    def evaluate(self):
        """
        손패의 족보를 계산하여 (랭크코드, 타이브레이커 목록) 형태로 반환.
        큰 수일수록 강한 패가 되도록 랭크코드를 정함.
        예시: 스트레이트 플러시(8) > 포카드(7) > 풀하우스(6) > 플러시(5) > 스트레이트(4) > 트리플(3) > 투페어(2) > 원페어(1) > 하이카드(0)

        반환 형식 예:
          (8, [최고카드값])
          (7, [포카드값, 남은카드])
          (6, [트리플값, 페어값])
          (5, [상위부터 카드들])
          (4, [최고카드값])
          (3, [트리플값, kickers...])
          (2, [페어큰값, 페어작은값, 남은한장])
          (1, [페어값, kickers...])
          (0, [상위부터 카드들])
        """
        # TODO: 아래 3개 헬퍼를 먼저 구현한 뒤, 해당 값을 사용해 최종 (랭크코드, 타이브레이커) 를 계산하세요.
        vals = self.values_sorted()
        suits = self.suits()

        is_flush, flush_vals = self._is_flush(vals, suits)       # TODO 구현
        is_straight, straight_high = self._is_straight(vals)     # TODO 구현
        groups = self._group_by_value(vals)                      # TODO 구현  {값: 개수}

        # TODO: 여기서부터 분기 구성
        # 힌트: groups 를 이용해 포카드(4), 풀하우스(3+2), 트리플(3), 투페어(2+2), 원페어(2) 판정
        raise NotImplementedError("TODO: Hand.evaluate() 구현")  # 임시로 예외 발생
    
    # ====== 헬퍼들 (학생 과제) ======
    def _is_flush(self, vals, suits):
        # 같은 무늬 5장인지 확인
        # 반환: (bool, 내림차순값리스트)
        # TODO: 무늬가 모두 같은지 확인하고 (True, vals) 또는 (False, vals) 반환
        raise NotImplementedError("TODO: _is_flush 구현")
    
    def _is_straight(self, vals):
        # 연속된 5장인지 확인 (A-2-3-4-5 처리 포함)
        # 반환: (bool, 최고카드값)
        # TODO: 값 집합을 사용해 연속성 확인. A2345 는 최고값 5로 처리
        raise NotImplementedError("TODO: _is_straight 구현")
    
    def _group_by_value(self, vals):
        # 같은 랭크끼리 묶어서 개수 세기 -> dict 반환
        # 예: [14,14,10,10,3] -> {14:2, 10:2, 3:1}
        # TODO: 딕셔너리로 개수 세기
        raise NotImplementedError("TODO: _group_by_value 구현")

def rank_to_str(v):
    # 숫자값을 다시 문자열로
    for r, num in RANK_TO_VALUE.items():
        if num == v:
            return r
    return str(v)
