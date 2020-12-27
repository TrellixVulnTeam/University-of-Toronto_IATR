"""
ConsoleController: User interface for manually solving
Anne Hoy's problems from the console.
"""

# Group members: Ruijie Sun, Jiayi Zhang, Xiaoyuan Yao COPYING

# Copyright 2014, 2017 Dustin Wehr, Danny Heap, Bogdan Simion,
# Jacqueline Smith, Dan Zingaro
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


from toah_model import TOAHModel, IllegalMoveError


def move(model, origin, dest):
    """ Apply move from origin to destination in model.

    May raise an IllegalMoveError.

    @param TOAHModel model:
        model to modify
    @param int origin:
        stool number (index from 0) of cheese to move
    @param int dest:
        stool number you want to move cheese to
    @rtype: None
    """
    model.move(origin, dest)


class ConsoleController:
    """ Controller for text console.
    """

    def __init__(self, number_of_cheeses, number_of_stools):
        """ Initialize a new ConsoleController self.

        @param ConsoleController self: the ConsoleController itself
        @param int number_of_cheeses: the number of cheeses
        @param int number_of_stools: the number of stools
        @rtype: None
        """
        self.model = TOAHModel(number_of_stools)
        self.model.fill_first_stool(number_of_cheeses)

    def play_loop(self):
        """ Play Console-based game.

        @param ConsoleController self: the ConsoleController itself
        @rtype: None

        TODO:
        -Start by giving instructions about how to enter moves (which is up to
        you). Be sure to provide some way of exiting the game, and indicate
        that in the instructions.
        -Use python's built-in function input() to read a potential move from
        the user/player. You should print an error message if the input does
        not meet the spe instruction or if it denotes
        an invalid move (e.g. moving a cheese ontcifications given in youro a
        smaller cheese).
        You can print error messages from this method and/or from
        ConsoleController.move; it's up to you.
        -After each valid move, use the method TOAHModel.__str__ that we've
        provided to print a representation of the current state of the game.
        """
        print("""
               --------Welcome to the Game of Hanoi--------
        Type two integers like x y (two integers x and y seperated by a space)
        to move a cheese from xth stool to yth stool. If the input move is
        invalid, an error message will be sent until you type a valid move.
        NO.{} represent the number of successful moves you have made.
        Type quit to exit the game.
              """)
        move_order = input('Please order a move or type quit to exit the game:')
        n = self.model.get_number_of_stools()
        while move_order != 'quit':
            try:
                from_stool = int(move_order.split()[0]) - 1
                dest_stool = int(move_order.split()[1]) - 1
                if len(move_order.split()) != 2:
                    print("Hey, dude! Please follow the format!")
                elif from_stool == -1 or dest_stool == -1:
                    print("Hey, dude! We don't have that stool!")
                else:
                    move(self.model, from_stool, dest_stool)

            except IndexError:
                if len(move_order.split()) != 2:
                    print("Hey, dude! Please follow the format!")
                elif from_stool + 1 > n or dest_stool + 1 > n:
                    print("Hey, dude! We don't have that stool")
                else:
                    print("Hey, dude! Please follow the format!")
            except IllegalMoveError:
                if from_stool == dest_stool:
                    print("Hey, dude! Origin and destination stools must "
                          "be distinct!")
                elif self.model.get_top_cheese(from_stool) is None:
                    print("Hey, dude! Can't find a cheese from an empty stool!")
                elif self.model.get_top_cheese(from_stool).size > self.model\
                        .get_top_cheese(dest_stool).size:
                    print('Hey, dude! A big cheese can not be on a small one!')
            except ValueError:
                print("Hey, dude! Don't type other characters!")

            print(self.model)
            move_order = input('NO.{} Give me a move:'.
                               format(self.model.number_of_moves()))

if __name__ == '__main__':
    # TODO:
    # You should initiate game play here. Your game should be playable by
    # running this file.
    new_game = ConsoleController(5, 4)
    new_game.play_loop()
    # Leave lines below as they are, so you will know what python_ta checks.
    # You will need consolecontroller_pyta.txt in the same folder.
    import python_ta
    python_ta.check_all(config="consolecontroller_pyta.txt")
