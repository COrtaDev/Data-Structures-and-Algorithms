// Complete the sortedInsert function below.
/*
 * For your reference:
 *
 * DoublyLinkedListNode {
 *     int data;
 *     DoublyLinkedListNode next;
 *     DoublyLinkedListNode prev;
 * }
 *
 */
function sortedInsert(head, data) {
    let current = head;
    let temp;
    let newNode = new DoublyLinkedListNode(data);
    while (current.data < data) {
        if (!current.next) {
            current.next = newNode;
            newNode.prev = current;
            return head;
        }
        temp = current
        current = current.next;
    }
    if (!temp) {
        newNode.next = current;
        current.prev = newNode;
        return newNode;
    } else {
        temp.next = newNode;
        newNode.prev = temp;
        newNode.next = current;
        current.prev = newNode;
        return head;
    }
}
