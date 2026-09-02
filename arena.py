"""대전 러너 — N판 돌려 승/패/무를 센다.

    .venv/Scripts/python.exe arena.py bots/my_bot.py do_nothing -n 20

봇은 내장 봇 이름(do_nothing, random, nearest_enemy) 이거나 .py 파일 경로다.
D2 에서 신뢰구간과 실험 로그를 붙인다.
"""

import argparse
import pathlib

from kaggle_environments import evaluate


def resolve(spec):
    return str(pathlib.Path(spec).resolve()) if spec.endswith(".py") else spec


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("a", help="플레이어 1")
    ap.add_argument("b", help="플레이어 2")
    ap.add_argument("-n", type=int, default=20, help="판 수")
    ap.add_argument("--env", default="planet_wars")
    args = ap.parse_args()

    rewards = evaluate(args.env, [resolve(args.a), resolve(args.b)], num_episodes=args.n)

    # reward 가 None 이면 그 봇이 ERROR / TIMEOUT / 무효 명령으로 몰수패 한 것이다.
    # 패배로 세되 따로 표시한다 — 조용히 넘어가면 진짜 문제를 놓친다.
    err = sum(1 for r in rewards if r[0] is None)
    win = sum(1 for r in rewards if r[0] is not None and (r[1] is None or r[0] > r[1]))
    loss = sum(1 for r in rewards if r[0] is None or (r[1] is not None and r[0] < r[1]))
    draw = len(rewards) - win - loss

    tail = f"   [내 봇 몰수패 {err}판]" if err else ""
    print(f"{args.a} vs {args.b}  ->  W{win} L{loss} D{draw}   승률 {win / len(rewards):.0%}{tail}")


if __name__ == "__main__":
    main()
