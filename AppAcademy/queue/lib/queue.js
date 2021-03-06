// ============================================================================
// Implementation Exercise: Queue
// ============================================================================
//
// -------
// Prompt:
// -------
//
// Implement a Queue and all of its methods below!
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

class Queue {
    constructor() {
        this.front = null;
        this.back = null;
        this.length = 0;
    }
    enqueue(value) {
        let newNode = new Node(value);
        if (!this.length) {
            this.front = newNode;
            this.back = newNode;
        } else {
            // let next = newNode;
            console.log(this.front)
            // this.front.next = this.back;
            // this.back = newNode;
        }
        // console.log(this);
        this.length++;
        return this.length;
    }
    dequeue() {
        if (!this.length) return null;
        let dequeued = this.front;
        if (this.length > 1) {
            let next = this.front.next;
            this.front = next;
        } else {
            this.front = null;
            this.back = null;
        }
        this.length--;
        return dequeued.value;
    }
    size() {
        this.length;
    }
}

exports.Node = Node;
exports.Queue = Queue;
