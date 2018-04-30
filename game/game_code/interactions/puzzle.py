from lib import scene


class Puzzle(scene.Scene):
    pass


class MultipleChoice(Puzzle):

    def __init__(self, name, opening_text, correct_answer, wrong_answers, success, failure, **kwargs):
        """
        multiple choice puzzle, has 1 correct answer and the rest are wrong answers
        if you choose the correct answer you go to the success scene, otherwise the failure scene
        :param name: puzzle name
        :param opening_text: puzzle text
        :param correct_answer: the correct answer for the puzzle
        :param wrong_answers: a list of wrong answers
        :param success: correct answer leads here
        :param failure: all wrong answers lead here
        :param kwargs: kwargs for "prompt for choice" default no index
        """
        options = {correct_answer: success}
        for wrong_answer in wrong_answers:
            options[wrong_answer] = failure
        kwargs.setdefault('by_index', False)
        super(MultipleChoice, self).__init__(name, opening_text, options=options, **kwargs)
