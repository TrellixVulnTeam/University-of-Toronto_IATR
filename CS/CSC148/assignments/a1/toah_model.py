"""
TOAHModel:  Model a game of Tour of Anne Hoy
Cheese:   Model a cheese with a given (relative) size
IllegalMoveError: Type of exceptions thrown when an illegal move is attempted
MoveSequence: Record of a sequence of (not necessarily legal) moves. You will
need to return MoveSequence object after solving an instance of the 4-stool
Tour of Anne Hoy game, and we will use that to check the correctness of your
algorithm.
"""

# Group members: Ruijie Sun, Jiayi Zhang, Xiaoyuan Yao COPYING

# Copyright 2013, 2014, 2017 Gary Baumgartner, Danny Heap, Dustin Wehr,
# Bogdan Simion, Jacqueline Smith, Dan Zingaro, Ritu Chaturvedi, Samar Sabie
# Distributed under the terms of the GNU General Public License.
#
# This file is part of Assignment 1, CSC148, Winter 2017.
#
# This is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This file is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this file.  If not, see <http://www.gnu.org/licenses/>.
#


class TOAHModel:
    """ Model a game of Tour Of Anne Hoy.

    Model stools holding stacks of cheese, enforcing the constraint
    that a larger cheese may not be placed on a smaller one.
    """

    def __init__(self, number_of_stools):
        """ Create new TOAHModel with empty stools to hold stools of cheese.

        @param TOAHModel self: a new TOAHModel
        @param int number_of_stools: the number of stools
        @rtype: None

        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> (M.get_number_of_stools(), M.number_of_moves()) == (4,0)
        True
        >>> M.get_number_of_cheeses()
        5
        """
        self.trace = []
        self._move_seq = MoveSequence([])
        self._stools = [[] for i in range(number_of_stools)]

    def get_move_seq(self):
        """ Return the move sequence

        @param TOAHModel self: the TOAHModel itself
        @rtype: MoveSequence

        >>> toah = TOAHModel(2)
        >>> toah.get_move_seq() == MoveSequence([])
        True
        """
        return self._move_seq

    def __eq__(self, other):
        """ Return whether TOAHModel self is equivalent to other.

        Two TOAHModels are equivalent if their current
        configurations of cheeses on stools look the same.
        More precisely, for all h,s, the h-th cheese on the s-th
        stool of self should be equivalent the h-th cheese on the s-th
        stool of other

        @param TOAHModel self: a TOAHModel self
        @param TOAHModel other: a TOAHModel other
        @rtype: bool

        >>> m1 = TOAHModel(4)
        >>> m1.fill_first_stool(7)
        >>> m1.move(0, 1)
        >>> m1.move(0, 2)
        >>> m1.move(1, 2)
        >>> m2 = TOAHModel(4)
        >>> m2.fill_first_stool(7)
        >>> m2.move(0, 3)
        >>> m2.move(0, 2)
        >>> m2.move(3, 2)
        >>> m1 == m2
        True
        """
        if len(self._stools) != len(other._stools):
            return False
        for i in range(len(self._stools)):
            if len(self._stools[i]) != len(other._stools[i]):
                return False
            for j in range(len(self._stools[i])):
                if self._cheese_at(i, j) != other._cheese_at(i, j):
                    return False
        return True

    def _cheese_at(self, stool_index, stool_height):
        # """ Return (stool_height)th from stool_index stool, if possible.
        #
        # @type self: TOAHModel
        # @type stool_index: int
        # @type stool_height: int
        # @rtype: Cheese | None
        #
        # >>> M = TOAHModel(4)
        # >>> M.fill_first_stool(5)
        # >>> M._cheese_at(0,3).size
        # 2
        # >>> M._cheese_at(0,0).size
        # 5
        # """
        if 0 <= stool_height < len(self._stools[stool_index]):
            return self._stools[stool_index][stool_height]
        else:
            return None

    def __str__(self):
        """ Depicts only the current state of the stools and cheese.

        @param TOAHModel self: the TOAHModel itself
        @rtype: str
        """
        all_cheeses = []
        for height in range(self.get_number_of_cheeses()):
            for stool in range(self.get_number_of_stools()):
                if self._cheese_at(stool, height) is not None:
                    all_cheeses.append(self._cheese_at(stool, height))
        max_cheese_size = max([c.size for c in all_cheeses]) \
            if len(all_cheeses) > 0 else 0
        stool_str = "=" * (2 * max_cheese_size + 1)
        stool_spacing = "  "
        stools_str = (stool_str + stool_spacing) * self.get_number_of_stools()

        def _cheese_str(size):
            # helper for string representation of cheese
            if size == 0:
                return " " * len(stool_str)
            cheese_part = "-" + "--" * (size - 1)
            space_filler = " " * int((len(stool_str) - len(cheese_part)) / 2)
            return space_filler + cheese_part + space_filler

        lines = ""
        for height in range(self.get_number_of_cheeses() - 1, -1, -1):
            line = ""
            for stool in range(self.get_number_of_stools()):
                c = self._cheese_at(stool, height)
                if isinstance(c, Cheese):
                    s = _cheese_str(int(c.size))
                else:
                    s = _cheese_str(0)
                line += s + stool_spacing
            lines += line + "\n"
        lines += stools_str

        return lines

    def fill_first_stool(self, number_of_cheeses):
        """ Add number of cheeses, number_of_cheeses, to the first stool,
        the cheese adds in in an order from larger size(larger diameter) at the
        bottom to smaller size on the top.

        @param TOAHModel self: the TOAHModel itself
        @param int number_of_cheeses: the number of cheeses
        @rtype: None

        >>> M = TOAHModel(4)
        >>> M.fill_first_stool(5)
        >>> M._stools[0] == [Cheese(5), Cheese(4), Cheese(3), Cheese(2), \
        Cheese(1)]
        True
        """
        for i in range(number_of_cheeses, 0, -1):
            self._stools[0].append(Cheese(i))

    def get_number_of_stools(self):
        """ Return the number of stools in the TOAHModel.
        @param TOAHModel self: the TOAHModel itself
        @rtype: int
        >>> new_toah = TOAHModel(5)
        >>> new_toah.get_number_of_stools()
        5
        """
        return len(self._stools)

    def get_number_of_cheeses(self):
        """ Return the total number of cheese inside the TOAHModel.

        @param TOAHModel self: the TOAHModel itself
        @rtype: int

        >>> new_toah = TOAHModel(5)
        >>> new_toah.fill_first_stool(6)
        >>> new_toah.get_number_of_cheeses()
        6
        """
        return sum([len(stool) for stool in self._stools])

    def add(self, cheese_add, s_index):
        """ Add cheese, cheese_add, to indicated stool represented by s_index,
        add the cheese iff the top cheese's size at the indicated stool is less
        than the cheese, cheese_add, that we are going add, or the indicated
        stool is empty, otherwise, raise exception.

        @param TOAHModel self: the TOAHModel itself
        @param Cheese cheese_add: the cheese object to add
        @param int s_index: the index of a specific stool
        @rtype: None

        >>> new_toah = TOAHModel(5)
        >>> new_toah.fill_first_stool(6)
        >>> new_toah.add(Cheese(1), 2)
        >>> new_toah.get_cheese_location(Cheese(1))
        2
        """
        if len(self._stools[s_index]) == 0 or cheese_add.size < \
                self._stools[s_index][-1].size:
            self._stools[s_index].append(cheese_add)
        else:
            raise IllegalMoveError()

    def get_cheese_location(self, cheese):
        """ Return the index of the stool where the cheese is located in the
        TOAHModel self.

        @param TOAHModel self: the TOAHModel
        @param Cheese cheese: the cheese that you want to find the location
        @rtype: int

        >>> new_toah = TOAHModel(5)
        >>> new_toah.fill_first_stool(6)
        >>> new_toah.add(Cheese(1), 2)
        >>> new_toah.get_cheese_location(Cheese(1))
        2
        """
        s_index = -1
        for index in range(len(self._stools)):
            if cheese in self._stools[index]:
                s_index = index
        if s_index == -1:
            raise CheeseNotFoundError()
        else:
            return s_index

    def get_top_cheese(self, stool_index):
        """ Return the Cheese object based on the stool_index in the TOAHModel
        self.

        @param TOAHModel self: the TOAHModel itself
        @param int stool_index: the index of stool
        @rtype: Cheese
        """
        if len(self._stools[stool_index]) == 0:
            return None
        else:
            return self._stools[stool_index][-1]

    def move(self, from_stool, dest_stool):
        """ Move cheese from from_stool to dest_stool iff the cheese size is
        less than dest_stool's top Cheese'size or the dest_stool is a empty
        stool, otherwise raise IllegalMoveError.

        @param TOAHModel self: the TOAHModel itself
        @param int from_stool: the index of the from_stool
        @param int dest_stool: the index of the dest_stool
        @rtype: None

        >>> new_toah = TOAHModel(5)
        >>> new_toah.fill_first_stool(6)
        >>> new_toah.move(0, 1)
        >>> new_toah.get_top_cheese(0).size
        2
        """
        if len(self._stools[from_stool]) != 0:
            top_cheese = self.get_top_cheese(from_stool)
            self.add(top_cheese, dest_stool)
            self._stools[from_stool].remove(top_cheese)
            self._move_seq.add_move(from_stool, dest_stool)
        else:
            raise IllegalMoveError()

    def number_of_moves(self):
        """ Return the number of moves of the TOAHModel self.

        @parm TOAHModel self: the TOAHself itself
        @rtype: int

        >>> new_toah = TOAHModel(5)
        >>> new_toah.fill_first_stool(6)
        >>> new_toah.move(0, 1)
        >>> new_toah.move(0, 2)
        >>> new_toah.number_of_moves()
        2
        """
        return self._move_seq.length()


class Cheese:
    """ A cheese for stacking in a TOAHModel

    === Attributes ===
    @param int size: width of cheese
    """

    def __init__(self, size):
        """ Initialize a Cheese to diameter size.

        @param Cheese self: The Cheese itself
        @param int size: Cheese size
        @rtype: None

        >>> c = Cheese(3)
        >>> isinstance(c, Cheese)
        True
        >>> c.size
        3
        """
        self.size = size

    def __eq__(self, other):
        """ Is self equivalent to other?

        We say they are if they're the same
        size.

        @param Cheese self: The Cheese itself
        @param Cheese|Any other: Other Cheese
        @rtype: bool

        >>> c1 = Cheese(3)
        >>> c2 = Cheese(4)
        >>> c3 = Cheese(3)
        >>> c1 == c2
        False
        >>> c1 == c3
        True
        """
        return type(self) == type(other) and self.size == other.size


class IllegalMoveError(Exception):
    """ Exception indicating move that violate TOAHModel
    """
    pass


class CheeseNotFoundError(Exception):
    """Exception indicating that the cheese is not in the TOAHModel
    """
    pass


class MoveSequence(object):
    """ Sequence of moves in TOAH game
    """

    def __init__(self, moves):
        """ Create a new MoveSequence self.

        @param MoveSequence self: The MoveSequence itself
        @param list[tuple[int]] moves: move record
        @rtype: None

        >>> ms = MoveSequence([(1, 2)])
        >>> ms._moves == [(1, 2)]
        True
        """
        self._moves = moves

    def get_move(self, i):
        """ Return the move at position i in self

        @param MoveSequence self: The MoveSequence itself
        @param int i: The i th move
        @rtype: tuple[int]

        >>> ms = MoveSequence([(1, 2)])
        >>> ms.get_move(0) == (1, 2)
        True
        """
        return self._moves[i]

    def add_move(self, src_stool, dest_stool):
        """ Add move from src_stool to dest_stool to MoveSequence self.

        @param MoveSequence self: The MoveSequence itself
        @param int src_stool: the source stool
        @param int dest_stool: the destination stool
        @rtype: None

        >>> ms = MoveSequence([(1, 2)])
        >>> ms.add_move(3, 4)
        >>> ms.get_move(1) == (3, 4)
        True
        """
        self._moves.append((src_stool, dest_stool))

    def length(self):
        """ Return number of moves in self.

        @param MoveSequence self: The MoveSequence itself
        @rtype: int

        >>> ms = MoveSequence([(1, 2)])
        >>> ms.length()
        1
        """
        return len(self._moves)

    def generate_toah_model(self, number_of_stools, number_of_cheeses):
        """ Construct TOAHModel from number_of_stools and number_of_cheeses
        after moves in self.

        Takes the two parameters for
        the game (number_of_cheeses, number_of_stools), initializes the game
        in the standard way with TOAHModel.fill_first_stool(number_of_cheeses),
        and then applies each of the moves in this move sequence.

        @param MoveSequence self: The MoveSequence itself
        @param int number_of_stools: the number of stools
        @param int number_of_cheeses: the number of cheeses
        @rtype: TOAHModel

        >>> ms = MoveSequence([])
        >>> toah = TOAHModel(2)
        >>> toah.fill_first_stool(2)
        >>> toah == ms.generate_toah_model(2, 2)
        True
        """
        model = TOAHModel(number_of_stools)
        model.fill_first_stool(number_of_cheeses)
        for move in self._moves:
            model.move(move[0], move[1])
        return model


if __name__ == '__main__':
    #    import doctest
    #    doctest.testmod(verbose=True)
    # Leave lines below to see what python_ta checks.
    # File toahmodel_pyta.txt must be in same folder.
    import python_ta
    python_ta.check_all(config="toahmodel_pyta.txt")
