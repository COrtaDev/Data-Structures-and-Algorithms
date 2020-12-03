// ============================================================================
// Implementation Exercise: Singly Linked List
// ============================================================================
//
// -------
// Prompt:
// -------
//
// Implement a Singly Linked List and all of its methods below!
//
// ------------
// Constraints:
// ------------
//
// Make sure the time and space complexity of each is equivalent to those
// in the table provided in the Time and Space Complexity Analysis section
// of your Linked List reading!
//
// -----------
// Let's Code!
// -----------

// TODO: Implement a Linked List Node class here
class Node {
    constructor(val) {
        this.value = val;
        this.next = null;
    }

}

// TODO: Implement a Singly Linked List class here
class LinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    // TODO: Implement the addToTail method here
    addToTail(val) {
        // we create a newNode
        let newNode = new Node(val);
        // we set up a condition to check to see if this will be the first node based on the value of this.head
        // if this.head is falsey (aka: we have an empty list...), we assign the newNode to be this.head
        if (!this.head) this.head = newNode;
        // otherwise, we set the next property of the current tail node to the new node...
        else this.tail.next = newNode;
        // ...and we reassign the current tail to be new node as well.
        this.tail = newNode;
        // increment the length since this method 'adds' to the length of the list...
        this.length++;
        //... and finally, return this object. (In the demoList.js file, this is the object called myList.)
        return this;
    }

    // TODO: Implement the removeTail method here
    removeTail() {
        if (!this.head) return undefined;
        // to get there, we must iterate through the list, starting at the head.
        // the variable 'current' points to our position in the list and is initially the head of the list.
        let currentNode = this.head;
        // the new tail will be the node for which the next property of it's next property evaluates falsey...
        // to get find it, we loop while the current node's next property evalutates truthy.
        let newTail;
        while (currentNode.next) {
            newTail = currentNode;
            currentNode = currentNode.next;
            // once we reach the node for which the next property evaluates falsey, we exit the loop.
        }
        // we reassign this.tail to be the node right before we found the node who's next was falsey...
        this.tail = newTail;
        // shorten the length of the list since we have removed a node from it.
        this.length--;
        // set up a condition to check to see if our list is empty by checking to see if the length is falsey
        if (!this.length) {
            // if it is empty, change the values of the head and tail to be null, its initial state.
            this.head = null;
            this.tail = null;
        } else {
            //otherwise we should net the value of the node at the tail to be null, since it is the tail now...
            this.tail.next = null;
        }
        //finally, we return the node we assigned to current node, back when we were looking for node who's next property had a falsey value.
        return currentNode;
    }

    // TODO: Implement the addToHead method here
    addToHead(val) {

    }

    // TODO: Implement the removeHead method here
    removeHead() {

    }

    // TODO: Implement the contains method here
    contains(target) {

    }

    // TODO: Implement the get method here
    get(index) {

    }

    // TODO: Implement the set method here
    set(index, val) {

    }

    // TODO: Implement the insert method here
    insert(index, val) {

    }

    // TODO: Implement the remove method here
    remove(index) {

    }

    // TODO: Implement the size method here
    size() {

    }
}

exports.Node = Node;
exports.LinkedList = LinkedList;


/*
~~~this is the solution from a/A:~~~
|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|
class Node {
    constructor(val) {
        this.value = val;
        this.next = null;
    }
}

class LinkedList {
    constructor() {
        this.head = null;
        this.tail = null;
        this.length = 0;
    }

    addToTail(val) {
        const newNode = new Node(val);

        if (!this.head) {
            this.head = newNode;
        } else {
            this.tail.next = newNode;
        }

        this.tail = newNode;
        this.length++;
        return this;
    }

    removeTail() {
        if (!this.head) return undefined;
        let current = this.head;
        let newTail = current;
        while (current.next) {
            newTail = current;
            current = current.next;
        }
        this.tail = newTail;
        this.tail.next = null;
        this.length--;
        if (this.length === 0) {
            this.head = null;
            this.tail = null;
        }
        return current;
    }

    addToHead(val) {
        let newNode = new Node(val);
        if (!this.head) {
            this.head = newNode;
            this.tail = newNode;
        } else {
            newNode.next = this.head;
            this.head = newNode;
        }
        this.length++;
        return this;
    }

    removeHead() {
        if (!this.head) return undefined;
        const currentHead = this.head;
        this.head = currentHead.next;
        this.length--;
        if (this.length === 0) {
            this.tail = null;
        }
        return currentHead;
    }

    contains(target) {
        let node = this.head;
        while (node) {
            if (node.value === target) return true;
            node = node.next;
        }
        return false;
    }

    get(index) {
        if (index < 0 || index >= this.length) return null;
        let counter = 0;
        let current = this.head;
        while (counter !== index) {
            current = current.next;
            counter++;
        }
        return current;
    }

    set(index, val) {
        const foundNode = this.get(index);
        if (foundNode) {
            foundNode.value = val;
            return true;
        }
        return false;
    }

    insert(index, val) {
        if (index < 0 || index >= this.length) return false;
        if (index === this.length) return !!this.addToTail(val);
        if (index === 0) return !!this.addToHead(val);

        const newNode = new Node(val);
        const prev = this.get(index - 1);
        const temp = prev.next;
        prev.next = newNode;
        newNode.next = temp;
        this.length++;
        return true;
    }

    remove(index) {
        if (index < 0 || index >= this.length) return undefined;
        if (index === 0) return this.removeHead();
        if (index === this.length - 1) return this.removeTail();
        const previousNode = this.get(index - 1);
        const removed = previousNode.next;
        previousNode.next = removed.next;
        this.length--;
        return removed;
    }

    size() {
        return this.length;
    }
}

exports.Node = Node;
exports.LinkedList = LinkedList;
*/
