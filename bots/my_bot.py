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
  enemy = 3 - me

  planets = obs["planets"]
  my_planets = []
  num_my_planets = 0
  num_my_ships = 0

  enemy_planets = []
  num_enemy_planets = 0
  num_enemy_ships = 0

  neutral_planets = []

  move = []

  for p in planets :
    if p[3] == me :
      my_planets.append(p)
      num_my_planets += 1
      num_my_ships += p[4]
    elif p[3] == enemy :
      enemy_planets.append(p)
      num_enemy_planets += 1
      num_enemy_ships += p[4]
    else :
      neutral_planets.append(p)
          
  if num_my_ships >= 500 :
    for p in my_planets :
      min_distence = 99999
      min_planet = -1
      for e in enemy_planets :
        d = distance(p, e)
        if d < min_distence :
          min_distence = d
          min_planet = e[0]
      if min_planet == -1 : continue
      ships = p[4]
      if ships <= 0:
        continue
      move.append([p[0], min_planet, ships])
    return move
  
  for p in my_planets :
    min_distence = 99999
    min_planet = -1
    for n in neutral_planets :
      d = distance(p, n)
      if d < min_distence :
        min_distence = d
        min_planet = n[0]
    if min_planet == -1 : continue
    ships = p[4] // 2
    if ships <= 0:
      continue

    move.append([p[0], min_planet, ships])

  return move
