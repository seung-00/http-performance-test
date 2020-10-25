const Axios = require('axios');
const ADRESS = 'http://osean.iptime.org:8080/node'

Axios.get(ADRESS)
    .then(response => {
        console.log(response);
    })
    .catch(error => {
        console.log(error);
    })