# 포커 게임 실행 모듈 (드로우 포커 미니 버전, 학생용)
# compare_hands 는 TODO 로 비워두었습니다.

import random
from cards import Deck
from players import Human, Dealer

def compare_hands(hand_a, hand_b):
    # 손패 비교: (랭크코드, 타이브레이커배열) 을 비교
    # TODO: Hand.evaluate() 결과를 이용해 승패 판정 (1: a승, -1: b승, 0: 무승부)
    raise NotImplementedError("TODO: compare_hands 구현")

class PokerGame:
    # 한 라운드: 5장 배분 -> 교체 -> 비교
    def __init__(self, seed=None):
        if seed is not None:
            random.seed(seed)
        self.deck = Deck()
        self.player = Human("플레이어", bankroll=100)
        self.dealer = Dealer("딜러")
        self.pot = 0  # 베팅 금액 합

    def deal(self):
        # 5장씩 배분
        self.player.reset_hand()
        self.dealer.reset_hand()
        self.player.hand.add(self.deck.draw(5))
        self.dealer.hand.add(self.deck.draw(5))

    def betting_round(self):
        # 간단 베팅: 고정 10원
        self.pot += self.player.bet(10)
        self.pot += self.dealer.bet(10)

    def player_discard_phase(self):
        # 플레이어 카드 보기
        print("당신의 패:", " ".join(str(c) for c in self.player.hand.cards))
        raw = input("버릴 카드 인덱스를 공백으로 입력 (예: 0 2). 없으면 엔터: ").strip()
        if raw:
            try:
                idx = sorted({int(x) for x in raw.split()})
                self.player.hand.replace_with_indices(idx, self.deck)
            except Exception:
                print("입력이 잘못되어 교체하지 않습니다.")

    def dealer_discard_phase(self):
        # 딜러 교체 (간단 규칙)
        idx = self.dealer.choose_discard_indices()
        if idx:
            self.dealer.hand.replace_with_indices(idx, self.deck)

    def showdown(self):
        # 최종 핸드 공개 (evaluate 가 아직 미구현이면 예외가 날 수 있습니다)
        try:
            ra, tba = self.player.hand.evaluate()
            rb, tbb = self.dealer.hand.evaluate()
            print("당신의 최종 패:", " ".join(str(c) for c in self.player.hand.cards), f"(rank={ra}, tiebreak={tba})")
            print("딜러의 최종 패:", " ".join(str(c) for c in self.dealer.hand.cards), f"(rank={rb}, tiebreak={tbb})")
        except NotImplementedError:
            print("evaluate() 미구현 상태라 랭크 표시는 건너뜁니다.")

        try:
            res = compare_hands(self.player.hand, self.dealer.hand)
            if res > 0:
                print("당신의 승리! +", self.pot)
                self.player.win(self.pot)
            elif res < 0:
                print("딜러의 승리!")
            else:
                print("무승부! 포트 반환")
                self.player.win(self.pot // 2)
                self.dealer.win(self.pot - self.pot // 2)
        except NotImplementedError:
            print("compare_hands 미구현 상태입니다. 승패 판정은 생략합니다.")
        self.pot = 0

    def run(self):
        # 게임 한 판 실행
        print("=== 드로우 포커: 수업용 미니 버전 (학생용) ===")
        self.deal()
        self.betting_round()
        self.player_discard_phase()
        self.dealer_discard_phase()
        self.showdown()

if __name__ == "__main__":
    PokerGame().run()
