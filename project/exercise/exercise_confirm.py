import exercise_tour_50 as tour
import pandas as pd

country = tour.tour_lst()
pd.DataFrame(country).to_csv('./resource/exercise.csv',header = False,index = False)
