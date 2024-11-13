class HumanService:

    def __init__(self):
        self._dna = None
        self._is_mutant = False
        self._identical_sequences = 0
        self._verified_positions = set()

    def _validations(self):
        """
        Validate the DNA
        :return:
        """
        if not all(len(row) == len(self._dna) for row in self._dna):
            raise Exception("DNA must be a square matrix")

    def _can_move_in_direction(self, row, col, equal_sequences, row_size, col_size):
        """
        Check if the sequence can be found in the direction
        :param row (int):
        :param col (int):
        :param equal_sequences (int):
        :param row_size (int):
        :param col_size (int):
        :return:
        """
        can_vertically = row + equal_sequences <= row_size
        can_horizontally = col + equal_sequences <= col_size
        return {
            0: (can_vertically and col - equal_sequences >= -1, 1, -1),
            1: (can_vertically and can_horizontally, 1, 1),
            2: (can_horizontally, 0, 1),
            3: (can_vertically, 1, 0)
        }

    def _check_directional_coincidences(self, row, col, directional_moves, equal_sequences, dna):
        """
        Check the coincidences in the direction
        :param row:
        :param col:
        :param directional_moves:
        :param equal_sequences:
        :param dna:
        :return:
        """
        for i in range(len(directional_moves)):
            x = row
            y = col
            if directional_moves[i][0]:
                if (row, col, i) not in self._verified_positions:
                    col_or_row = col if i == 2 else row
                    range_var = equal_sequences + col_or_row
                    coincidences = 0
                    positions = []
                    for j in range(col_or_row, range_var):
                        next_position = dna[x][y]
                        x += directional_moves[i][1]
                        y += directional_moves[i][2]
                        if dna[row][col] == next_position:
                            coincidences += 1
                            positions.append((x, y, i))
                        else:
                            break
                    if coincidences == equal_sequences:
                        self._identical_sequences += 1
                        self._verified_positions.update(positions)

    def is_mutant(self, dna, equal_sequences=4):
        """
        Check if the DNA is from a mutant
        :param dna:
        :param equal_sequences:
        :return:
        """
        self._dna = dna
        self._validations()
        row_size = len(dna)
        col_size = len(dna[0])

        for row in range(row_size):
            for col in range(col_size):
                directional_moves = self._can_move_in_direction(row, col, equal_sequences, row_size, col_size)
                self._check_directional_coincidences(row, col, directional_moves, equal_sequences, dna)
        print(self._identical_sequences)
        self._is_mutant = self._identical_sequences >= 2
        return self._is_mutant