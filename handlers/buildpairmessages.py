class BuildPairMessages:
    """This class returns a list that contains messages with paired comments
    (e.g. input-output) for the ticket.
    Unpaired comments are not included in the result

    -------

    def __init__(self, tickets: list, comments: list): -> None:

    -------

    def build(self) -> list:
        Main 'BuildPairComments' class method
        for building a list of pair messages input-output
    -------

    def _get_conversation_id(self, comment: dict) -> int:
        Returns the conversation_id value from a single message
    -------

    def _get_ticket_id(self, ticket: dict, comment: dict) -> int:
        Compares the matching ticket_id from the tickets
        with ticket_id from the comments.
        If the case is a match returns the ticket_id value from the ticket
    -------

    def _get_keys(self, keys: list) -> list[str]:
        Converts <class 'dict_keys'> to <class 'list'>
    -------

    def _get_pairs(self, msgs: list) -> list:
        Returns only pair input-output.
        Unpaired input-output-input, ... are not included in the result
    """
    def __init__(self,
                 tickets: list[dict[str, int]],
                 comments: list[dict[str, int | list[dict[str, str]]]]
                 ) -> None:
        """
        :rtype: object
        :param tickets: ticket_id list
        :param comments: list of messages
        """
        self._tickets = tickets
        self._comments = comments

    def _get_conversation_id(self,
                             comment: dict[str, int | list[dict[str, str]]]
                             ) -> int:
        """Returns the conversation_id value from a single message

        :param comment: one message from the list of messages
        :return: conversation_id value
        """
        return comment.get('conversation_id')

    def _get_ticket_id(self,
                       ticket: dict[str, int],
                       comment: dict[str, int | list[dict[str, str]]]
                       ) -> int:
        """Compares the matching ticket_id from the tickets
        with ticket_id from the comments.
        If the case is a match returns the ticket_id value from the ticket

        :param ticket: ticket_id
        :param comment: one message from the list of messages
        :return: ticket_id value
        """
        id_ticket = ticket.get('ticket_id')
        id_ticket_comment = comment.get('ticket_id')
        if id_ticket == id_ticket_comment:
            return id_ticket
        else:
            return -1

    def _get_keys(self, keys: list) -> list[str]:
        """Converts <class 'dict_keys'> to <class 'list'>

        :param keys: dict_keys object after using .keys()
        :return: key as list
        """
        l_keys = list(keys)
        # we must understand that key (input/output) is really one
        if len(l_keys) == 1:
            return l_keys
        else:
            pass  # TODO: return something

    def _get_pairs(self,
                   msgs: list[dict[str, str]]
                   ) -> list[dict[str, str]]:
        """Returns only pair input-output.
        Unpaired input-output-input, ... are not included in the result

        :param msgs: one message from the list of messages
        which contains pair or unpair input-output-input
        :return: pair input-output
        """
        pairs = []
        cnt_msgs = len(msgs)
        for mes in range(cnt_msgs):
            list_keys = self._get_keys(msgs[mes].keys())
            if (list_keys[0] == 'input') & (mes + 1 < cnt_msgs):
                list_keys_next = self._get_keys(msgs[mes + 1].keys())
                if list_keys_next[0] == 'output':
                    pairs.append(msgs[mes])
                    pairs.append(msgs[mes + 1])
        return pairs

    def build(self) -> list[dict[str, int | str]]:
        """Main 'BuildPairMessages' class method
        for building a list of pair messages input-output

        :return: list of pair messages input-output
        """
        res = []
        cnt_tickets = len(self._tickets)
        cnt_comments = len(self._comments)
        if cnt_tickets == cnt_comments:  # must match
            for i in range(cnt_tickets):
                conversation_id = self._get_conversation_id(
                    self._comments[i])
                ticket_id = self._get_ticket_id(self._tickets[i],
                                                self._comments[i])
                pairs = self._get_pairs(self._comments[i].get('msgs'))
                count = 0
                for pair in range(0, len(pairs), 2):
                    count += 1
                    res.append({'conversation_id': conversation_id,
                                'input': pairs[pair].get('input'),
                                'output': pairs[pair + 1].get('output'),
                                'ticket_id': ticket_id,
                                'count': count})
        else:
            print(f'Counts does not match!\n'
                  f'Count tickets = {cnt_tickets}, '
                  f'Count comments = {cnt_comments}')
        return res
