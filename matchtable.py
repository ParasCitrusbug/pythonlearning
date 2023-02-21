import random


class Matchs:
    """sidual for team matches in day."""

    def __init__(self) -> str:
        self.team_list = list()

    def team(self) -> str:
        """Create team matches."""
        number = int(input("Enter total team: "))
        total_match = 0
        for i in range(1, number + 1):
            for j in range(i + 1, number + 1):
                total_match += 1
                self.team_list.append([i, j])
        return f"total number of match is {total_match}"

    def match_day_timetable(self) -> dict:
        """Sidual match in day."""
        dict_day = {}
        team_list_data = self.team_list
        random.shuffle(team_list_data)
        day_per_match_input = int(
            input(
                "per day match maximum per day 3 matchs so, enter the your wise in monday to friday match:  "
            )
        )

        day_per_match_input2 = int(
            input(
                "per day match maximum per day 5 matchs so, enter the your wise in saturday and sunday :  "
            )
        )
        # if day_per_match_input>3 or day_per_match_input2 >5:
        #     return "please insert of value is given to the statement"
        i = 1
        saterday_teamp = 6
        while team_list_data:
            if i % 7 == 0 or saterday_teamp == i:
                dict_day[f"day{i}"] = team_list_data[:day_per_match_input2]
                saterday_teamp += 3.5

                if len(team_list_data) >= day_per_match_input2:
                    [team_list_data.pop(0) for _ in range(day_per_match_input2)]
                else:
                    break
            else:
                dict_day[f"day{i}"] = team_list_data[:day_per_match_input]
                if len(team_list_data) >= day_per_match_input:
                    [team_list_data.pop(0) for _ in range(day_per_match_input)]
                else:
                    break
            i = i + 1
        return dict_day


obj = Matchs()
print(obj.team())
print(obj.match_day_timetable())
