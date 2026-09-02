"""planet_wars 첫 봇 — D1.

목표: do_nothing 상대 20판 전승.
    .venv/Scripts/python.exe arena.py bots/my_bot.py do_nothing -n 20


── 관측 (obs) ────────────────────────────────────────────────────────────
obs["player"]   내 번호. 1 또는 2. (중립 행성의 owner 는 0)
obs["step"]     현재 턴. 0 부터 시작, episodeSteps=200
obs["planets"]  [id, x, y, owner, num_ships, growth_rate] 의 리스트
                - id 는 planets 리스트의 인덱스와 같다
                - x, y 는 실수 좌표 (격자 아님)
                - owner: 0=중립, 1=P1, 2=P2
                - growth_rate: 1~5. 소유 중이면 매 턴 이만큼 함선이 늘어난다.
                  중립 행성은 늘지 않는다.
obs["fleets"]   [owner, num_ships, source, dest, total_trip, turns_remaining] 의 리스트
                - 이동 중인 함대. 양쪽 플레이어 것이 모두 보인다.

── 행동 (반환값) ─────────────────────────────────────────────────────────
[[source_id, dest_id, ships], ...] 형태의 리스트를 반환한다.
아무것도 안 할 때는 None 이 아니라 [] 를 반환할 것.

유효성 규칙 — 하나라도 어기면 그 자리에서 몰수패다:
    - ships > 0
    - source != dest
    - source, dest 모두 유효한 행성 id
    - source 는 내가 소유한 행성이어야 한다
    - 한 행성에서 나가는 ships 합계 <= 그 행성의 num_ships

── 규칙 ──────────────────────────────────────────────────────────────────
이동 시간 = ceil(두 행성 사이 유클리드 거리) 턴.
도착하면 그 행성에서 전투. 가장 큰 세력이 이기고 (1등 - 2등) 만큼 남는다.
200턴이 지나면 함선 총합(행성 + 이동 중)이 많은 쪽이 승리.
"""

import math


def distance(a, b):
    """행성 a 에서 b 까지 걸리는 턴 수."""
    return math.ceil(math.hypot(a[1] - b[1], a[2] - b[2]))


def agent(obs, config=None):
    me = obs["player"]
    planets = obs["planets"]

    # TODO: 여기를 채운다.
    #
    # 가장 단순한 출발점 — 내 행성마다 함선 절반을 어딘가 내 것이 아닌 행성으로 보낸다.
    # 그것만으로 do_nothing 은 이긴다. 이긴 다음에 목표 선택을 개선한다.
    #
    # 생각해볼 것:
    #   - 어느 행성을 칠까? 가까운 곳 / 성장률 높은 곳 / 수비가 약한 곳
    #   - 몇 척을 보낼까? 절반은 게으른 답이다. 점령에 필요한 최소는 몇인가?
    #   - 도착할 때쯤 그 행성의 함선은 몇 척이 되어 있을까?

    return []
