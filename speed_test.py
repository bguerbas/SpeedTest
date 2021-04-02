import speedtest
from datetime import datetime
import pandas as pd
from threading import Timer
import unittest


class internet_function_test(unittest.TestCase):
    def test_internet_function(self):
        self.assertEqual([retrieve_current.date(), retrieve_current.time(), round(retrieve_current.internet_speed())],
                         internet(lambda parameters_list: parameters_list))


class retrieve_current:
    @ staticmethod
    def time():
        return datetime.now().strftime('%H:%M')

    @ staticmethod
    def date():
        return datetime.now().strftime('%d/%m/%Y')

    @ staticmethod
    def internet_speed():
        return speedtest.Speedtest().download(threads=None)*(10**-6)


def write_to_excel(parameters_list):
    df = pd.read_excel('dados.xlsx', sheet_name='base')
    df.loc[len(df)] = parameters_list
    df.to_excel('dados.xlsx', sheet_name='base', index=False)


def internet(write_function):
    write_function([retrieve_current.date(),
                    retrieve_current.time(),
                    round(retrieve_current.internet_speed())])


def execute_application():
    internet(write_to_excel)
    Timer(1, execute_application).start()


unittest.main()
execute_application()
