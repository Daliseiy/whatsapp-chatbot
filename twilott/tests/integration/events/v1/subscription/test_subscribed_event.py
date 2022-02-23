# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class SubscribedEventTestCase(IntegrationTestCase):

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.events.v1.subscriptions("DFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .subscribed_events.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://events.twilio.com/v1/Subscriptions/DFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/SubscribedEvents',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "types": [],
                "meta": {
                    "page": 0,
                    "page_size": 10,
                    "first_page_url": "https://events.twilio.com/v1/Subscriptions/DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SubscribedEvents?PageSize=10&Page=0",
                    "previous_page_url": null,
                    "url": "https://events.twilio.com/v1/Subscriptions/DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SubscribedEvents?PageSize=10&Page=0",
                    "next_page_url": null,
                    "key": "types"
                }
            }
            '''
        ))

        actual = self.client.events.v1.subscriptions("DFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .subscribed_events.list()

        self.assertIsNotNone(actual)

    def test_read_results_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "types": [
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "type": "com.twilio.messaging.message.delivered",
                        "schema_version": 2,
                        "subscription_sid": "DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "url": "https://events.twilio.com/v1/Subscriptions/DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SubscribedEvents/com.twilio.messaging.message.delivered"
                    },
                    {
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "type": "com.twilio.messaging.message.failed",
                        "schema_version": 15,
                        "subscription_sid": "DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "url": "https://events.twilio.com/v1/Subscriptions/DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SubscribedEvents/com.twilio.messaging.message.failed"
                    }
                ],
                "meta": {
                    "page": 0,
                    "page_size": 50,
                    "first_page_url": "https://events.twilio.com/v1/Subscriptions/DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SubscribedEvents?PageSize=50&Page=0",
                    "previous_page_url": null,
                    "url": "https://events.twilio.com/v1/Subscriptions/DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SubscribedEvents?PageSize=50&Page=0",
                    "next_page_url": null,
                    "key": "types"
                }
            }
            '''
        ))

        actual = self.client.events.v1.subscriptions("DFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .subscribed_events.list()

        self.assertIsNotNone(actual)

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.events.v1.subscriptions("DFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .subscribed_events.create(type="type")

        values = {'Type': "type", }

        self.holodeck.assert_has_request(Request(
            'post',
            'https://events.twilio.com/v1/Subscriptions/DFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/SubscribedEvents',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "subscription_sid": "DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "type": "com.twilio.messaging.message.delivered",
                "schema_version": 2,
                "url": "https://events.twilio.com/v1/Subscriptions/DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SubscribedEvents/com.twilio.messaging.message.delivered"
            }
            '''
        ))

        actual = self.client.events.v1.subscriptions("DFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .subscribed_events.create(type="type")

        self.assertIsNotNone(actual)

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.events.v1.subscriptions("DFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .subscribed_events("type").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://events.twilio.com/v1/Subscriptions/DFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/SubscribedEvents/type',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "subscription_sid": "DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "type": "com.twilio.messaging.message.delivered",
                "schema_version": 2,
                "url": "https://events.twilio.com/v1/Subscriptions/DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SubscribedEvents/com.twilio.messaging.message.delivered"
            }
            '''
        ))

        actual = self.client.events.v1.subscriptions("DFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .subscribed_events("type").fetch()

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.events.v1.subscriptions("DFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .subscribed_events("type").update()

        self.holodeck.assert_has_request(Request(
            'post',
            'https://events.twilio.com/v1/Subscriptions/DFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/SubscribedEvents/type',
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "subscription_sid": "DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "type": "com.twilio.messaging.message.delivered",
                "schema_version": 2,
                "url": "https://events.twilio.com/v1/Subscriptions/DFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/SubscribedEvents/com.twilio.messaging.message.delivered"
            }
            '''
        ))

        actual = self.client.events.v1.subscriptions("DFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .subscribed_events("type").update()

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.events.v1.subscriptions("DFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                 .subscribed_events("type").delete()

        self.holodeck.assert_has_request(Request(
            'delete',
            'https://events.twilio.com/v1/Subscriptions/DFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX/SubscribedEvents/type',
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.events.v1.subscriptions("DFXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                                      .subscribed_events("type").delete()

        self.assertTrue(actual)