const process = require('process');
const args = process.argv;
const rest = args.slice(2);
const typed = rest.join(' ');

fetch(require('fs').readFileSync('link.txt').toString() + "/send?typed="+typed, {
    method: 'GET'
})