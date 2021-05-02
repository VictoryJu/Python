// EXAM #1
const numbers = [11, 22, 33, 44, 55];

function refine(item) {
    return new Promise((resolve, reject) => {
        try {
            setTimeout(() => {
                const result = item % 5;
                resolve(result);
            }, Math.random() * 200);
        } catch (e) {
            console.error(e);
            reject(-1);
        }
    });
}

// Solve #1
/*
async function solution() {
    const results: number[] = [];
    for (const item of numbers) {
        console.log(`${item}`)
        results.push(await refine(item));
    }
    return results
}
*/

// Solve #2
function solution() {
    return new Promise(function (resolve, reject) {
        //코드 작성
        try {
            const results = Promise.all(numbers.map(function (item) {
                console.log(`${item}`);
                return refine(item);
            }));
            resolve(results);
        }
        catch (e) {
            console.error(e);
            reject(-1);
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