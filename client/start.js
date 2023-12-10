const fs = require('fs');
const { exec } = require('child_process');

const link = process.argv[2];

if (!link) {
  console.error('Please provide the access link as an argument when running the script.');
  process.exit(1);
}

fs.writeFile('link.txt', link, (err) => {
  if (err) {
    console.error('Error while saving the link:', err);
  } else {
    console.log('Link successfully saved in the file link.txt');
  }
});