"""
functions to run TOAH tours.
"""


# Copyright 2013, 2014, 2017 Gary Baumgartner, Danny Heap, Dustin Wehr,
# Bogdan Simion, Jacqueline Smith, Dan Zingaro
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
# Copyright 2013, 2014 Gary Baumgartner, Danny Heap, Dustin Wehr


# you may want to use time.sleep(delay_between_moves) in your
# solution for 'if __name__ == "main":'
import time
import math
from toah_model_jerry import TOAHModel

def tour_of_three_stools(model, n, from_stool, mid_stool, dest_stool):
    if n == 0:
        pass
        #model.move(from_stool, dest_stool)
    else:
        tour_of_three_stools(model, n - 1, from_stool, dest_stool, mid_stool)

        model.move(from_stool, dest_stool)

        tour_of_three_stools(model, n - 1, mid_stool, from_stool, dest_stool)

#def find_mini_k(n):
#    """"""
#    i = 1
#    k = 0
#    for i in range(n+1):
#        min = min = 10000000000
#        for k in range(1, i + 1)



def tour_of_four_stools(model, n, from_stool, fir_stool, sec_stool, dest_stool):
    """Move a tower of cheeses from the first stool in model to the fourth.

    @type model: TOAHModel
        TOAHModel with tower of cheese on first stool and three empty
        stools
    @type delay_btw_moves: float
        time delay between moves if console_animate is True
    @type animate: bool
        animate the tour or not
    """
    if n == 1:
        model.move(from_stool, dest_stool)

    else:
        k = math.floor(0.5 * (math.sqrt(8 * n + 1) - 1))

        tour_of_four_stools(model, n - k, from_stool, sec_stool, dest_stool, fir_stool)

        tour_of_three_stools(model, k, from_stool, sec_stool, dest_stool)

        tour_of_four_stools(model, n - k, fir_stool, from_stool, sec_stool, dest_stool)















if __name__ == '__main__':
    num_cheeses = 8
    delay_between_moves = 0.5
    console_animate = False

    # DO NOT MODIFY THE CODE BELOW.
    four_stools = TOAHModel(4)
    four_stools.fill_first_stool(num_cheeses)


    tour_of_four_stools(four_stools, num_cheeses, 0, 1, 2, 3)


    print(four_stools.number_of_moves())
    print(four_stools.get_move_seq()._moves)
    # Leave files below to see what python_ta checks.
    # File tour_pyta.txt must be in same folder
    import python_ta
    python_ta.check_all(config="tour_pyta.txt")
