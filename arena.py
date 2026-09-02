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

    win = sum(1 for r in rewards if r[0] > r[1])
    loss = sum(1 for r in rewards if r[0] < r[1])
    draw = len(rewards) - win - loss
    print(f"{args.a} vs {args.b}  ->  W{win} L{loss} D{draw}   승률 {win / len(rewards):.0%}")


if __name__ == "__main__":
    main()
