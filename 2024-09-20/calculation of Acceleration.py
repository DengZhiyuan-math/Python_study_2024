def get_input():
    data = input("please enter distance, time and initial velocity, seperate the input with space:")
    distance, time, initial_velocity = map(float, data.split())
    return distance, time, initial_velocity

def calculate_acceleration(distance, time, initial_velocity):
    if time == 0:
        raise ValueError("time cannot be zero")
    acceleration = (distance - time * initial_velocity)
    return acceleration



if __name__ == "__main__":
    try:
        distance, time, initial_velocity = get_input()
        acceleration = calculate_acceleration(distance, time, initial_velocity)
        print(f"The acceleration is: {acceleration} m/s^2")
    except ValueError as e:
        print(e)