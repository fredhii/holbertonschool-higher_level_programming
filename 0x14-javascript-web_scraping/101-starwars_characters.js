#!/usr/bin/node
let request = require('request');
let episodeNumber = process.argv[2];
let url = 'http://swapi.co/api/films/' + episodeNumber;
request(url, function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    let charDict = {};
    let allChars = JSON.parse(body).characters;
    for (let c in allChars) {
      request(allChars[c], function (err, response, body) {
        if (err) {
          console.log(err);
        } else {
          charDict[c] = JSON.parse(body).name;
        }
        if (allChars.length === Object.keys(charDict).length) {
          for (let key in charDict) {
            console.log(charDict[key]);
          }
        }
      });
    }
  } else {
    console.log('Wrong status code');
  }
});
