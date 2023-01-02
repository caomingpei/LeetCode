const {
    PriorityQueue
} = require('@datastructures-js/priority-queue')

/**
 * @param {number[][]} orders
 * @return {number}
 */
var getNumberOfBacklogOrders = function(orders) {
    const MOD = 1000000007;
    const boq = new PriorityQueue((a, b) => b[0] - a[0]);
    const soq = new PriorityQueue((a, b) => a[0] - b[0]);

    for(const ord of orders){
        const [price, amount, ordtype] = ord;
        if(ordtype===0){
            let count =amount;
            while(
                count>0 &&
                !soq.isEmpty() &&
                soq.front()[0] <=price
                ) {
                const sellOrder = soq.dequeue();
                const sellAmount = Math.min(count, sellOrder[1]);
                count -= sellAmount;
                sellOrder[1] -= sellAmount;
                if(sellOrder[1] > 0){
                    soq.enqueue(sellOrder);
                }
            }
            if (count > 0){
                boq.enqueue([price, count]);
            }
        }else{
            let count = amount;
            while (
                count > 0 &&
                !boq.isEmpty() &&
                boq.front()[0] >= price
                ) {
                const buyOrder = boq.dequeue();
                const buyAmount = Math.min(count, buyOrder[1]);
                count -= buyAmount;
                buyOrder[1] -= buyAmount;
                if (buyOrder[1] > 0) {
                    boq.enqueue(buyOrder);
                }
            }
            if (count > 0) {
                soq.enqueue([price, count]);
            }
        }
    }

    let total = 0;
    for (const pq of [boq, soq]) {
        while(!pq.isEmpty()){
            const ord = pq.dequeue();
            total = (total + ord[1]) % MOD;
        }
    }
    return total;
};


const orders = [[10,5,0],[15,2,1],[25,1,1],[30,4,0]]

console.log(getNumberOfBacklogOrders(orders))