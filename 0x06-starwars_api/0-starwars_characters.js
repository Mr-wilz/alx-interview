#!/usr/bin/node

/**
 * This script fetches and displays chars in sta wars movie
 */

const request = require('request');

/**
 * Sends a request to the Star Wars API to get characters for the given movie ID
 * and logs each character's name in the specified order.
 *
 * @param {string} movieId - The ID of the movie to fetch characters from
 */

request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (err, res, body) {
  if (err) throw err;
  const actors = JSON.parse(body).characters;
  exactOrder(actors, 0);
});
const exactOrder = (actors, x) => {
  if (x === actors.length) return;
  request(actors[x], function (err, res, body) {
    if (err) throw err;
    console.log(JSON.parse(body).name);
    exactOrder(actors, x + 1);
  });
};
