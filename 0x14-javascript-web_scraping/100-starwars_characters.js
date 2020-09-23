#!/usr/bin/node
let request = require('request');
let episodeNumber = process.argv[2];
let url = 'http://swapi.co/api/films/' + episodeNumber;
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    let allChars = JSON.parse(body).characters;
    for (let c in allChars) {
      let charUrl = allChars[c];
      request(charUrl, function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          let currentChar = JSON.parse(body);
          console.log(currentChar.name);
        }
      });
    }
  } else {
    console.log('Wrong status code');
  }
});
