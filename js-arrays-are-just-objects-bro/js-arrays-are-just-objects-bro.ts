const names = ["Yngve", "Vegard", "Hilde", "Sunniva", "Robin", "Ivar"];
const indices = [0, 1, 2, 3, 4, 5];
const randomizedArray = [];

const chosenIndex = 0;

// JS lar deg ikke poppe på en spesifikk index, så lager en kjapp utility function
function popSpecificIndex(array, index) {
  const popped = array[index];
  array.splice(index, 1);
  return popped;
}

// Konstruer den nye lista med tilfeldig key
for (let name of names) {
  const index = popSpecificIndex(
    indices,
    Math.floor(Math.random() * indices.length)
  );
  Object.defineProperty(randomizedArray, index, { value: name });
}

console.log(randomizedArray[chosenIndex]);
