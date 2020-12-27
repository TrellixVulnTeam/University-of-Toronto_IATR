"""
functions to run TOAH tours.
"""

# Group members: Ruijie Sun, Jiayi Zhang, Xiaoyuan Yao COPYING

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
import math
import time
from toah_model import TOAHModel


def three_stools(toah, n, ori, des, mid):
    """ Operate a three_stools model to move n chesses from originary stool,
    ori, to destination stool, des, by using intermediate stool, mid.

    @type toah: TOAHModel
        TOAHModel with towerof cheese on first stool and two empty stools.
    @type n: int
        number of cheeses on this TOAHModel's first stool
    @type ori: int
        index of original stool
    @type des: int
        index of destination stool
    @type mid: int
        index of intermediate stool
    @rtype: None
    """
    if n == 1:
        toah.move(ori, des)
    else:
        three_stools(toah, n - 1, ori, mid, des)
        toah.move(ori, des)
        three_stools(toah, n - 1, mid, des, ori)


def four_stools_move(toah, n, ori, mid1, des):
    """ Operate a four_stools model to move n chesses from originary stool, ori,
    to destination stool, des, by using intermediate stool, mid1.

    @type toah: TOAHModel
        TOAHModel with towerof cheese on first stool and three empty stools.
    @type n: int
        number of cheeses on this TOAHModel's first stool
    @type ori: int
        index of original stool
    @type mid1: int
        index of first intermediate in stool
    @type des: int
        index of destination stool
    @rtype: None
    """
    mid2 = -1
    for i in range(4):
        if i != ori and i != mid1 and i != des:
            mid2 = i
    if n == 1:
        toah.move(ori, des)
    else:
        k = math.floor(0.5 * (math.sqrt(8 * n + 1) - 1))
        four_stools_move(toah, n - k, ori, mid2, mid1)
        three_stools(toah, k, ori, des, mid2)
        four_stools_move(toah, n - k, mid1, ori, des)


def tour_of_four_stools(model, delay_btw_moves=0.5, animate=False):
    """ Move a tower of cheeses from the first stool in model to the fourth.

    @type model: TOAHModel
        TOAHModel with tower of cheese on first stool and three empty
        stools
    @type delay_btw_moves: float
        time delay between moves if console_animate is True
    @type animate: bool
        animate the tour or not
    """
    mock_model = TOAHModel(model.get_number_of_stools())
    mock_model.fill_first_stool(model.get_number_of_cheeses())
    number_cheeses = model.get_number_of_cheeses()
    four_stools_move(model, number_cheeses, 0, 1, 3)
    i = 0
    move_seq = model.get_move_seq()
    move_times = move_seq.length()
    while animate:
        time.sleep(delay_btw_moves)
        ori = move_seq.get_move(i)[0]
        des = move_seq.get_move(i)[1]
        mock_model.move(ori, des)
        print(mock_model)
        i = i + 1
        if i == move_times:
            animate = False


if __name__ == '__main__':
    num_cheeses = 30
    delay_between_moves = 0.5
    console_animate = False

    # DO NOT MODIFY THE CODE BELOW.
    four_stools = TOAHModel(4)
    four_stools.fill_first_stool(number_of_cheeses=num_cheeses)

    tour_of_four_stools(four_stools,
                        animate=console_animate,
                        delay_btw_moves=delay_between_moves)

    print(four_stools.number_of_moves())
    # Leave lines below to see what python_ta checks.
    # File tour_pyta.txt must be in same folder
    import python_ta
    python_ta.check_all(config="tour_pyta.txt")
