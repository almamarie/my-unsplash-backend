# test imports
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flaskr import create_app
from models import UserDetails, FilesData, setup_db
from config import SQLALCHEMY_DATABASE_URI


class UnsplashTesCase(unittest.TestCase):
    """This class represents the Human rights situation test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "unsplash"
        self.database_path = SQLALCHEMY_DATABASE_URI

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_up_and_running(self):
        res = self.client().get('/')
        body = json.loads(res.data)
        expected_output = {"success": True,
                           "message": "Configuration Successful"}
        self.assertEqual(body, expected_output)

    # # ====================================================================================
    # # post a new report
    # # Tests for /reports method = ['POST']
    # # ====================================================================================
    # # successful operation

    # def test_add_a_new_report(self):
    #     sample_report = {
    #         "data_report_made": datetime.now(),
    #         "country": "The Gambia",
    #         "region": "West Africa",
    #         "complain":  'Test Heres another new complain string',
    #     }

    #     res = self.client().post('/questions', json=sample_report)

    #     report = Hrsreport.query.filter(
    #         Hrsreport.complain == sample_report['complain']).one_or_none()

    #     data = json.loads(res.data)
    #     # print("\n\nadd new question: ", data, '\n\n')
    #     self.assertTrue(data['success'], True)
    #     self.assertTrue(report.any())
    #     self.assertEquat(report.region, sample_report['region'])

    # # test 422_body incomplete (body has no question)
    # def test_422_post_question_without_a_required_field(self):
    #     sample_report = {
    #         "region": "West Africa",
    #         "complain":  'Test Heres another new complain string',
    #     }

    #     res = self.client().post('/questions', json=sample_report)
    #     data = json.loads(res.data)

    #     report = Hrsreport.query.filter(
    #         Hrsreport.complain == sample_report['complain']).one_or_none()
    #     self.assertIsNone(report)
    #     self.assertTrue(res.status_code, 422)


if __name__ == "__main__":
    unittest.main()
