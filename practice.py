class Player:
    def __init__(self, name, age, position, team):
        self.name = name
        self.age = age
        self.position = position
        self.team = team


kevin = {"name": "Kevin Durant", "age": 34,
        "position": "small forward", "team": "Brooklyn Nets"}

# Pass in all the values from the dictionary by their keys
player_kevin = Player(kevin["name"], kevin["age"],
                    kevin["position"], kevin["team"])
print(player_kevin.position)  # prints small forward
