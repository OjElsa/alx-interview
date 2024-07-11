#!/usr/bin/node

const axios = require('axios');
const process = require('process');

if (process.argv.length !== 3) {
  console.log('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const baseUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

async function getCharacterNames(characters) {
  const names = [];

  for (const characterUrl of characters) {
    try {
      const response = await axios.get(characterUrl);
      names.push(response.data.name);
    } catch (error) {
      console.error('Error fetching character:', error);
    }
  }

  return names;
}

async function main() {
  try {
    const response = await axios.get(baseUrl);
    const characters = response.data.characters;

    const characterNames = await getCharacterNames(characters);

    // Print character names in the correct order
    characterNames.forEach(name => {
      console.log(name);
    });

  } catch (error) {
    console.error('Error fetching movie:', error);
  }
}

main();

