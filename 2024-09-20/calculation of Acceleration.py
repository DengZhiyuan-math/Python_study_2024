def get_input():
    data = input("please enter distance, time and initial velocity, seperate the input with space")
        distance = int(data[0])
        time = int(data[1])
        initial_velocity = int(data[2])
    return distance, time, initial_velocity

def calculate_acceleration():
    acceleration = (distance - time * initial_velocity)



