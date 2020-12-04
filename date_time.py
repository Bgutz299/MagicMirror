from datetime import date, datetime

def date_get():
	today = date.today()
	today_date = today.strftime("%B %d, %Y")
	return today_date
def time_get():
	now = datetime.now()
	now_conv = now.strftime("%H:%M %p")
	curr_time = now_conv
	return curr_time
