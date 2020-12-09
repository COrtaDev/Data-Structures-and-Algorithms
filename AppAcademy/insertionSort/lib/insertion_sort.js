function insertionSort(list) {
  for (let i = 1; i < list.length; i++) {
    let current = list[i];
    for (var j = i - 1; j >= 0 && current < list[j]; j--) {
      list[j + 1] = list[j];
    }
    list[j + 1] = current;
  }
  return list;
}

module.exports = {
  insertionSort
};
