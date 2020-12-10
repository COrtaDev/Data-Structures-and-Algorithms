function quickSort(array) {
  if (array.length <= 1) {
    return array;
  }
  let piv = array.shift();
  let left = array.filter(el => el < piv);
  let right = array.filter(el => el >= piv);

  let leftSorted = quickSort(left);
  let rightSorted = quickSort(right);

  return [...leftSorted, piv, ...rightSorted];
}


module.exports = {
  quickSort
};
