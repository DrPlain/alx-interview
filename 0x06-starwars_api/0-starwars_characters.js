#!/usr/bin/node
const request = require('request');
const id = process.argv[2];

const URL = `https://swapi-api.alx-tools.com/api/films/${id}`;

function getRequest (url) {
  return new Promise((resolve, reject) => {
    request.get(url, (error, response, body) => {
      if (error) {
        reject(error);
      }
      if (response.statusCode === 200) {
        resolve(body);
      }
    });
  });
}

async function getCharacters () {
  try {
    const response = await getRequest(URL);
    const data = JSON.parse(response);
    const characters = data.characters;
    const names = [];
    for (const character of characters) {
      try {
        const res = await getRequest(character);
        const data = JSON.parse(res);
        names.push(data.name);
      } catch (error) {
        console.log(error);
      }
    }
    names.forEach((item) => console.log(item));
  } catch (error) {
    console.log(error);
  }
}
getCharacters();
