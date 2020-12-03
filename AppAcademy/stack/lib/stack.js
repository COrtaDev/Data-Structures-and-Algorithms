// ============================================================================
// Implementation Exercise: Stack
// ============================================================================
//
// -------
// Prompt:
// -------
//
// Implement a Stack and all of its methods below!
//
// ------------
// Constraints:
// ------------
//
// Make sure the time and space complexity of each is equivalent to those
// in the table provided in the Time and Space Complexity Analysis section
// of your Stack reading!
//
// -----------
// Let's Code!
// -----------

class Node {
    constructor(value) {
        this.value = value;
        this.next = null;
    }
}

class Stack {
    constructor() {
        this.top = null;
        this.length = 0;
    }

    push(value) {
        let newNode = new Node(value);
        if (!this.length) {
            this.top = newNode;
        } else {
            let next = this.top;
            newNode.next = next;
            this.top = newNode;
        }
        this.length++;
        return this.length;
    }

    pop() {
        if (!this.length) return null;
        let popped = this.top;
        if (this.length > 1) {
            // console.log(popped.next)
            this.top = popped.next;
        } else {
            this.top = null;
        }
        // console.log(this);
        this.length--;
        return popped.value;
    }

    size() {
        return this.length;
    }
}

exports.Node = Node;
exports.Stack = Stack;
