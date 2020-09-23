#!/usr/bin/node
const request = require('request');

request('https://swapi-api.hbtn.io/api/films', (error, response, body) => {
  if (error) { console.log(error); }
  const json = JSON.parse(body);
  const episode = json.results.filter((element) => parseInt(element.episode_id) === parseInt(process.argv[2]));
  episode[0].characters.forEach(async (url) => {
    await request(url, async (error, response, body) => {
      if (error) { console.log(error); }
      const json = await JSON.parse(body);
      console.log(json.name);
    });
  });
});
