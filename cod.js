// EXAM #1
const numbers = [11, 22, 33, 44, 55];

function refine(item) {
    return new Promise((resolve, reject) => {
        try {
            setTimeout(() => {
                const result = item % 5;
                resolve(result);
                console.log(result)
            }, Math.random() * 200);
        } catch (e) {
            console.error(e);
            reject(-1);
        }
    });
}

// Solve #1

// async function solution() {
//     const results = [];
//     for (const item of numbers) {
//         console.log(`${item}`)
//         results.push(await refine(item));
//     }
//     return results
// }


//Solve #2
function solution() {
    return new Promise((resolve, reject) => {
      //코드 작성
        let results = [];
        try{
            for(const item of numbers)
                {
                    console.log(`${item}`);
                }
                Promise.resolve()
                        .then(()=>{
                            for(const item of numbers)
                            {
                                results.push(refine(item))
                            };  //순서대로 진행하고 for문이 끝난뒤에 resolve를 하고싶음
                        }).then(results)
                        .then((results)=>resolve(results));  
        }
        catch(e){
            reject(error)
        }
    });
}

// Answer func
(() => {
    solution()
        .then((results) => {
            console.log(`${results}`)
        });
})();

// Expected Answer
/*
11
22
33
44
55
1,2,3,4,0
*/