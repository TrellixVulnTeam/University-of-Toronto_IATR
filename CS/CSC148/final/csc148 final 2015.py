class Tune:

    def __init__(self, title, artist, length):
        """ Initialize this Tune.

        @type self: Tune
        @type title: str
        @type artist: str
        @type length: int
        @rtype: None
        """

        self.title = title
        self.artist = artist
        self.length = length
        self._record = []

    def play(self, user_email):
        """ Record this user played this tune.

        @type self: Tune
        @type user_email: str
        @rtype: None
        """

        self._record.append(user_email)

    def plays_by(self,user_email):
        """ Return the number of time that this user with this email
        has played the Tune.

        @type self: Tune
        @type user_email: str
        @rtype: int
        """

        result = 0
        for email in self._record:
            if email == user_email:
                result += 1
        return result

class Playlist:

    def __init__(self):
        """ Initialize this playlist.

        @type self: Playlist
        @rtype: None
        """

        self.tunes_list = []

    def add_tune(self, tune):
        """ Add a tune to this playlist's tunes_list.

        @type self: Playlist
        @type tune: Tune
        @rtype: None
        """

        self.tunes_list.append(tune)

    def play(self, n, user_email):
        """ Record this user play the first n Tunes in this playlist's Tunes list.
        If n is larger than length of this playlist's tunes list, then record all
        the tune list.

        @type self: Playlist
        @type n: int
        @type user_email: str
        @rtype: None
        """
        i = 0
        while i < n and i < len(self.tunes_list):
            self.tunes_list[i].play(user_email)
            i += 1

    def total_time_played(self, user_email):
        """ Return the total time played by this user.

        @type self: Playlist
        @type user_email: str
        @rtype: None
        """

        acc = 0
        for tune in self.tunes_list:
            acc += tune.plays_by(user_email) * tune.length

        return acc


# Question 2
def occur(root, s):
    """ Return whether or not s equals to a path from root to leave.

    @type root: BTNode | None
    @type s: str
    @rtype: bool
    """

    paths_list = all_paths(root)
    return s in paths_list


def all_paths(root):
    """ Return all the the path from this root to leaves.

    @type root: BTNode | None
    @rtype: list
    """

    # Since it's an example on the review session. the comment is simplified.
    # Base case:
    if not root:
        return []

    # Base case2:
    if root.right is None and root.left is None:
        return [root.data]
    else:
        acc = []
        # recursive step:
        for c in [root.left, root.right]:
            for path in all_paths(c):
                acc.append(str(root.data) + path)
        return acc


# Question 3

def TPBT(root):
    """ Return a tuple containing: (1) the heighest perfect binary tree within the
    tree root. (2) whether this perfect binary tree root at root itself.

    @type root: BTNode
    @rtype: tuple
    """
    # Base case1: root is None.
    if not root:
        return tuple(0, True)
    # Base case2: a perfect binary tree with no children.
    if not (root.left and root.right):
        return tuple(1, True)
    # Base case3: a non-perfect binary tree with single children.
    elif not root.left or not root.right:
        return tuple(0, False)

    # Recursive step:
    else:
        right = TPBT(root.right)
        left = TPBT(root.left)

        # find the max height of the perfect binary tree of left and right
        max_ = max(right[0], left[0])

        # flag is False first
        flag = False

        # If this root's left and right are all perfect binary tree
        # and their height are equal
        # then this root is a perfect binary tree, make flag into True.
        if right == left:

            # this root is also a perfect binary tree.
            # the height plus one.
            max_ += 1
            flag = True
        return tuple(max_, flag)


# Question 4
# Assume that we already has a class Stack.
class Stack:
    def __init__(self):
        self.items = []

    def add(self, item):
        self.items.append(item)

    def remove(self):
        self.items.pop()

    def is_empty(self):
        return self.items == []

def unique_paths(t):
    """
    """

    acc = set()
    stack_ = Stack()
    stack_.add(t)
    while not stack_.is_empty():
        temp = stack_.remove()
        if not id(temp) in acc:
            acc.add(id(temp))
        else:
            return False

        for c in temp.children:
            stack_.add(c)

    return True


# Question 5

class LLNode():

    def __init__(self, value, next):
        """ Initialize this Linkedlist.
        """

        self.value = value
        self.next = next

# function version. actually you could do it without using function.

def reverse_two(lnk, p):
    """
    """

    if p.next and p.next.next:  # There's two nodes after p
        pointer = p.next
        p.next = pointer.next
        pointer2 = pointer.next.next
        pointer.next.next = pointer
        pointer.next = pointer2

reverse_two(lnk, p)
# function version.  actually you could do it without using function.

def copy_after(lnk, p):

    if p.next:
        new_node = LLNode(p.next.value)
        pointer = p.next.next
        p.next = new_node
        new_node.next = pointer

copy_after(lnk, p)

# Question 6


class Queue:

    def __init__(self ,value , nxt):
        """
        """

        self._front, self._back = None

    def enqueue(self, c):
        """
        """

        new_node = LLNode(c)
        if self._back:
            self._back.nxt = new_node
            self._back = new_node
        else:
            self._back = self._front = new_node

    def dequeue(self):
        """
        """

        new_value = self._front.value
        self._front = self._front.next
        return new_value

    def is_empty(self):
        """
        """

        return self._front == None


class LeakyQueue(Queue):

    def defer(self, from_value, to_value):
        """
        """

        temp = self._front  # A pointer

        while temp and temp.value != from_value:  # First, we need to find the value equal
            # to from_value.
            temp = temp.next

        temp2 = temp
        while temp2.next and temp2.next.value != to_value:  # Second, we need to find the value equal
            # to to_value.
            # we need to find the node just before the to_value in order to make a delete.
            temp2 = temp2.next

        if temp2:  # If this value exist.
            temp.value = temp2.next.value
            temp2.next = temp2.next.next
        else:
            pass  # Do nothing if there's no such a temp2.

# Question7
# this is about the assignment so omited here.

# (a)
# O(log(n))

# (b)
# O(n)
# i loop n iterations
# j loop log(n) iterations
# However, j loop only run during the first iteration of i loop
# so just list n + log(n)
# which we consider as O(n)
# notice that if there's a j = 0 in the outer loop
# the running time would be O(n * log(n))

# (c)
# O(n^3)

# (d)
# O(n)

