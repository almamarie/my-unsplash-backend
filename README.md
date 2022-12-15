<!-- Please update value in the {}  -->

<h1 align="center">{My Unsplash}</h1>

<div align="center">
   Solution for a challenge from  <a href="http://devchallenges.io" target="_blank">Devchallenges.io</a>.
</div>

TODO: Complete the portion below

<div align="center">
  <h3>
    <a href="https://{your-demo-link.your-domain}">
      Demo
    </a>
    <span> | </span>
    <a href="https://{your-url-to-the-solution}">
      Solution
    </a>
    <span> | </span>
    <a href="https://devchallenges.io/challenges/rYyhwJAxMfES5jNQ9YsP">
      Challenge
    </a>
  </h3>
</div>

<!-- TABLE OF CONTENTS -->

## Table of Contents

- [Overview](#overview)
  - [Built With](#built-with)
- [Features](#features)
- [How to use](#how-to-use)
- [Contact](#contact)
- [Acknowledgements](#acknowledgements)

<!-- OVERVIEW -->

## Overview

![screenshot](https://user-images.githubusercontent.com/16707738/92399059-5716eb00-f132-11ea-8b14-bcacdc8ec97b.png)

Introduce your projects by taking a screenshot or a gif. Try to tell visitors a story about your project by answering:

- Where can I see your demo?
- What was your experience?
- What have you learned/improved?
- Your wisdom? :)

### Built With

<!-- This section should list any major frameworks that you built your project using. Here are a few examples.-->

- [React](https://reactjs.org/)
- [Flask](https://flask.palletsprojects.com/en/2.2.x/)

## Features

<!-- List the features of your application or follow the template. Don't share the figma file here :) -->

This application/site was created as a submission to a [DevChallenges](https://devchallenges.io/challenges) challenge. The [challenge](https://devchallenges.io/challenges/rYyhwJAxMfES5jNQ9YsP) was to build an application to complete the given user stories.

## How To Use

<!-- Example: -->

To clone and run this application, you'll need [Git](https://git-scm.com) and [Node.js](https://nodejs.org/en/download/) (which comes with [npm](http://npmjs.com)) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/your-user-name/your-project-name

# Install dependencies
$ npm install

# Run the app
$ npm start
```

## Acknowledgements

<!-- This section should list any articles or add-ons/plugins that helps you to complete the project. This is optional but it will help you in the future. For example: -->

- [Steps to replicate a design with only HTML and CSS](https://devchallenges-blogs.web.app/how-to-replicate-design/)
- [Node.js](https://nodejs.org/)
- [Marked - a markdown parser](https://github.com/chjj/marked)

## Contact

- Website [your-website.com](https://{your-web-site-link})
- GitHub [@your-username](https://{github.com/almamarie})
- Twitter [@your-twitter](https://)

---

# Getting Started

Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, <http://127.0.0.1:5000/>, which is set as a proxy in the frontend configuration.

Authentication: This version of the application does not require authentication or API keys.
Error Handling
Errors are returned as JSON objects in the following format:

```json
{
"success": False,
"error": 400,
"message": "bad request"
}
```

There are 2 ways errors will be sent to the client:

1. These are the http error codes. The API will return three error types when requests fail in the format presented above:

400: Bad Request
404: Resource Not Found
422: Not Processable
405: Method Not Allowed

2. The status_code is 200 but the error is stated in the body of the response. The format is as stated below:

```json
{
"success": False,
"message": "item exists in database. no duplicate items allowed"
}
```

## Endpoints

#### GET '/categories'

Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category

###### Request Arguments: None

Returns: An object with a single key, categories, that contains an object of id: category_string key:value pairs.

```json
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  }
}
```
