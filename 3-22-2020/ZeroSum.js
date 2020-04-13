/*
Date: 3/22/2020
By: Andrew

URL: https://leetcode.com/problems/3sum/
*/

const zeroSumFinder = (array) => {
  if(array.length <= 2){return []}
  let zeroSets = [];
  let length = array.length;

  for(let i = 0; i < length; i++){
    for(let j = i+1; j < length; j++){
      for(let k = j+1; k < length; k++){

        let sum = array[i] + array[j] + array[k];
        if(sum === 0){
          var found = false;
          for(let sets of zeroSets) {

            if(sets.has(array[i]) && sets.has(array[j]) && sets.has(array[k])){
              found = true;
              break;
            }
          }
          if (!found) {
            let set = new Set([array[i], array[j], array[k]]);
            zeroSets.push(set);
          }
        }
      }
    }
  }

  return zeroSets;
}

let nums = [-1, 0, 1, 2, -1, -4];

console.log(zeroSumFinder(nums));
