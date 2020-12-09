
function swap(arr, index1, index2) {
  let temp = arr[index1];
  arr[index1] = arr[index2];
  arr[index2] = temp;
}

function selectionSort(list) {
 for (let i = 0; i < list.length; i++) {
    let minIndex = i;
    for (let j = i + 1; j < list.length; j++) {
      if (list[minIndex] > list[j]) {
        minIndex = j;
      }
    }
    swap(list, i, minIndex);
  }
  return list;
}

module.exports = {
  selectionSort,
  swap
};
