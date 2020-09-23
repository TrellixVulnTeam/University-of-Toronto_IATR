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
from toah_model_jerry import TOAHModel


def three_stools(toah, n, ori, des, mid):
    if n == 1:
        toah.move(ori, des)
    else:
        three_stools(toah, n - 1, ori, mid, des)
        toah.move(ori, des)
        three_stools(toah, n - 1, mid, des, ori)


def mini_step(i):
    if i == 1:
        return 1
    else:
        k = 1
        step = 2 * mini_step(i - 1) + 1
        for j in range(1, i):
            if 2 * mini_step(i - j) + 2 ** j - 1 > step:
                step = 2 * mini_step(i - j) + 2 ** j - 1
                k = j
        return k

def four_stools(toah, n, ori, des, mid1):
    mid2 = -1
    for i in range(4):
        if i != ori and i != des and i != mid1:
            mid2 = i
    if n == 1:
        toah.move(ori, des)
        return 1
    else:
        k = 1
        step = 2 * four_stools(toah, n - 1, ori, des, mid1) + 1
        for j in range(1, n):
            if 2 * four_stools(toah, n - j, ori, des, mid1) + 2 ** j - 1 < step:
                step = 2 * four_stools(toah, n - j, ori, des, mid1) + 2 ** j - 1
                k = j
        four_stools(toah, n - k, ori, mid1, des)
        three_stools(toah, k, ori, des, mid2)
        four_stools(toah, n - k, mid1, des, ori)
    return step

def tour_of_four_stools(model, delay_btw_moves=0.5, animate=False):
    """Move a tower of cheeses from the first stool in model to the fourth.

    @type model: TOAHModel
        TOAHModel with tower of cheese on first stool and three empty
        stools
    @type delay_btw_moves: float
        time delay between moves if console_animate is True
    @type animate: bool
        animate the tour or not
    """
    pass




if __name__ == '__main__':
    #num_cheeses = 5
    #delay_between_moves = 0.5
    #console_animate = False

    # DO NOT MODIFY THE CODE BELOW.
    #four_stools = TOAHModel(4)
    #four_stools.fill_first_stool(number_of_cheeses=num_cheeses)

    #tour_of_four_stools(four_stools,
                        #animate=console_animate,
                        #delay_btw_moves=delay_between_moves)

    #print(four_stools.number_of_moves())
    # Leave files below to see what python_ta checks.
    # File tour_pyta.txt must be in same folder
    #import python_ta
    #python_ta.check_all(config="tour_pyta.txt")

    new = TOAHModel(3)
    new.fill_first_stool(4)
    model = TOAHModel(3)
    model.fill_first_stool(4)
    three_stools(new, 4, 0, 2, 1)
    seq = new.get_move_seq()
    for item in range(seq.length()):
        ori = seq.get_move(item)[0]
        des = seq.get_move(item)[1]
        model.move(ori, des)
        print(model)

    new_ = TOAHModel(4)
    new_.fill_first_stool(5)
    model_ = TOAHModel(4)
    model_.fill_first_stool(5)
    four_stools(new_, 5, 0, 3, 1)
    seq = new_.get_move_seq()
    for item in range(seq.length()):
        ori = seq.get_move(item)[0]
        des = seq.get_move(item)[1]
        model_.move(ori, des)
        print(model_)
    print(new_.number_of_moves())



