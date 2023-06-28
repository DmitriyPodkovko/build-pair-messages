from const.constants import tickets, comments
from handlers.buildpairmessages import BuildPairMessages

ls_pair_msgs = BuildPairMessages(tickets, comments)

if __name__ == '__main__':
    ls_pair_msgs.build()
