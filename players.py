# 플레이어 관련 모듈 (학생용)
# 딜러의 간단한 AI는 TODO 로 남겨두었습니다.

from cards import Hand

class Player:
    # 기본 플레이어
    def __init__(self, name, bankroll=100):
        self.name = name
        self.bankroll = bankroll
        self.hand = Hand()
    
    def reset_hand(self):
        # 새 라운드 시작 시 손패 초기화
        self.hand = Hand()
    
    def bet(self, amount):
        # 베팅 (잔고에서 차감)
        if amount > self.bankroll:
            amount = self.bankroll
        self.bankroll -= amount
        return amount
    
    def win(self, amount):
        # 승리 시 잔고 증가
        self.bankroll += amount

class Human(Player):
    # 사람 플레이어 (입력 기반)
    def __init__(self, name="플레이어", bankroll=100):
        super().__init__(name, bankroll)

class Dealer(Player):
    # 딜러 (간단한 교체 전략을 적용) - 학생 과제
    def __init__(self, name="딜러", bankroll=99999999):
        super().__init__(name, bankroll)
    
    def choose_discard_indices(self):
        # TODO: 딜러가 버릴 카드 인덱스를 결정하는 간단한 규칙을 구현해보세요.
        # 힌트: 하이카드면 가장 낮은 2장 정도 교체, 원페어면 페어를 제외한 3장 중 낮은 것 위주 교체 등
        return []
