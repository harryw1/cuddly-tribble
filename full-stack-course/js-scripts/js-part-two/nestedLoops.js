// Write your code below

let bobsFollowers = ['person1','person2','person3','person4',]

let tinasFollowers = ['person4','person5','person1',]

let mutualFollowers = []

for (let i = 0; i < bobsFollowers.length; i++){
  for (let h = 0; h < tinasFollowers.length; h++){
    if (bobsFollowers[i]===tinasFollowers[h]){
      mutualFollowers.push(bobsFollowers[i])
    }
  }
}