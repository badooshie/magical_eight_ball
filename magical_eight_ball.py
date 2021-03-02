#! usr/bin/python3

"""
Command line Script that mimics a magic eight ball with a NLP twist.

General Steps
 - Waits for question from user
 - Asks user to shake magical eight ball
 - Randomize answer and return answer
 - process question with NLP for important words
 - utilize random answer to form a negative response of search results or positive response of search results. 
 - provide option to open search results, ask another question, or stop

"""

class Eightball:
    """ 
    input is question
    will provide random number and return answer from list of responses
    returns answer with search link
    """
    def __init__(self, question):
        self.question = quesion
        self.randAns = randAns
        self.searchRes = searchRes

    # magic eight ball answer list:
    def answers(randNum):
    return {
        1 : 'It is certain',
        2 : 'My sources say no',
        3 : 'Reply Hazy, Try Again'
    }[randNum]


def main():
    """Looping eightball question"""
    pass

if __name__ = '__main__':
    main()