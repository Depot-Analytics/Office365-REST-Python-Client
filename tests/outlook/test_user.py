from tests.graph_case import GraphTestCase


class TestOutlookUser(GraphTestCase):

    def test1_my_supported_languages(self):
        result = self.client.me.outlook.supported_languages().execute_query()
        self.assertIsNotNone(result.value)

    def test2_my_supported_time_zones(self):
        result = self.client.me.outlook.supported_time_zones().execute_query()
        self.assertIsNotNone(result.value)
