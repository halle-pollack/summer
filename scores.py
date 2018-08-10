
team1_list = []
team2_list = []
teams_total = set()

with open('scores.txt','r') as x:
	y=x.readlines()
	for each_line in y:
		team1,_,team2,_=each_line.split(',')
		team1_list.append(team1)
		team2_list.append(team2)
		teams_total.update([team1, team2])