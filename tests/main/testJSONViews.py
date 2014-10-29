from django.test import TestCase
from main.json_views import StatusCollection, StatusMember
from main.models import StatusReport
from main.serializers import StatusReportSerializer


class dummyRequest(object):

    def __init__(self, method):
        self.method = method
        self.encoding = 'utf8'
        self.user = "root"
        self.QUERY_PARAMS = {}
        self.META = {}


class JsonViewTests(TestCase):

    def test_get_collection(self):
        status = StatusReport.objects.all()
        expected_json = StatusReportSerializer(status, many=True).data
        response = StatusCollection.as_view()(dummyRequest("GET"))

        self.assertEqual(expected_json, response.data)