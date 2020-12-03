// Complete the insertNodeAtPosition function below.
/*
 * For your reference:
 *
 * SinglyLinkedListNode {
 *     int data;
 *     SinglyLinkedListNode next;
 * }
 *
 */
function insertNodeAtPosition(head, data, position) {
    let newNode = new SinglyLinkedListNode(data)
    let current = head;
    while (position - 1) {
        current = current.next;
        position--;
    }
    let temp = current.next;
    current.next = newNode;
    newNode.next = temp;
    // console.log(head);
    return head;
}
