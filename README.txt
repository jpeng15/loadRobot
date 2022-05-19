loadRobot.py

loadRobot(loadID, x, y)
loadRobot sends a get request to https://60c8ed887dafc90017ffbd56.mockapi.io/robots to retrieve a list of all 100 robots in the fleet including their
ID number, current x and y coordinates, and current battery level. It returns a dictionary contatining the id of the robot selected to transport the load along with its
distance from the load and its battery level
Parameters:
    loadID: the load ID
    x: the x coordinate of the load
    y: the y coordinate of the load

Return:
    roboInfo: dictionary containin the required information about the robot selected to move the load

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Extra features to implement:

Robot control: after selecting a robot to pick up the load, send a message to the robot telling it to move to the package and deliver it to its desired location

Continous robot tracking: after selecting a robot to pick up the load, the function could continue to send requests to the API to obtain live location and battery level
information about the robot until the robot picks up the load and the load is delivered to its desired location.

Battery Level calculations: the function could also calculate how much battery power it would take to devlier the package and if a selected robot does not have the required
power, the function would select another robot.


