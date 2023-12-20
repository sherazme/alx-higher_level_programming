#!/usr/bin/python3
""" Node Class """


class Node:
    """ Node class define a node of a singly linked list

    Attributes:
        data (int): Data of the node.
        next_node (Node): Next node in the list.
    """

    def __init__(self, data, next_node=None):
        """ Initialize a new Node

        Args:
          data (int): Data of the node.
          next_node (Node): Next node on the list.

        Raises:
           If data is not an integer: raise a TypeError exception with
              the message data must be an integer.
           If next_node is not a Node or None: raise a TypeError exception with
              the message next_node must be a Node object.
        """
        if isinstance(data, int):
            self.__data = data
        else:
            raise TypeError("data must be an integer")

        if next_node is None or isinstance(next_node, Node):
            self.__next_node = next_node
        else:
            raise TypeError("next_node must be a Node object")

    # data
    @property
    def data(self):
        """ Retrive the data of the node """
        return (self.__data)

    @data.setter
    def data(self, value):
        """ Set the data of the node """
        if isinstance(value, int):
            self.__data = value
        else:
            raise TypeError("data must be an integer")

    # next_node
    @property
    def next_node(self):
        """ Retrive the next_node """
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


""" SinglyLinkedList Class """


class SinglyLinkedList:
    """ Class SinglyLinkedList

    Atrributes:
        Head (Node): Head of the list.
    """

    def __init__(self):
        """ Initialise an empty Sinlgy Linked List """
        self.head = None

    def is_empty(self):
        """ Check if a Singly Linked List is empty or not

        Returns:
           True if the list is empty, False otherwise.
        """
        return (self.head is None)

    def sorted_insert(self, value):
        """ Insert a node in a sorted way

        Args:
          value (int): Value of the node to insert.
        """
        new = Node(value)

        # Insert at the begining of the list
        if self.is_empty() or self.head.data > value:
            new.next_node = self.head
            self.head = new

        # Insert in the list
        else:
            current = self.head
            while (current.next_node is not None and
                   current.next_node.data < value):
                current = current.next_node
            new.next_node = current.next_node
            current.next_node = new

    def __str__(self):
        """ Return a string representation of the singli linked lits """
        elements = []
        current = self.head
        while current is not None:
            elements.append(str(current.data))
            current = current.next_node
        return "\n".join(elements)
