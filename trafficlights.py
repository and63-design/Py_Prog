#create a traffic light class with three states: red, amber, green
#each state has a method to change to the next state

class TrafficLight:
    def __init__(self):
        self.state = "red"

    def change(self):
        if self.state == "red":
            self.state = "green"
        elif self.state == "green":
            self.state = "amber"
        elif self.state == "amber":
            self.state = "red"

    def __str__(self):
        return f"Traffic light is {self.state}"
    def __repr__(self):
        return f"TrafficLight(state={self.state})"
    def get_state(self):
        return self.state
    def set_state(self, state):
        if state in ["red", "amber", "green"]:
            self.state = state
        else:
            raise ValueError("Invalid state. Must be 'red', 'amber', or 'green'.")
    def is_red(self):
        return self.state == "red"
    def is_amber(self):
        return self.state == "amber"
    def is_green(self):
        return self.state == "green"        
    def reset(self):
        self.state = "red"
    def next_state(self):
        self.change()
        return self.state
    
# Example usage:

if __name__ == "__main__":
    traffic_light = TrafficLight()
    print(traffic_light)
    traffic_light.change()
    print(traffic_light)
    traffic_light.change()
    print(traffic_light)
    traffic_light.change()
    print(traffic_light)
    traffic_light.reset()
    print(traffic_light)

    traffic_light.set_state("amber")
    print(traffic_light)
    traffic_light.set_state("green")
    print(traffic_light)
    traffic_light.set_state("red")
    print(traffic_light)    