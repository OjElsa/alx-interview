#!/usr/bin/node

const axios = require('axios');
const process = require('process');

if (process.argv.length !== 3) {
  console.log('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const baseUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

axios.get(baseUrl)
  .then(response => {
    const characters = response.data.characters;
    characters.forEach(characterUrl => {
      axios.get(characterUrl)
        .then(characterResponse => {
          console.log(characterResponse.data.name);
        })
        .catch(error => {
          console.error('Error fetching character:', error);
        });
    });
  })
  .catch(error => {
    console.error('Error fetching movie:', error);
  });
