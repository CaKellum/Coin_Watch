import unittest
from ..main import data_manager as dm;
from ..main import db_manager as db;
from ..main import figure_trend as ft;

class coin_watch_tests:

    def testfigure_trend(self):
        pass


    def testmanage_email(self):
        pass


    def testdb_manager(self):
        conn = db.db_connect();
        self.assertNotNone(conn)


    def testdata_manager(self):
        pass


if __name__ == "__main__":
    unittest.main()