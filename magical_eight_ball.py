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

from random import randrange

class Eightball:
    """ 
    input is question
    will provide random number and return answer from list of responses
    returns answer with search link
    """
    
    def __init__(self, question):
        self.question = question
        self.randAns = self.answer(self.random_number())
        self.search_res = 'searchRes text'

    def random_number(self):
        return randrange(1,21)

    def answer(self, random_number):
        """
        Dict to contain answers. each answer has a 'score' which indicates a postive or negative answer. 5 is a postive answer, 1 is negative, 3 is unsure. this score will determine the whether the search result is worded.
        """
        return {
            1:('As I see it, yes.', 5),
            2:('Ask again later.', 3),
            3:('Better not tell you now.', 3),
            4:('Cannot predict now.', 3),
            5:('Concentrate and ask again.', 3),
            6:('Don’t count on it.', 1),
            7:('It is certain.', 5),
            8:('It is decidedly so.', 5),      
            9:('Most likely.', 5),
            10:('My reply is no.', 1),
            11:('My sources say no.', 1),
            12:('Outlook not so good.', 1),
            13:('Outlook good.', 5),
            14:('Reply hazy, try again.', 3),
            15:('Signs point to yes.', 5),
            16:('Very doubtful.', 1),
            17:('Without a doubt.', 5),
            18:('Yes.', 5),
            19:('Yes – definitely.', 5),
            20:('You may rely on it.', 5)
        }[random_number]

    def search_results():
        pass


def main():
    """Looping eightball question"""
    print("Please ask the magical eight ball a question:")
    # question = input("")
    # answer = Eightball(question)
    pass

if __name__ == '__main__':
    main()