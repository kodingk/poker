# test_suite.py
# 드로우 포커 수업 버전용 단일 테스트 모듈
# python test_suite.py 로 실행
# TODO가 남아 있으면 해당 항목은 SKIP 으로 표시됩니다.

from cards import Card, Hand
from game import compare_hands
from players import Dealer

def make_hand(cards_str):
    # 예: '♠A ♠K ♠Q ♠J ♠10'
    parts = cards_str.split()
    cards = [Card(suit=p[0], rank=p[1:]) for p in parts]
    h = Hand()
    h.add(cards)
    return h

def run_eval_test(title, cards_str, expect_rank, expect_tb=None):
    print(f"[Hand.evaluate] {title} ... ", end="")
    h = make_hand(cards_str)
    try:
        rank, tb = h.evaluate()
    except NotImplementedError:
        print("SKIP (TODO)")
        return
    if expect_tb is None:
        assert rank == expect_rank
    else:
        assert rank == expect_rank and tb == expect_tb
    print("OK")


def run_compare_test(title, a_str, b_str, expect):
    print(f"[compare_hands] {title} ... ", end="")
    a = make_hand(a_str)
    b = make_hand(b_str)
    try:
        res = compare_hands(a, b)
    except NotImplementedError:
        print("SKIP (TODO)")
        return
    assert res == expect
    print("OK")


def run_dealer_test():
    print("[Dealer AI] 반환 형식 ... ", end="")
    d = Dealer()
    d.hand.add([
        Card("♠", "A"), Card("♦", "7"),
        Card("♥", "2"), Card("♣", "9"),
        Card("♠", "4")
    ])
    # 구현 전이면 그냥 [] 를 반환해도 무방
    idx = d.choose_discard_indices()
    assert isinstance(idx, list)
    for i in idx:
        assert 0 <= i < 5
    print("OK")


if __name__ == "__main__":
    print("=== 테스트 시작 ===\n")

    # Hand.evaluate 기본 족보들
    run_eval_test("스트레이트 플러시", "♠A ♠K ♠Q ♠J ♠10", 8, [14])
    run_eval_test("포카드", "♠K ♥K ♦K ♣K ♠3", 7)  # tiebreak 상세는 구현 방식 따라 다를 수 있음
    run_eval_test("풀하우스", "♠Q ♥Q ♦Q ♠9 ♥9", 6, [12, 9])
    run_eval_test("플러시", "♠A ♠J ♠9 ♠4 ♠3", 5)
    run_eval_test("A-2-3-4-5 스트레이트", "♠A ♦5 ♥4 ♠3 ♣2", 4, [5])
    run_eval_test("투페어", "♠Q ♥Q ♦8 ♣8 ♠2", 2)
    run_eval_test("원페어", "♠J ♥J ♦9 ♠4 ♥3", 1)
    run_eval_test("하이카드", "♠A ♥Q ♦9 ♠4 ♥3", 0)

    print("")  # 줄바꿈

    # compare_hands
    run_compare_test("랭크 우위 비교", "♠A ♠K ♠Q ♠J ♠10", "♠K ♥K ♦K ♣K ♠3", 1)
    run_compare_test("타이브레이커 비교", "♠A ♥A ♦K ♣Q ♠3", "♠A ♥A ♦Q ♣J ♠3", 1)
    run_compare_test("완전 무승부", "♠A ♥A ♦K ♣Q ♠3", "♦A ♣A ♥K ♠Q ♦3", 0)

    print("")  # 줄바꿈

    # Dealer AI
    run_dealer_test()

    print("\n모든 완료 (남은 항목은 SKIP 로 표시됨) ✅")
