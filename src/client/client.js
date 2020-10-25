const Axios = require('axios');
const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});
rl.question(`put server's ip address\n`, (answer) => {
    Axios.get(answer)
    .then(response => {
        console.log(response);
    })
    .catch(error => {
        console.log(error);
    })

    rl.close();
  });
