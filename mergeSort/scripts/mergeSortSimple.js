// sort two integers
function sortTuple(a, b) {
  sorted = []
  if (a < b) {
    sorted = [a, b]
  } else {
    sorted = [b, a]
  }
  console.log("Sorted tuple: " + sorted)
  return sorted
}

// Take two arrays and return merged array
// a and b should both be sorted arrays
function mergeSortedArrays(a, b) {
  console.log("Merging sorted: [" + a + '], [' + b + ']')
  var i = 0, // index of a
      j = 0, // index of b
      c = [] // merge into c

  while (i < a.length || j < b.length) {
    // if there are still items in both a and b, do a comparison
    if (i < a.length && j < b.length) {
      if (a[i] < b[j]) {
        c.push(a[i])
        i++
      } else {
        c.push(b[j])
        j++
      }
      // if there are still items in a or b, append the rest and push the curser to the end
    } else if (i < a.length) {
      c = c.concat(a.slice(i, a.length))
      i = a.length
    } else if (j < b.length) {
      c = c.concat(b.slice(j, b.length))
      j = b.length
    }
  }
  console.log("Merged: " + c)
  return c
}

function sortOrMerge(array) {
  sorted = []
  if (array.length > 2) {
    // recurse
    sorted = mergeSort(array)
  } else if (array.length == 2) {
    // base case length == 2 sort the tuple
    sorted = sortTuple.apply(this, array)
  } else {
    // base case length == 1, sorted is itself
    sorted = array
  }
  return sorted
}

function mergeSort(array) {
  var halfway = Math.ceil(array.length/2)
  var a = array.slice(0, halfway) // inclusive
  var b = array.slice(halfway, array.length) // exclusive
  console.log("first half: " + a)
  console.log("second half: " + b)

  // sort each half recursively
  var a_sorted = sortOrMerge(a),
      b_sorted = sortOrMerge(b)

  return mergeSortedArrays(a_sorted, b_sorted)
}

// show original array
//
var arr = [];
for (var i = 0, l = 9; i < l; i++) {
    arr.push(Math.round(Math.random() * l))
}

console.log("Unsorted: " + arr)
console.log("Sorted: " + mergeSort(arr))