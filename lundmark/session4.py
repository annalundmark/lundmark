import requests
import getpass
from dateutil import parser
from pandas import Series
from pandas import DataFrame
from collections import Counter

def main(): 
	commits=get_dataframe()
	get_day_hour(commits)

def get_credentials(): 
	user=raw_input("Username:")
	passwd=getpass.getpass()
	return [user, passwd]

def get_dataframe(): 
	[user, passwd] = get_credentials()
	repos=requests.get("https://api.github.com/orgs/pythonkurs/repos", auth=(user, passwd))
	repos_data=repos.json()
	#print repos_data[0]
	#print len(users_data)
	
	date_list=[]
	message_list=[]
	
	for repo in repos_data: 
		commit_url = repo['commits_url'][:-6]
		commits = requests.get(commit_url, auth=(user, passwd))
		commits_data = commits.json()
		for commit in commits_data: 
			try: 
				date = parser.parse(commit[u'commit'][u'author']['date'])
				date_list.append(date)
				message = commit[u'commit'][u'message']
				message_list.append(message)
			except TypeError: continue
		print 'added all the commits from repo '+repo['name']+' to lists'
	
	s = Series(message_list, index = date_list)
	df = DataFrame(s)
	
	#print date_list, message_list
	
	return df

def get_day_hour(commits): 
	days = commits.index.dayofweek
	hours = commits.index.hour
	counter_days = Counter(days)
	counter_hours = Counter(hours)
	weekday = counter_days.most_common(1)[0][0]
	hour = counter_hours.most_common(1)[0][0]
	weekday_list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
		
	print "The most common weekday for commits to pythonkurs is " + str(weekday_list[weekday]) + " and the most common hour is " + str(hour) 
	
			
if __name__ == "__main__": 
	main()