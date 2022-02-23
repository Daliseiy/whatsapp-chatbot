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


class RoomTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.insights.v1.rooms("RMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://insights.twilio.com/v1/Video/Rooms/RMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "room_type": "go",
                "unique_participant_identities": 0,
                "codecs": [
                    "VP8"
                ],
                "max_participants": 0,
                "room_sid": "RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "create_time": "2015-07-30T20:00:00Z",
                "end_reason": "room_ended_via_api",
                "duration_sec": 50000000,
                "room_status": "in_progress",
                "media_region": "us1",
                "recording_enabled": false,
                "edge_location": "ashburn",
                "max_concurrent_participants": 0,
                "unique_participants": 0,
                "room_name": "room_name",
                "created_method": "sdk",
                "total_participant_duration_sec": 50000000,
                "status_callback_method": "GET",
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "end_time": "2015-07-30T20:00:00Z",
                "total_recording_duration_sec": 50000000,
                "processing_state": "complete",
                "concurrent_participants": 0,
                "status_callback": "http://www.example.com",
                "url": "https://insights.twilio.com/v1/Video/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "participants": "https://insights.twilio.com/v1/Video/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants"
                }
            }
            '''
        ))

        actual = self.client.insights.v1.rooms("RMXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

    def test_list_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.insights.v1.rooms.list()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://insights.twilio.com/v1/Video/Rooms',
        ))

    def test_read_empty_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "first_page_url": "https://insights.twilio.com/v1/Video/Rooms?PageSize=50&Page=0",
                    "url": "https://insights.twilio.com/v1/Video/Rooms?PageSize=50&Page=0",
                    "page_size": 50,
                    "next_page_url": null,
                    "key": "rooms",
                    "page": 0,
                    "previous_page_url": null
                },
                "rooms": []
            }
            '''
        ))

        actual = self.client.insights.v1.rooms.list()

        self.assertIsNotNone(actual)

    def test_read_full_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "meta": {
                    "first_page_url": "https://insights.twilio.com/v1/Video/Rooms?PageSize=50&Page=0",
                    "url": "https://insights.twilio.com/v1/Video/Rooms?PageSize=50&Page=0",
                    "page_size": 50,
                    "next_page_url": null,
                    "key": "rooms",
                    "page": 0,
                    "previous_page_url": null
                },
                "rooms": [
                    {
                        "room_type": "go",
                        "unique_participant_identities": 0,
                        "codecs": [
                            "VP8"
                        ],
                        "max_participants": 0,
                        "room_sid": "RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "create_time": "2015-07-30T20:00:00Z",
                        "end_reason": "room_ended_via_api",
                        "duration_sec": 50000000,
                        "room_status": "in_progress",
                        "media_region": "us1",
                        "recording_enabled": false,
                        "edge_location": "ashburn",
                        "max_concurrent_participants": 0,
                        "unique_participants": 0,
                        "room_name": "room_name",
                        "created_method": "sdk",
                        "total_participant_duration_sec": 50000000,
                        "status_callback_method": "GET",
                        "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "end_time": "2015-07-30T20:00:00Z",
                        "total_recording_duration_sec": 50000000,
                        "processing_state": "complete",
                        "concurrent_participants": 0,
                        "status_callback": "http://www.example.com",
                        "url": "https://insights.twilio.com/v1/Video/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                        "links": {
                            "participants": "https://insights.twilio.com/v1/Video/Rooms/RMaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Participants"
                        }
                    }
                ]
            }
            '''
        ))

        actual = self.client.insights.v1.rooms.list()

        self.assertIsNotNone(actual)
