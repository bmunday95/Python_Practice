from datetime import date, time, datetime

sealed = date(2020, 1, 20)
date_diff = date.today()-sealed
prison = date_diff.days

print(f'Shibuya Incident: October 31st 2018. '
      f'\nChapter 91 was released on January 20th 2020.'
      f'\nGojo Satoru has been sealed for {prison} days.')
