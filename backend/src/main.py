from backend.src.spotify_api.skip_listener import SKIP_LISTENER
from backend.src.model.decision_maker import DecisionLoop
from backend.src.config import settings
from multiprocessing import Process

def main():
    processes=[]
    loop_1=DecisionLoop()
    loop_2=SKIP_LISTENER()
    p1 = Process(target=loop_1.decision_maker(), args=())
    processes.append(p1)
    p2 = Process(target=loop_2.decision_maker(), args=())
    processes.append(p2)

if __name__ == "__main__":
    main()