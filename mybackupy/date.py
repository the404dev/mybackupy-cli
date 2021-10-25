from datetime import datetime

class Date:
    def get_current_date_and_time():
        now = datetime.now()
        str_datetime = now.strftime("%d_%m_%Y_%H_%M_%S")
        return str_datetime
