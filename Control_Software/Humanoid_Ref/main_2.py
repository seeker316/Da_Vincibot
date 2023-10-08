import time

from coppeliasim_zmqremoteapi_client import *
from humanoid_robot import HumanoidRobot

def main():
    client = RemoteAPIClient()
    sim = client.getObject('sim')
    robot = HumanoidRobot(sim)
    sim.startSimulation()
    try:
    
        # robot.start_upper()
        # time.sleep(2)
        robot.start_lower()
        time.sleep(0.1)

        for i in range(5):
            robot.transfer_left()
            time.sleep(0.1)
            robot.raise_right()
            time.sleep(0.1)
            robot.transfer_right()
            time.sleep(0.1)
            robot.raise_left()
            time.sleep(0.1)

        # robot.stop()

    
    except KeyboardInterrupt:
        sim.stopSimulation()
        # robot.stand()


if __name__ == '__main__':
    main()
