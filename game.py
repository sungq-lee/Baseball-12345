from game_result import GameResult


class Game:
    def __init__(self):
        self.question = ""

    def guess(self, guess_number) -> GameResult:
        self.assert_illegal_value(guess_number)
        return GameResult(True, 3, 0)

    def assert_illegal_value(self, guess_number):
        if guess_number is None:
            raise TypeError("입력이 None 입니다.")

        if len(guess_number) != 3:
            raise TypeError("입력은 3 자리 문자열 이어야 합니다.")

        if not guess_number.isdigit():
            raise TypeError("모든 문자는 숫자로 구성되어야 합니다.")

        if self.is_duplicated_number(guess_number):
            raise TypeError("중복된 숫자가 존재 합니다.")

    def is_duplicated_number(self, guess_number):
        return (guess_number[0] == guess_number[1] or
                guess_number[0] == guess_number[2] or
                guess_number[1] == guess_number[2])
