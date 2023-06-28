from handlers.buildpairmessages import BuildPairMessages


class TestCompareData:
    """This class is for comparing the output data with the expected data

    -------

    def test_build(self):
        Compares of the expected result
    """

    _tickets = [
        {"ticket_id": 1},
        {"ticket_id": 2},
        {"ticket_id": 3}
    ]

    _comments = [
        {"conversation_id": 12345678,
         "msgs": [{"input": "some_text_input1_12345678"},
                  {"output": "some_text_output1_12345678"}
                  ],
         "ticket_id": 1
         },
        {"conversation_id": 123456789,
         "msgs": [{"input": "some_text_input1_123456789"},
                  {"output": "some_text_output1_123456789"},
                  {"input": "some_text_input_2_unpair"},
                  {"input": "some_text_input_3_unpair"},
                  ],
         "ticket_id": 2
         },
        {"conversation_id": 12345678910,
         "msgs": [{"output": "some_text_output_0_unpair"},
                  {"input": "some_text_input1_12345678910"},
                  {"output": "some_text_output1_12345678910"},
                  {"input": "some_text_input2_12345678910"},
                  {"output": "some_text_output2_12345678910"},
                  {"input": "some_text_input_3_unpair"},
                  {"input": "some_text_input_4_unpair"},
                  {"input": "some_text_input5_12345678910"},
                  {"output": "some_text_output5_12345678910"},
                  {"output": "some_text_output_6_unpair"},
                  {"input": "some_text_input_7_unpair"},

                  ],
         "ticket_id": 3
         }
    ]

    _expected = [
        {'conversation_id': 12345678,
         'input': 'some_text_input1_12345678',
         'output': 'some_text_output1_12345678',
         'ticket_id': 1,
         'count': 1
         },
        {'conversation_id': 123456789,
         'input': 'some_text_input1_123456789',
         'output': 'some_text_output1_123456789',
         'ticket_id': 2,
         'count': 1
         },
        {'conversation_id': 12345678910,
         'input': 'some_text_input1_12345678910',
         'output': 'some_text_output1_12345678910',
         'ticket_id': 3,
         'count': 1
         },
        {'conversation_id': 12345678910,
         'input': 'some_text_input2_12345678910',
         'output': 'some_text_output2_12345678910',
         'ticket_id': 3,
         'count': 2
         },
        {'conversation_id': 12345678910,
         'input': 'some_text_input5_12345678910',
         'output': 'some_text_output5_12345678910',
         'ticket_id': 3,
         'count': 3
         }

    ]

    def test_build(self):
        """Compares of the expected result

        :return: True or AssertionError
        """
        ls_pair_msgs = BuildPairMessages(self._tickets, self._comments).build()
        assert ls_pair_msgs == self._expected
